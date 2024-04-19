from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.contrib import messages
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    messages.success(request, _(f'You have successfully logged in as {user.username}.'))

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    messages.success(request, _('You have been successfully logged out.'))

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created,**kwargs):
    if created:
        instance.userprofile.save()