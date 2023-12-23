from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models.functions import Length

from .models import Article


class ArticalAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'date', 'get_html_image')
    list_display_links = ('id','title')
    search_fields = ('title', 'content')
    
    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src=' {object.image.url} ' width=50>")
        



admin.site.register(Article, ArticalAdmin)