from datetime import datetime
from __future__ import unicode_literals

from django.db import models
from finconuser.models import User


class EntryCategory(models.Model):
    CATEGORY_TYPES = (
        'income',
        'expense',
    )
    category = models.CharField()
    icon = models.ImageField()
    cat_type = models.CharField(choices=CATEGORY_TYPES)


class Entry(models.Model):
    amount = models.DecimalField(decimal_places=2)
    category = models.ForeignKey(EntryCategory)
    note = models.CharField()
    entry_date = models.DateTimeField(default=datetime.date.today)
    owner = models.ForeignKey(User)
