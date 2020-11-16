from django.contrib import admin

from .models import FriendGroup

# Allowing the admins to regulate the friend groups
admin.site.register(FriendGroup)
