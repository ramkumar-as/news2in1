from django.contrib import admin
from .models import Article, ArticleContent, LanguageArticle, LanguageArticleContent

class ArticleContentInline(admin.StackedInline):
    model = ArticleContent
    extra = 1  # Number of empty forms to display

class LanguageArticleContentInline(admin.StackedInline):
    model = LanguageArticleContent
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleContentInline]
    list_display = ('title', 'publish_date', 'category', 'created_by')
    search_fields = ('title', 'category')

class ArticleContentAdmin(admin.ModelAdmin):
    inlines = [LanguageArticleContentInline]
    list_display = ('article', 'content_type')
    search_fields = ('article__title',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleContent, ArticleContentAdmin)
# For LanguageArticle and LanguageArticleContent, simple registration may suffice
admin.site.register(LanguageArticle)
admin.site.register(LanguageArticleContent)
