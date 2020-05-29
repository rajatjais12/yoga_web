from django.conf.urls import url
from django.contrib import admin 
from django.urls import path ,include
from django.conf.urls.static import static
from . import views




app_name = 'base'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('', views.home_page, name='home'),
    path('yoge_category/<str:Sategory_slug>/', views.home_page, name='product_list_by_sategory'),
    path('<int:id>/<str:slug>', views.product_detail, name='sub_product_list'),

    #path('<int:id>/<str:slug>/', views.product_detail, name='sub_product_list'),
    ]