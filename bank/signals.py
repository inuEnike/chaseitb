from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import *

def profile_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='profile')
        instance.groups.add(group)
        Profile.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(profile_profile, sender=User)


def deposit(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='deposit')
        instance.groups.add(group)
        Deposit.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(deposit, sender=User)


def card(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='card')
        instance.groups.add(group)
        Card.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(card, sender=User)



def accountnumber(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='accountnumber')
        instance.groups.add(group)
        Accountnumber.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(accountnumber, sender=User)


def transfer(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='transfer')
        instance.groups.add(group)
        Transfer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(transfer, sender=User)


def withdraw(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='withdraw')
        instance.groups.add(group)
        Withdraw.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(withdraw, sender=User)

def pin(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='pin')
        instance.groups.add(group)
        Pin.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(pin, sender=User)