import imp
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.cretae(user=instance)

@receiver(post_save,sender=RelationShip)
def post_save_add_friend(sender,instance,created,**kwargs):
    # import pdb;pdb.set_trace()
    sender_=instance.sender
    receiver_=instance.receiver
    if instance.status=='accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)

        sender_.save()
        receiver_.save()