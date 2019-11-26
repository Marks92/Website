from django.contrib import admin

from .models import People, Genres, Games

# Register your models here.
admin.site.register(People)
admin.site.register(Genres)
admin.site.register(Games)
