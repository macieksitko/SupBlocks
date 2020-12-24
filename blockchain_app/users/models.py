
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randrange
from .services import validate_address

links =  [
    ('producer', 'Producer'),
    ('shipper', 'Shipper'),
    ('wholesaler', 'Wholesaler'),
    ('detailer', 'Detailer'),
    ]

class UserProfile(AbstractUser):
    widget = models.CharField(max_length=20, choices=links,verbose_name="Choose your link",default=links[0])
    nonce = models.IntegerField(default=randrange(1000000,9999999))
    public_address = models.CharField(max_length=20,validators=[validate_address])


