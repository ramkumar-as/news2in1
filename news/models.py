from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image

LANGUAGE_CHOICES = (
    ('tamil', 'Tamil'),
    ('hindi', 'Hindi'),
)    
CATEGORY_CHOICES = (
    ('world', 'World'),
    ('sports', 'Sports'),
)
    # New visibility field
PRIVATE = 'private'
PUBLIC = 'public'
DRAFT = 'draft'
VISIBILITY_CHOICES = [
    (PRIVATE, 'Private'),
    (PUBLIC, 'Public'),
    (DRAFT, 'Draft'),
]
class Article(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    modified_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique_for_date='publish_date')
    thumbnail = models.ImageField(upload_to='media/', blank=True, null=True)


    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES,
        default=DRAFT,
    )
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
  
        if self.thumbnail:
            img = Image.open(self.thumbnail.path)
            output_size = (300, 300)  # Desired thumbnail size
            img.thumbnail(output_size, Image.ANTIALIAS)
            img.save(self.thumbnail.path)
                  
    def __str__(self):
        return f"{self.title}"


class ArticleContent(models.Model):
    article = models.ForeignKey(Article, related_name='contents', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=15, choices=(('text', 'Text'), ('media', 'Media'), ('external_link','External Link')))
    content = models.TextField()  # Stores text directly or URL for media
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True, help_text="Include a YouTube or Instagram link.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            # Resize the image
            img.thumbnail((800, 800), Image.ADAPTIVE)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.content[:50]}..."

class LanguageArticle(models.Model):
    article = models.ForeignKey(Article, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    title_translation = models.CharField(max_length=255)

    def get_static_path(self):
        return f"/{self.language}/{self.article.publish_date.year}/{self.article.publish_date.month}/{self.article.publish_date.day}/{self.article.category}/{self.article.slug}.html"

    def __str__(self):
        return f"{self.article.title} - {self.language}"

class LanguageArticleContent(models.Model):
    article_content = models.ForeignKey(ArticleContent, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    text_translation = models.TextField()

    def __str__(self):
        return f"{self.text_translation}"
