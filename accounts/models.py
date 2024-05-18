from django.db import models

# Create your models here.


class Account(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
