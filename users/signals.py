from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import Profile

@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(signals.post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    