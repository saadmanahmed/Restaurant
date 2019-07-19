from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from .models import Restaurant, Dishes
from .views import RestaurantDetail
from .views import DishesView
from django.urls import path
urlpatterns = [


    path('',RestaurantDetail.as_view()),
    path('',DishesView.as_view()),
        ]