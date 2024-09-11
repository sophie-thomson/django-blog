from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# decorator is how we register a class, not just standard model
# register it with a decorator that is more Pythonic
# allows us to customise how the model will appear on the admin site
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
# admin.site.register(Post) - COMMENTED OUT as @admin.register(Post) decorator does this
admin.site.register(Comment)