from django.db import models
from django.contrib.auth.models import Group


class FriendGroup(Group):
    def __str__(self):
        return self.name
