# users/signals.py

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    messages.success(request, _(f'You have successfully logged in as {user.username}.'))

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    messages.success(request, _('You have been successfully logged out.'))
