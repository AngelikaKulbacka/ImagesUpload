from rest_framework import serializers
from .models import UploadedImage, AccountTier, AccountTierOption


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = '__all__'


class AccountTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTier
        fields = '__all__'


class AccountTierOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTierOption
        fields = '__all__'