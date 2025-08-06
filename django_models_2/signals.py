from django.db.models.signals import post_save
from django.dispatch import receiver

from django_models_2.models import Name, User4, User4Profile

@receiver(post_save, sender=Name)
def create_log_after_save(sender, instance, created, **kwarge):
    if created:
        print(f'created a new Name: {instance.name}')
        # print(f'Sender: {sender}')
    else:
        print(f'updated a name: {instance.id}')

@receiver(post_save, sender=User4)
def auto_create_profile(sender, instance, created, **kwargs):
    if created:
        User4Profile.objects.create(user4 = instance)


