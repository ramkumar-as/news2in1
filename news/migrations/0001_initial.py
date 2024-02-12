# Generated by Django 5.0.2 on 2024-02-11 19:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.DateField()),
                ('category', models.CharField(max_length=100)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('text', 'Text'), ('media', 'Media')], max_length=10)),
                ('content', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='news.article')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=10)),
                ('title_translation', models.CharField(max_length=255)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='translation', to='news.article')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageArticleContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=10)),
                ('text_translation', models.TextField()),
                ('article_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='news.articlecontent')),
            ],
        ),
    ]
