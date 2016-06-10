from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from bookkeeper.models import EntryCategory
from finconuser.models import User


class BudgetItem(models.Model):
    owner = models.ForeignKey(User)
    category = models.ForeignKey(EntryCategory)
    amount = models.DecimalField(decimal_places=2)
    period_of_days = models.IntegerField()
    start_date = models.DateField(default=datetime.date.today)
