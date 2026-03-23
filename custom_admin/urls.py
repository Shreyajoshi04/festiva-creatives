from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('themes/', views.theme_list, name='theme_list'),
    path('themes/add/', views.theme_add, name='theme_add'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('customers/', views.customer_list, name='customer_list'),
]
