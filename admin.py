from django.contrib import admin
from .models import Post

class Postco(admin.ModelAdmin):
    list_display =[
        "Title", "Text", "Author", "created_date", "published_date"
        ]
# Register your models here.
admin.site.register(Post, Postco)
