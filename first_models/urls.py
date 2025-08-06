from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('blog/', views.blog_post, name='blog_post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product_list/', views.product_list, name='product_list'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
    path('post_form1/', views.create_post1, name='create_post1')



]
