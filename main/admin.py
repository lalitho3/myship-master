from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'foto', 'mensaje')

admin.site.register(Post, PostAdmin)

