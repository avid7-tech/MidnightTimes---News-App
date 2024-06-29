from django.shortcuts import render
import requests
from datetime import datetime
import logging

API_KEY = '70a4cd3ca43d42dfae7423d7ee157628'
logger = logging.getLogger(__name__)

def home(request):
    keyword = request.GET.get('keyword')
    sort = request.GET.get('sort')


    if keyword:
        try:
            url = f'https://newsapi.org/v2/everything?q={keyword}&from=2024-05-29&sortBy=publishedAt&apiKey={API_KEY}'
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            data = response.json()
            articles = data['articles']
            
            if sort == 'date_asc':
                articles.sort(key=lambda x: datetime.strptime(x['publishedAt'][:10], '%Y-%m-%d'))
            elif sort == 'date_desc':
                articles.sort(key=lambda x: datetime.strptime(x['publishedAt'][:10], '%Y-%m-%d'), reverse=True)
        
        except requests.exceptions.RequestException as e:
            # Handle errors like network issues or invalid API key
            context = {'error': f"An error occurred: {e}"}
        else:
            context = {'articles': articles}

        return render(request, 'news_api/home.html', context)

    else:
        # Handle case where no keyword is provided
        context = {}
        return render(request, 'news_api/home.html', context)
