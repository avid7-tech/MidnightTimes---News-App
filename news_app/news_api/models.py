from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Keyword(models.Model):
    """
    Model representing a keyword associated with a user.
    
    Attributes:
        user (ForeignKey): Reference to the user who added the keyword.
        text (CharField): The keyword text.
        created_at (DateTimeField): Timestamp when the keyword was created.
        updated_at (DateTimeField): Timestamp when the keyword was last updated.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'news_api_keyword'

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'


class SearchHistory(models.Model):
    """
    Model representing a search history entry for a keyword search by a user.
    
    Attributes:
        user (ForeignKey): Reference to the user who performed the search.
        keyword (CharField): The keyword that was searched.
        results (JSONField): The results of the search stored in JSON format.
        last_fetched (DateTimeField): Timestamp when the search results were last fetched.
        searched_at (DateTimeField): Timestamp when the search was performed.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    results = models.JSONField(default=dict)
    last_fetched = models.DateTimeField(default=timezone.now)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword
