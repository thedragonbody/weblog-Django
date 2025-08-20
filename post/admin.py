from django.contrib import admin

# Register your models here.

from .models import post, comment

class commentadmininline(admin.TabularInline):
    model = comment
    fields = ['txt']
    extra = 0

@admin.register(post)
class post_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enable', 'publish_date', 'created_time', 'update_time']
    inlines = [commentadmininline]

# class comment_admin(admin.ModelAdmin):
    # list_display = ['post', 'txt', 'created_time']


# admin.site.register(post, post_admin)
# admin.site.register(comment, comment_admin)