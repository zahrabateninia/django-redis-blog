from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Article

LIST_CACHE_KEY = "articles:list:v1"

@receiver(post_save, sender=Article)
@receiver(post_delete, sender=Article)
def clear_article_list_cache(**kwargs):
    cache.delete(LIST_CACHE_KEY)
