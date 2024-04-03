from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants,
    }
    return render(request, 'restaurants/index.html', context)

def detail(request, restaurant_pk):
    location = Restaurant.objects.get(pk=restaurant_pk)
    context = {
        'location' : location,
    }
    return render(request, 'restaurant/detail.html', context)

def create(request, restaurant_pk):
    location = Restaurant.objects.get(pk=restaurant_pk)
    if location.is_valid():
        
