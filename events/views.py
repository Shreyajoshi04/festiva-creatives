from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import EventCategory, EventTheme, CartItem, Order

# -------------------- Home & Themes --------------------

def home(request):
    categories = EventCategory.objects.all()
    return render(request, 'events/home.html', {'categories': categories})

def themes_by_category(request, category_id):
    category = get_object_or_404(EventCategory, id=category_id)
    themes = EventTheme.objects.filter(category=category)
    return render(request, 'events/themes.html', {'category': category, 'themes': themes})

# -------------------- Cart --------------------

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.theme.price * item.quantity for item in cart_items)
    return render(request, 'events/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def add_to_cart(request, theme_id):
    theme = get_object_or_404(EventTheme, id=theme_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, theme=theme)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('view_cart')

# -------------------- Checkout & Orders --------------------

@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.theme.price * item.quantity for item in items)
    if request.method == 'POST':
        address = request.POST['address']
        order = Order.objects.create(user=request.user, total_price=total, address=address)
        items.delete()  # clear cart after checkout
        return redirect('orders')
    return render(request, 'events/checkout.html', {'items': items, 'total': total})

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'events/orders.html', {'orders': orders})

# -------------------- Authentication --------------------

def signup(request):   # Register new user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'events/signup.html', {'form': form})

def login_view(request):   # Login existing user
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})

def logout_view(request):   # Logout user
    logout(request)
    return redirect('signup')
