from django.contrib import admin
from .models import Avatar, Profile

# Register your models here.

admin.site.register(Profile)

admin.site.register(Avatar)