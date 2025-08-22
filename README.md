# django-redis-blog

I built a simple Django blog where:

You can create and view articles (title + content).

I added Redis caching so pages load faster by storing results in memory.

Without Redis → every request goes to the database.

With Redis → repeated requests are served directly from cache.

This is a learning project: Django (backend), Redis (cache).
