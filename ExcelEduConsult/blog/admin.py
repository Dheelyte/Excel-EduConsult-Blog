from django.contrib import admin
from .models import Post, Tag

admin.site.site_header = "Excel Edu Consult"
admin.site.site_title = "Excel Edu Consult Admin Dashboard"
admin.site.index_title = "Welcome to the Excel Edu Consult Admin Dashboard"

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'tag', 'content', 'author', 'thumbnail']}),
    ]
    list_display = ('title', 'date_posted')
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)