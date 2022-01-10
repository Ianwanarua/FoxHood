from hood.models import Business, Neighbourhood, Post, Profile
from django.contrib import admin

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)