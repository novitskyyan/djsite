# Generated by Django 3.2.16 on 2024-01-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]