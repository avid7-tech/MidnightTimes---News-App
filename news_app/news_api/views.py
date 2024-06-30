from django.shortcuts import render
from django.core.cache import cache
import requests
from dotenv import load_dotenv
import os

load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

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
