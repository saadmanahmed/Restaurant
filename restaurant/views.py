from django.shortcuts import render
from .models import Restaurant
from .models import Dishes
from django.views.generic import DetailView,TemplateView

# Create your views here.
class RestaurantDetail(TemplateView):
  model = Restaurant
  template_name = 'restaurant/restaurant_list.html'
  


