from django.shortcuts import render
from .models import Restaurant
from .models import Dishes
from django.views.generic import DetailView,TemplateView,ListView

# Create your views here.
class RestaurantDetail(ListView):
  model = Restaurant
  template_name = 'restaurant/base.html'
  context_objectname='restaurant_list'
class DishesView(ListView):
  model=Dishes
  template_name='restaurant/__disheslist.html'
  context_objcetname="dishes_list"
  


