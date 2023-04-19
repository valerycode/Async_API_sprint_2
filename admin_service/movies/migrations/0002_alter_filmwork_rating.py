# Generated by Django 4.1.2 on 2022-12-02 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, message='Rating should be greater than 0'), django.core.validators.MaxValueValidator(100, message='Rating should be less than 100')], verbose_name='rating'),
        ),
    ]
