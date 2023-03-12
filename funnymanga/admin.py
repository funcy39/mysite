from django.contrib import admin
from .models import Picture, Comment

# Register your models here.

# class PictureAdmin(admin.ModelAdmin):
#     fields = [
#         (None,               {'fields': ['picture_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

admin.site.register(Picture)
admin.site.register(Comment)