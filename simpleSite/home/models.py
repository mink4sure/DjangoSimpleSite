from django.db import models
from django.contrib.auth.models import Group

# Creating a database model for the friend groups
class FriendGroup(Group):
    def __str__(self):
        return self.name
