# Generated by Django 5.1.5 on 2025-01-28 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
