from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Movie(models.Model):
    CATEGORIES =  (
        ('Comedy','Comedy'),
        ('Romance','Romance'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Adventure', 'Adventure'),
        ('Sci-Fi','SciFi'),
        ('Crime','Crime'),
        ('Biography','Biography'),
        ('Histroy', 'History')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    year = models.IntegerField(default=2000)
    category = models.CharField(max_length=200,null=True, choices=CATEGORIES)
    image = models.ImageField(null=True,blank=True,default='images/default.png',upload_to='images/')
    actors = models.ManyToManyField('Actor',null = False, blank=True)
    mean_rating = models.FloatField(null=True,blank=True)
    rating_count = models.IntegerField(null=True,blank=True,default=0)

    def __str__(self):
        return self.title

class Watchlist(models.Model):
    movie = models.ManyToManyField(Movie , null = True )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return ( 'Watchlist ' + self.user_id.username )

class Actor(models.Model):

    name = models.CharField(max_length=200)
    birthYear = models.IntegerField(default=1930)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True,default='images/default.png',upload_to='images/')
    movies = models.ManyToManyField(Movie, null = False, blank=True)
    def __str__(self):
        return (self.name)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    context = models.TextField()
    date = models.DateField(default=datetime.now(),blank=True)

    class Meta:
        unique_together = ('user', 'movie',)
    def __str__(self):
        return ('Review ' + self.user.username + ' for '+ self.movie.title)

class Rating(models.Model):
    Numbers = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=2,null=True, choices=Numbers)
    star1 = models.ImageField(null=True,blank=True,default='images/orangestar.png',upload_to='images/')
    star2 = models.ImageField(null=True, blank=True, default='images/bluestar.jpeg', upload_to='images/')

    class Meta:
        unique_together = ('user', 'movie',)
    def __str__(self):
        return ('Rating ' + self.user.username + ' for '+ self.movie.title + ' is '+ str(self.rating))

