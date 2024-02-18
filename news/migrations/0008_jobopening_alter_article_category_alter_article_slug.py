# Generated by Django 5.0.2 on 2024-02-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_article_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('about_company', models.TextField()),
                ('position_overview', models.TextField()),
                ('key_responsibilities', models.TextField()),
                ('qualifications', models.TextField()),
                ('what_we_offer', models.TextField()),
                ('application_process', models.TextField()),
                ('compensation', models.DecimalField(decimal_places=2, max_digits=10)),
                ('job_status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN', max_length=6)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('world', 'World'), ('sports', 'Sports')], default='world', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique_for_date='publish_date'),
        ),
    ]
