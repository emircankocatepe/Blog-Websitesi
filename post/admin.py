from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ['baslik', 'yayimlanma_tarihi']
    list_display_links = ['yayimlanma_tarihi']
    list_filter = ['yayimlanma_tarihi']
    search_fields = ['baslik','metin']
    list_editable = ['baslik']

    class Meta: 
        model = Post

admin.site.register(Post, PostAdmin)