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
