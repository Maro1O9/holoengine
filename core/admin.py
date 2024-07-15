import profile
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, Media, Profile

# Register your models here.

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [MediaInline]
    list_display = ('id', 'user', 'text', 'created_at')

class UserInline(admin.TabularInline):
    model = Profile
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [UserInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(Post, PostAdmin)
admin.site.unregister(User)
admin.site.register(User,ProfileAdmin)
