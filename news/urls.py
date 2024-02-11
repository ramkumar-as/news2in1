# Inside your app's urls.py file

from django.urls import path
from .views import about_us, contact, home

urlpatterns = [
    path('about-us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('', home, name='home'),

    # Include other URL patterns
]
