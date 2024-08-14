from django.contrib import admin
from .models import *


class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'dateCreation']
    list_filter = ('author', 'dateCreation')


class RespondAdmin(admin.ModelAdmin):
    list_display = ['author', 'ad', 'dateCreation', 'status']
    list_filter = ('status', 'dateCreation')
    search_fields = ('author', 'text')

admin.site.register(UserResponse, RespondAdmin)
admin.site.register(Article, AdAdmin)

# Register your models here.
