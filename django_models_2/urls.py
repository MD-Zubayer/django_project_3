from django.urls import path
from django_models_2.views import home1
from . import views
urlpatterns = [
    path('', views.home1, name='home'),
    # path('create_view/', views.create_view, name='create_view'),
    path('create_view/', views.create_view2, name='create_view2'),
    path('list_view/', views.list_view, name='list_view'),
    path('test/', views.AccessOnToOnField, name='AccessOnToOnField'),
    path('test2/', views.AccessManyToManyField, name='AccessManyToManyField')

]