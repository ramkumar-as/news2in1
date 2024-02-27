# Inside your app's urls.py file

from django.urls import path
from .views import about_us, article_detail, contact
from news import views


urlpatterns = [
    #add root url here
    path('robots.txt/', views.robots_txt), 
    path('about-us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('career/', views.career_home, name='career_home'),
    path('career/<int:jobid>/<slug:slug>.html', views.job_detail, name='job_detail'),

    path('', views.home, name='home'),
    path('<str:language>/', views.home, name='home_by_language'),  # Add this line
    # add path for language and visibility
    path('<str:language>/<str:visibility>/', views.home, name='home_by_language_visibility'),
    path('<str:language>/<int:year>/<int:month>/<int:day>/<str:category>/<slug:slug>.html', article_detail, name='article_detail'),
    # Other URL patterns...
  
]
