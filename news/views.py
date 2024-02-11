# Inside your app's views.py file
from django.shortcuts import render

def about_us(request):
    return render(request, 'news/about_us.html')

def contact(request):
    return render(request, 'news/contact.html')

def home(request):
    return render(request, 'news/home.html')  # Adjust the path based on your app's name