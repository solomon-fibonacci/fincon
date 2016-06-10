from __future__ import unicode_literals
from userplus.models import UserPlus


class User(UserPlus):
    REQUIRED_FILEDS = ['first_name', 'last_name']
