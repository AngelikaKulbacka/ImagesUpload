# Generated by Django 4.2.5 on 2023-09-24 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounttieroption',
            old_name='thumbnail_size',
            new_name='thumbnail_size_1',
        ),
        migrations.AddField(
            model_name='accounttieroption',
            name='thumbnail_size_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accounttieroption',
            name='expiration_duration',
            field=models.PositiveIntegerField(choices=[(300, '5 minutes'), (600, '10 minutes'), (1800, '30 minutes'), (2700, '45 minutes'), (3000, '50 minutes')], default=300),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
