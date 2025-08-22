from django.shortcuts import render
import time
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.cache import cache
from .models import Article

LIST_CACHE_KEY = "articles:list:v1"
LIST_TTL = 60  

def article_list(request):
    # count visits via session (stored in Redis)
    request.session["visits"] = request.session.get("visits", 0) + 1
    visits = request.session["visits"]

    cached_html = cache.get(LIST_CACHE_KEY)
    if cached_html is not None:
        # served from Redis
        return HttpResponse(cached_html)

    # simulate slow work on cache miss 
    time.sleep(2)

    articles = Article.objects.all()
    html = render_to_string(
        "articles/list.html",
        {"articles": articles, "visits": visits, "cached": False},
        request=request,
    )
    cache.set(LIST_CACHE_KEY, html, LIST_TTL)
    return HttpResponse(html)
