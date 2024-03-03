from django.contrib import admin
from .models import Article, ArticleContent, JobOpening, LanguageArticle, LanguageArticleContent
from nested_inline.admin import NestedStackedInline, NestedModelAdmin



class LanguageArticleContentInline(NestedStackedInline):
    model = LanguageArticleContent
    extra = 1
    fk_name = 'article_content'  # Adjust based on your model's ForeignKey field

class ArticleContentInline(NestedStackedInline):

    model = ArticleContent
    extra = 1
    inlines = [LanguageArticleContentInline]

class LanguageArticleInline(admin.TabularInline):
    
    model = LanguageArticle
    extra = 1  # Number of extra forms to display

class ArticleAdmin(NestedModelAdmin):
    class Media:
        css = {
            "all": (    
                "admin/css/forms.css",
            )
        }
    inlines = [ArticleContentInline]
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
admin.site.register(LanguageArticle)
#admin.site.register(LanguageArticleContent)
admin.site.register(JobOpening, JobOpeningAdmin)