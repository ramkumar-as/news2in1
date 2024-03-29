# Generated by Django 5.0.2 on 2024-02-12 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_articlecontent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='visibility',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='external_link',
            field=models.URLField(blank=True, help_text='Include a YouTube or Instagram link.', null=True),
        ),
        migrations.AlterField(
            model_name='articlecontent',
            name='content_type',
            field=models.CharField(choices=[('text', 'Text'), ('media', 'Media'), ('external_link', 'External Link')], max_length=15),
        ),
    ]
