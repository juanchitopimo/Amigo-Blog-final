from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Notification
# Import Post if you want to trigger notifications for posts
from blog.models import Post
from django.contrib.auth.signals import user_logged_in
from django.contrib import messages

# To create the profile picture


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# To save profile picture


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# To send a welcome message when user logs in


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    messages.success(request, f'Hola or hello, {user.username}!')
    Notification.objects.create(
        user=user, message="You've successfully logged in.")
