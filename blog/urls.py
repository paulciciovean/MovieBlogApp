from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('movies/', views.movies, name='blog-movies'),
    path('actors/', views.actors, name='blog-actors'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('addmovie/', views.add_movies, name='addmovie'),
    path('addactor/', views.add_actor, name='addactor'),
    path('moviewatchlist/<movie_id>', views.add_to_watchlist, name='add-watchlist'),
    path('removemoviewatchlist/<movie_id>', views.remove_to_watchlist, name='remove-watchlist'),
    path('addreview/<movie_id>', views.add_review, name='add-review'),
    path('showmovie/<movie_id>', views.show_movie, name='show-movie'),
    path('myreviews/<user_id>', views.my_reviews, name='myreviews'),
    path('search_movies/', views.search_movies, name='search-movies'),
    path('addrating/<movie_id>', views.add_rating, name='add-rating'),
    path('myratings/<user_id>', views.my_ratings, name='myratings'),
    path('update_review/<review_id>', views.update_review, name='update-review'),
    path('update_rating/<rating_id>', views.update_rating, name='update-rating'),
    path('delete_rating/<rating_id>', views.delete_rating, name='delete-rating'),
    path('delete_review/<review_id>', views.delete_review, name='delete-review'),
]
