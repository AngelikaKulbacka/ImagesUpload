from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class AccountTier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class AccountTierOption(models.Model):
    account_tier = models.ForeignKey(AccountTier, on_delete=models.CASCADE)
    thumbnail_size_1 = models.IntegerField(null=True, blank=True)
    thumbnail_size_2 = models.IntegerField(null=True, blank=True)
    include_original_link = models.BooleanField(default=False)
    generate_expiring_link = models.BooleanField(default=False)
    expiration_duration = models.PositiveIntegerField(choices=[(0, '---'), (300, '5 minutes'), (600, '10 minutes'), (1800, '30 minutes'), (2700, '45 minutes'), (3000, '50 minutes')], default=0)

    def __str__(self):
        return f"{self.account_tier.name} Option"


class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='list-images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded by {self.user.name}"