# Generated by Django 5.0.2 on 2024-02-18 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_jobopening_compensation'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopening',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
