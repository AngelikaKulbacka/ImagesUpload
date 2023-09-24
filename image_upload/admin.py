from django.contrib import admin
from django.contrib.auth.models import Group
from .models import AccountTier, AccountTierOption, UploadedImage

basic_group, _ = Group.objects.get_or_create(name='Basic')
premium_group, _ = Group.objects.get_or_create(name='Premium')
enterprise_group, _ = Group.objects.get_or_create(name='Enterprise')

@admin.register(AccountTier)
class AccountTierAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(AccountTierOption)
class AccountTierOptionAdmin(admin.ModelAdmin):
    list_display = ('account_tier', 'thumbnail_size_1', 'thumbnail_size_2', 'include_original_link', 'generate_expiring_link')

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'uploaded_at')
