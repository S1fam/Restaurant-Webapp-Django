from django.urls import path
from . import views  # from current directory import views.py

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),  # homepage
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='item_detail'),
    path('about/', views.About.as_view(), name='about')
]
