from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Location
from notice.models import Notice

# Inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    max_num = 1  # Only allow one


# Extend the default User admin to include Profile inline
class UserAdmin(DefaultUserAdmin):
    inlines = (ProfileInline,)

# Unregister the default User admin and register the new one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

# Register Notice model with some customization
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'created_at')
    list_filter = ('location', 'created_at')
    search_fields = ('title', 'description')
