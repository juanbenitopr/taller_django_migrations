from django.contrib.auth.models import User
from django.db import models

from django.db.models import CASCADE, ForeignKey


class Account(models.Model):
    amoun = models.FloatField(default=1)
    owner = ForeignKey(User, on_delete=CASCADE, null=True)

class AccountUser(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, related_name='owners')
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name='accounts')
