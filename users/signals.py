from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
