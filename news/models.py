from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image
from openai import OpenAI
from news2in1 import settings
import os
from openai import OpenAI
from news2in1 import settings



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
JOB_STATUS_CHOICES = [
    ('OPEN', 'Open'),
    ('CLOSED', 'Closed'),
]

def translate_content(content):
    api_key =settings.OPENAI_API_KEY
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",  # or another model name
        messages=[{"role": "user", "content": f'Translate the following English text to Tamil: {content}'}]
    )
    translation = response.choices[0].message.content.strip()
    return translation
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,default='world')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    modified_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique_for_date='publish_date', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media/', blank=True, null=True)
  

    
    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES,
        default=DRAFT,
    )
 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        is_new_article = not self.pk  # Check if it is a new article
        super().save(*args, **kwargs)

        if self.thumbnail:
            img = Image.open(self.thumbnail.path)
            output_size = (300, 300)  # Desired thumbnail size
            img.thumbnail(output_size, Image.ADAPTIVE)
            img.save(self.thumbnail.path)

        if is_new_article:  
            translation = translate_content(content=self.title)
            LanguageArticle.objects.create(article=self, title_translation=translation, language='tamil')

    def __str__(self):
        return f"{self.title}"

   

class ArticleContent(models.Model):
    article = models.ForeignKey(Article, related_name='contents', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=15, choices=(('text', 'Text'), ('media', 'Media'), ('external_link','External Link')))
    content = models.TextField()  # Stores text directly or URL for media
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True, help_text="Include a YouTube or Instagram link.")

    def save(self, *args, **kwargs):
        is_new_record = not self.pk  # Check if it is a new article
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            # Resize the image
            img.thumbnail((800, 800), Image.ADAPTIVE)
            img.save(self.image.path)

        # Translate the content to Tamil and save it in the LanguageArticleContent model
        # Only if it is a new content    
        if is_new_record and self.content_type == 'text':    
            translation = translate_content(content=self.content)
            LanguageArticleContent.objects.create(article_content=self, text_translation=translation, language='tamil')

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

class JobOpening(models.Model):

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    about_company = models.TextField()
    position_overview = models.TextField()
    key_responsibilities = models.TextField()
    qualifications = models.TextField()
    what_we_offer = models.TextField()
    application_process = models.TextField()
    compensation = models.CharField(max_length=200)
    job_status = models.CharField(max_length=6, choices=JOB_STATUS_CHOICES, default='OPEN')
    posted_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def get_static_path(self):
        return f"/career/{self.pk}/{self.slug}.html"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title