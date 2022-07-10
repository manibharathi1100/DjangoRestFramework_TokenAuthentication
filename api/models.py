from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    email_id = models.EmailField(max_length=100, unique=True)
    account_id = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=50)

class Meta:
    db_table = "Account"

def __str__(self):
    return self.email_id

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

