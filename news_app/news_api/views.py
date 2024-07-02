from django.shortcuts import render
from django.core.cache import cache
import requests
from dotenv import load_dotenv
import os

from .models import Keyword
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect
from .forms import KeywordForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

@login_required
def home(request):
    keyword = request.GET.get('keyword')
    language = request.GET.get('language')
    category = request.GET.get('category')
    sortBy = request.GET.get('sortBy')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')      

    if keyword:
        cache_key = f'news_{keyword}'  # Unique cache key based on keyword

        # Check if cached data exists
        cached_articles = cache.get(cache_key)
        if cached_articles:
            return render(request, 'news_api/home.html', {'articles': cached_articles})

        try:
            url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}'
            # LANGUAGE
            if language:
                url += f'&language={language}'
            # CATEGORY
            if category:
                url += f'&category={category}'
            # SORT BY
            if sortBy:
                url += f'&sortBy={sortBy}'
            # DATE RANGE
            if from_date:
                url += f'&from={from_date}'
            if to_date:
                url += f'&to={to_date}'
            
            
            
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            data = response.json()
            articles = data['articles']

            # Cache the fetched data for 15 minutes (900 seconds)
            cache.set(cache_key, articles, 900)

            context = {'articles': articles}

        except requests.exceptions.RequestException as e:
            # Handle errors like network issues or invalid API key
            context = {'error': f"An error occurred: {e}"}

    else:
        # Handle case where no keyword is provided
        context = {}

    return render(request, 'news_api/home.html', context)


def register(request):
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
  # Filter keywords based on current logged-in user
  keywords = Keyword.objects.filter(user=request.user).order_by('-created_at')
  return render(request, 'keyword_list.html', {'keywords': keywords})

@login_required
def keyword_create(request):
  if request.method == "POST":
      form = KeywordForm(request.POST)
      if form.is_valid():
          text = form.cleaned_data['text'].strip()  # Strip whitespace from text
          # Check if the keyword already exists for the user
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
  keyword = get_object_or_404(Keyword, pk=keyword_id, user = request.user)
  if request.method == 'POST':
    keyword.delete()
    return redirect('keyword_list')
  return render(request, 'keyword_confirm_delete.html', {'keyword': keyword})


@login_required
def control(request):
    
    # Get all users (excluding the currently logged-in user)
    users = User.objects.filter(is_superuser=False).exclude(pk=request.user.pk)

    # Context data for the template
    context = {'users': users}

    return render(request, 'control_panel/control_panel.html', context)


def block_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)

        # Toggle the user's active status
        user.is_active = not user.is_active
        user.save()

        # Redirect back to the control panel
        return redirect('control')

    return redirect('control')  # Redirect if not a POST request


def set_limit(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)

        # Get the posted limit value (ensure it's an integer)
        try:
            limit = int(request.POST['limit'])
            if limit < 1:
                raise ValueError("Limit must be a positive integer.")
        except (ValueError, KeyError):
            # Handle invalid or missing limit data
            error_message = "Invalid limit value. Please enter a positive integer."
            return render(request, 'control_panel/control_panel.html', {'error': error_message, 'users': User.objects.filter(is_superuser=False).exclude(pk=request.user.pk)})

        # Update the user's keyword limit (assuming you have a `keyword_limit` field)
        user.keyword_limit = limit
        user.save()

        context = {'success_message': "Keyword limit updated successfully!"}
        return render(request, 'control_panel/control_panel.html', context)


    return redirect('control')  # Redirect if not a POST request

from django.shortcuts import render

def not_authorized(request):
  return render(request, 'control_panel/not_auth.html')  # New template for non-superuser message

def signin(request):
  # Your existing login logic here
  if request.user.is_authenticated:
    if request.user.is_superuser:
      # Allow superuser to access the control panel
      return redirect('control')
    else:
      # Redirect non-superuser login attempts
      return redirect('not_authorized')
