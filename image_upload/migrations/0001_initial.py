# Generated by Django 4.2.5 on 2023-09-24 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountTierOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail_size', models.IntegerField()),
                ('include_original_link', models.BooleanField(default=False)),
                ('generate_expiring_link', models.BooleanField(default=False)),
                ('expiration_duration', models.PositiveIntegerField(choices=[(300, '5 minutes'), (600, '10 minutes'), (1800, '30 minutes')])),
                ('account_tier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_upload.accounttier')),
            ],
        ),
    ]
