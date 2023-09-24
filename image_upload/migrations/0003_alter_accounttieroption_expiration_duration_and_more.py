# Generated by Django 4.2.5 on 2023-09-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0002_rename_thumbnail_size_accounttieroption_thumbnail_size_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttieroption',
            name='expiration_duration',
            field=models.PositiveIntegerField(choices=[(0, '---'), (300, '5 minutes'), (600, '10 minutes'), (1800, '30 minutes'), (2700, '45 minutes'), (3000, '50 minutes')], default=0),
        ),
        migrations.AlterField(
            model_name='accounttieroption',
            name='thumbnail_size_1',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]