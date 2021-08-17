from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from blog.models import Watchlist

@receiver(post_save, sender=User)
def create_watchlist(sender, instance, created, **kwargs):
    if created:
        Watchlist.objects.create(user_id =instance)

@receiver(post_save, sender=User)
def save_watchlist(sender, instance, created, **kwargs):
    instance.watchlist.save()
