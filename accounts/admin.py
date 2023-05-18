from django.contrib import admin

from . models import User, GoogleSignUser

# Register your models here.
admin.site.register(User)
admin.site.register(GoogleSignUser)
# admin.site.register(Hotel)
