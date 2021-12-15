from django.contrib import admin

# Register your models here.
from .models import Project, Watchlist

admin.site.register(Project)
admin.site.register(Watchlist)
