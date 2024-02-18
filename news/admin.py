from django.contrib import admin
from .models import Article, ArticleContent, JobOpening, LanguageArticle, LanguageArticleContent

class ArticleContentInline(admin.StackedInline):
    model = ArticleContent
    extra = 1  # Number of empty forms to display

class LanguageArticleContentInline(admin.StackedInline):
    model = LanguageArticleContent
    extra = 1

class LanguageArticleInline(admin.TabularInline):
    model = LanguageArticle
    extra = 1  # Number of extra forms to display

class ArticleAdmin(admin.ModelAdmin):
    inlines = [LanguageArticleInline]
    list_display = ('title', 'publish_date', 'category', 'created_by')
    search_fields = ('title', 'category')

class ArticleContentAdmin(admin.ModelAdmin):
    inlines = [LanguageArticleContentInline]
    list_display = ('article', 'content_type')
    search_fields = ('article__title',)

class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'job_status')
    search_fields = ('title', 'location')
    


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleContent, ArticleContentAdmin)
# For LanguageArticle and LanguageArticleContent, simple registration may suffice
#admin.site.register(LanguageArticle)
#admin.site.register(LanguageArticleContent)
admin.site.register(JobOpening, JobOpeningAdmin)