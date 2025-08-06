from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver

from django_models_2.models import Name, User4, User4Profile, Product, User5, User5profile

# ✅ Step 1: post_save
@receiver(post_save, sender=Name)
def create_log_after_save(sender, instance, created, **kwarge):
    if created:
        print(f'created a new Name: {instance.name}')
        # print(f'Sender: {sender}')
    else:
        print(f'updated a name: {instance.id}')

 # ✅ 1. Create Profile automatically when User is created
@receiver(post_save, sender=User4)
def auto_create_profile(sender, instance, created, **kwargs):
    if created:
        User4Profile.objects.create(user4 = instance)
        print(f'✅ Profile created for user: {instance.name}')

# ✅ 2. Set default bio after profile is created
@receiver(post_save, sender=User4Profile)
def set_default_bio(sender, instance, created, *args, **kwargs):
    if created and not instance.bio:
        instance.bio = 'this is a default bio.'
        instance.full_clean()
        instance.save()
        print(f'✅ Default bio set for : {instance.user4.name}')




@receiver(post_save, sender=Product)
def send_welcome_email(sender, instance, created, *args, **kwargs):
    if created:
        print(f'Product created {instance.name}! Email sent')
    else:
        print(f'Product updated {instance.name}')

# ✅ pre_save
@receiver(pre_save, sender=Product)
def set_default_price(sender, instance, *args, **kwargs):
    if instance.price <= 0:
        instance.price = 100


class User5Signals:

    @staticmethod
    def create_profile(sender, instance,created, *args, **kwargs):
        if created:
            User5profile.objects.create(user5=instance)
            print(f'✅ Profile created for : {instance.name}')
    @staticmethod
    def delete_profile(sender, instance, *args, **kwargs):
        User5profile.objects.filter(user5=instance).delete()
        print(f'❌ Profile deleted for {instance.name}')


# ✅ Signals connect here
post_save.connect(User5Signals.create_profile, sender=User5)
post_delete.connect(User5Signals.delete_profile, sender=User5)
