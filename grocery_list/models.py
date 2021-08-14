from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
status_choices = [
    ('bought', 'Bought'),
    ('left', 'Left'),
    ('not available', 'Not Available')
]

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_quantity = models.IntegerField()
    item_status = models.CharField(max_length=20, choices=status_choices, default='green')
    date = models.DateTimeField(default = timezone.now)

