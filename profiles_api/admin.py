from django.contrib import admin
from .models import (
    UserProfile,
    ProfileFeedItem
)

admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)

