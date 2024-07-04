from django.shortcuts import render
from django.core.cache import cache
import requests
from dotenv import load_dotenv
import os
from django.db.models import Count
from .models import Keyword
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect
from .forms import KeywordForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import SearchHistory
import re


load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')


def sanitize_cache_key(key):
    """
    Sanitize the cache key by replacing any non-alphanumeric character with an underscore.

    Args:
        key (str): The original cache key.

    Returns:
        str: The sanitized cache key.
    """
    return re.sub(r'[^a-zA-Z0-9]', '_', key)

@login_required
def home(request):
    """
    Home view for fetching and displaying news articles based on user input.

    This view handles the following parameters from the request:
    - `keyword`: The search keyword for news articles.
    - `language`: The language filter for news articles.
    - `category`: The category filter for news articles.
    - `sortBy`: The sort order for news articles.
    - `from_date`: The start date for filtering news articles.
    - `to_date`: The end date for filtering news articles.
    - `refresh`: Boolean flag to refresh the cached articles.

    The view performs the following operations:
    1. Fetches the search keyword and other parameters from the request.
    2. Checks if there is a cached result for the keyword. If found and `refresh` is not set, it uses the cached results.
    3. If no cached result is found or `refresh` is set, it makes a request to the News API.
    4. Saves the fetched results in the cache and updates the search history for the user.
    5. Renders the results in the 'news_api/home.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page with news articles or error message.
    """
    keyword = request.GET.get('keyword')
    language = request.GET.get('language')
    category = request.GET.get('category')
    sortBy = request.GET.get('sortBy')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    refresh = request.GET.get('refresh')  # New parameter for refresh
    
    context = {}
    
    if keyword:
        history_entry = SearchHistory.objects.filter(user=request.user, keyword=keyword).first()
        if refresh and history_entry:
            last_fetched = history_entry.last_fetched.strftime('%Y-%m-%d')
            # Use the later of the provided from_date or last_fetched
            if not from_date or from_date < last_fetched:
                from_date = last_fetched

        sanitized_keyword = sanitize_cache_key(keyword)
        cache_key = f'news_{sanitized_keyword}'
        cached_articles = cache.get(cache_key)

        if cached_articles and not refresh:
            context['articles'] = cached_articles
        else:
            try:
                url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}'
                if language:
                    url += f'&language={language}'
                if category:
                    url += f'&category={category}'
                if sortBy:
                    url += f'&sortBy={sortBy}'
                if from_date:
                    url += f'&from={from_date}'
                if to_date:
                    url += f'&to={to_date}'
                
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                articles = data['articles']
                
                cache.set(cache_key, articles, 900)
                if history_entry:
                    history_entry.results = articles
                    history_entry.last_fetched = timezone.now()
                    history_entry.save()
                else:
                    SearchHistory.objects.create(user=request.user, keyword=keyword, results=articles)

                context['articles'] = articles
            except requests.exceptions.RequestException as e:
                context['error'] = f"An error occurred: {e}"

    return render(request, 'news_api/home.html', context)



@login_required
def search_history(request):
    """
    View for displaying the search history of the logged-in user.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered template with the user's search history.
    """
    search_history = SearchHistory.objects.filter(user=request.user).order_by('-searched_at')
    return render(request, 'news_api/search_history.html', {'search_history': search_history})

def register(request):
    """
    View for user registration.

    Handles user registration, password setting, and automatic login upon successful registration.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered registration form or redirect to the keyword list.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('keyword_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def keyword_list(request):
    """
    View for listing keywords added by the logged-in user.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered template with the list of keywords.
    """
    # Filter keywords based on current logged-in user
    keywords = Keyword.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'keyword_list.html', {'keywords': keywords})

@login_required
def keyword_create(request):
    """
    View for creating a new keyword for the logged-in user.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered keyword form or redirect to the keyword list.
    """
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text'].strip()
            existing_keyword = Keyword.objects.filter(user=request.user, text__iexact=text).first()
            if existing_keyword:
                form.add_error('text', 'You have already added this keyword!')
            else:
                keyword = form.save(commit=False)
                keyword.user = request.user
                keyword.save()
                return redirect('keyword_list')
    else:
        form = KeywordForm()
    return render(request, 'keyword_form.html', {'form': form})


@login_required
def keyword_delete(request, keyword_id):
    """
    View for deleting a keyword of the logged-in user.

    Args:
        request (HttpRequest): The request object.
        keyword_id (int): The ID of the keyword to be deleted.

    Returns:
        HttpResponse: Redirect to the keyword list or confirmation page.
    """
    keyword = get_object_or_404(Keyword, pk=keyword_id, user = request.user)
    if request.method == 'POST':
        keyword.delete()
        return redirect('keyword_list')
    return render(request, 'keyword_confirm_delete.html', {'keyword': keyword})

def block_user(request, user_id):
    """
    View for blocking or unblocking a user.

    Args:
        request (HttpRequest): The request object.
        user_id (int): The ID of the user to be blocked or unblocked.

    Returns:
        HttpResponse: Redirect to the control panel.
    """
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)

        user.is_active = not user.is_active
        user.save()

        return redirect('control')

    return redirect('control')


def set_limit(request, user_id):
    """
    View for setting a keyword limit for a user.

    Args:
        request (HttpRequest): The request object.
        user_id (int): The ID of the user for whom the limit is to be set.

    Returns:
        HttpResponse: Rendered template with success or error message, or redirect to the control panel.
    """
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)
        try:
            limit = int(request.POST['limit'])
            if limit < 1:
                raise ValueError("Limit must be a positive integer.")
        except (ValueError, KeyError):
            # Handle invalid or missing limit data
            error_message = "Invalid limit value. Please enter a positive integer."
            return render(request, 'control_panel/control_panel.html', {'error': error_message, 'users': User.objects.filter(is_superuser=False).exclude(pk=request.user.pk)})

        user.keyword_limit = limit
        user.save()

        context = {'success_message': "Keyword limit updated successfully!"}
        return render(request, 'control_panel/control_panel.html', context)


    return redirect('control')

def not_authorized(request):
    """
    View for displaying a not authorized message to non-superusers.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered template with not authorized message.
    """
    return render(request, 'control_panel/not_auth.html')

def signin(request):
    """
    View for handling user sign-in.

    Redirects authenticated users based on their status (superuser or not).

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Redirect to control panel or not authorized page.
    """
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('control')
        else:
            return redirect('not_authorized')

@login_required
def control(request):
    """
    View for the control panel accessible only to superusers.

    Displays a list of all non-superuser users and the top-10 trending keywords based on search history.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered template with control panel data.
    """
    users = User.objects.filter(is_superuser=False).exclude(pk=request.user.pk)

    trending_keywords = SearchHistory.objects.values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count')[:10]

    context = {
        'users': users,
        'trending_keywords': trending_keywords,
    }

    return render(request, 'control_panel/control_panel.html', context)

# @login_required
# def control(request):
#     """
#     View for the control panel accessible only to superusers.

#     Displays a list of all non-superuser users and trending keywords.

#     Args:
#         request (HttpRequest): The request object.

#     Returns:
#         HttpResponse: Rendered template with control panel data.
#     """
#     # Get all users (excluding the currently logged-in user)
#     users = User.objects.filter(is_superuser=False).exclude(pk=request.user.pk)

#     # Context data for the template
#     context = {'users': users}

#     return render(request, 'control_panel/control_panel.html', context)