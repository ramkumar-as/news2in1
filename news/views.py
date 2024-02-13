# Inside your app's views.py file
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Article, LanguageArticle, LanguageArticleContent, ArticleContent
from django.shortcuts import render, get_object_or_404
from news.models import Article

def about_us(request):
    return render(request, 'news/about_us.html')

def contact(request):
    return render(request, 'news/contact.html')


def home(request, language=None):
    if language:
        # Fetch LanguageArticle instances that match the specified language.
        language_articles = LanguageArticle.objects.filter(language=language, article__visibility='public').order_by('-article__publish_date').select_related('article')
    else:
        # If no language is specified, you might choose a default behavior.
        language_articles = LanguageArticle.objects.filter(article__visibility='public').order_by('-article__publish_date').select_related('article')

    return render(request, 'news/home.html', {'language_articles': language_articles})


def article_detail(request, language, year, month, day, category, slug):
    # Fetch the article
    article = get_object_or_404(Article, slug=slug, publish_date__year=year, 
                                publish_date__month=month, publish_date__day=day, category=category)
    
    language_article = get_object_or_404(LanguageArticle, article=article, language=language)
    # Fetch ArticleContents for the selected article
    article_contents = ArticleContent.objects.filter(article=article).order_by('id')
    
    # Fetch LanguageArticleContents for the selected language and related to the article contents
    language_article_contents = LanguageArticleContent.objects.filter(
        article_content__in=article_contents, language=language).select_related('article_content').order_by('article_content__id')

    # Organize translations to easily map them to their respective ArticleContent
    translations_map = {trans.article_content_id: trans for trans in language_article_contents}

    return render(request, 'news/article_detail.html', {
        'language_article': language_article,
        'article_contents': article_contents,
        'translations_map': translations_map,
        'selected_language': language
    })
