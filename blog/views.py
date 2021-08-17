from django.shortcuts import render,redirect
from .models import Movie, Watchlist , Actor, User, Review, Rating
from django.contrib import messages
from .forms import CreateMovie, CreateActor, CreateReview, CreateRating
from django.contrib.auth.decorators import login_required
import statistics

def home(request):
    reviews = Review.objects.all().order_by('?')
    usr = request.user
    ratings = usr.rating_set.all()
    context = {
        'reviews': reviews,
        'ratings': ratings
    }
    return render(request , 'home.html',context)

def about(request):
    return render(request, 'about.html')


def movies(request):
    movies = Movie.objects.all().order_by('?')
    for mv in movies:

        mean_rating=0
        ratings = Rating.objects.filter(movie=mv)
        if ratings.count() > 0:
            for rating in ratings:
                mean_rating += rating.rating

            mean_rating = mean_rating / ratings.count()
            mv.rating_count=ratings.count()
            mv.mean_rating=format(mean_rating,".1f")
            mv.save()


    context = {
        'movies': movies,

    }

    return render(request, 'movies.html', context)

def add_movies(request):

    if request.method=="POST":
        form = CreateMovie(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            m = Movie.objects.last()
            a = m.actors.all()
            for actor in a:
                actor.movies.add(m)
            messages.success(request, 'The movie was successfully added ')
            redirect('blog-home')
    else:
        form = CreateMovie()


    return render(request, 'addmovie.html',{ 'form':form})

def actors(request):
    acts = Actor.objects.all()
    context = {
        'actors': acts
    }
    return render(request, 'actors.html', context)

def add_actor(request):

    if request.method == "POST":
        form = CreateActor(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            a = Actor.objects.last()
            m = a.movies.all()
            for movie in m:
                movie.actors.add(a)
            messages.success(request, 'The actor was successfully added ')
            redirect('blog-home')
    else:
        form = CreateActor()


    return render(request, 'addactor.html',{ 'form':form})

def watchlist(request):
    user = request.user
    wl = user.watchlist
    movieswl = wl.movie.all()
    context = {
        'movieswl': movieswl
    }
    return render(request, 'watchlist.html', context)

def add_to_watchlist(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    user = request.user
    wl = user.watchlist
    wl.movie.add(movie)
    messages.success(request, 'The movie was successfully added to your watchlist')
    return redirect('watchlist')

def remove_to_watchlist(request, movie_id):
    user = request.user
    wl = user.watchlist
    mv = Movie.objects.get(id=movie_id)
    wl.movie.remove(mv)
    messages.info(request, 'The movie was removed from your watchlist')
    return redirect('watchlist')

def add_review(request,movie_id):
    user1 = request.user
    movie1 = Movie.objects.get(id=movie_id)
    review = Review(user=user1 , movie=movie1)
    if request.method == 'POST':
        form = CreateReview(request.POST)
        if form.is_valid():
            review.context = request.POST['context']
            try:
                review.save()
                messages.success(request, 'The review was posted')
            except:
                messages.warning(request, 'You already added a review for this movie , you can not add more')
                return redirect('blog-movies')
            return redirect('blog-home')
    else:
        form = CreateReview()

    return render(request, 'addreview.html', {'form': form, 'movie':movie1})

@login_required(login_url='users-login')
def show_movie(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    actors = movie.actor_set.all
    reviews = movie.review_set.all()

    return render(request,'showmovie.html',{ 'movie':movie,'actors':actors,'reviews':reviews})

@login_required(login_url='users-login')
def my_reviews(request,user_id):
    usr = User.objects.get(id=user_id)
    reviews = usr.review_set.all()
    return render(request, 'myreviews.html', {'reviews': reviews})

@login_required(login_url='users-login')
def my_ratings(request,user_id):
    usr = User.objects.get(id=user_id)
    ratings = usr.rating_set.all()
    return render(request, 'myratings.html', {'ratings': ratings})

@login_required(login_url='users-login')
def add_rating(request,movie_id):
    user1 = request.user
    movie1 = Movie.objects.get(id=movie_id)
    rating = Rating(user=user1 , movie=movie1)
    if request.method == 'POST':
        form = CreateRating(request.POST)
        if form.is_valid():
            rating.rating = request.POST['rating']
            try:
                rating.save()
                messages.success(request, 'The rating was saved')
            except:
                messages.warning(request, 'You already added rating for this movie , you can only update it')
                return redirect('blog-movies')
            return redirect('blog-home')
    else:
        form = CreateRating()

    return render(request, 'addrating.html', {'form': form, 'movie':movie1})

def search_movies(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        movies_searched = Movie.objects.filter(title__contains=searched)
        actors_searched = Actor.objects.filter(name__contains=searched)
        return render(request, 'search_movies.html',{'searched':searched, 'movies_searched':movies_searched, 'actors_searched':actors_searched } )

    return render(request,'search_movies.html',{})

@login_required(login_url='users-login')
def update_review(request,review_id):
    usr = request.user
    usr_reviews = usr.review_set.all()
    review = Review.objects.get(id=review_id)
    movie = review.movie
    if( review in usr_reviews):
        if request.method == 'POST':
            form = CreateReview(request.POST)
            if form.is_valid():
                review.context = request.POST['update_context']
                try:
                    review.save()
                    messages.success(request, 'The review was updated')
                    return redirect('blog-home')
                except:
                    messages.warning(request, 'You already added a review for this movie , you can not add more')
                    return redirect('blog-movies')

        else:
            form = CreateReview()
    else:
        messages.warning(request, 'You can update other people reviews')
        return redirect('blog-home')
    return render(request, 'update_review.html', {'review': review, 'movie':movie })

@login_required(login_url='users-login')
def update_rating(request,rating_id):
    usr = request.user
    usr_ratings = usr.rating_set.all()
    rating = Rating.objects.get(id=rating_id)
    movie = rating.movie
    if ( rating in usr_ratings):
        form = CreateRating(request.POST)
        if form.is_valid():
            rating.rating = request.POST['rating']
            rating.save()
            messages.success(request, 'The rating was updated')
            return redirect('blog-home')
        else:
            form=CreateRating()
    else:
        messages.warning(request, 'You can not update other people ratings')
        return redirect('blog-home')


    return render(request, 'update_rating.html', {'rating':rating, 'movie': movie,'form':form })

@login_required(login_url='users-login')
def delete_rating(request,rating_id):
    usr = request.user
    rating = Rating.objects.get(id=rating_id)
    if usr == rating.user:
        if rating:
            rating.delete()
            messages.success(request,"The rating was removed")
            return redirect('blog-movies')
    else:
        messages.warning(request,"You can't delete other people ratings")
    return render(request, 'delete_rating.html', {'rating':rating,})

@login_required(login_url='users-login')
def delete_review(request,review_id):
    usr = request.user
    review = Review.objects.get(id=review_id)
    if usr == review.user:
        if review:
            review.delete()
            messages.success(request,"The review was deleted")
            return redirect('blog-home')
    else:
        messages.warning(request,"You can't delete other people reviews")
    return render(request, 'delete_review.html', {'review':review,})
