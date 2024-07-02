from django.contrib import admin
from .models import Keyword, SearchHistory


admin.site.register(Keyword)

admin.site.register(SearchHistory)
