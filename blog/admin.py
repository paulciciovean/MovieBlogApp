from django.contrib import admin

from .models import Movie, Watchlist, Actor, Review, Rating
admin.site.register(Movie)
admin.site.register(Watchlist)
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Rating)

