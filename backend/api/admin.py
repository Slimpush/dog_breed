from django.contrib import admin

from .models import Breed, Dog

admin.site.register(Dog)
admin.site.register(Breed)
