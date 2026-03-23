from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
<<<<<<< HEAD

urlpatterns = [
    path('', views.home, name='home'),
    path('themes/<int:category_id>/', views.themes, name='themes'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<int:theme_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('category/<int:category_id>/themes/', views.themes_by_category, name='themes_by_category'),
]

=======
from django.urls import path
from .views import dashboard_view

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Themes
    path('themes/<int:category_id>/', views.themes, name='themes'),
    path('category/<int:category_id>/themes/', views.themes_by_category, name='themes_by_category'),

    # Cart
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:theme_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),

    # Checkout & Orders
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_id>/bill/', views.generate_bill, name='generate_bill'),
    path('payment/success/', views.payment_success, name='payment_success'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_view, name='accounts_login'),
    path("dashboard/", dashboard_view, name="dashboard"),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]
>>>>>>> f7b8409 (Initial commit with cart functionality)
