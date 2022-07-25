from django.contrib import admin

from django.contrib import admin
from Blog.models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')

admin.site.register(Blog, BlogAdmin)