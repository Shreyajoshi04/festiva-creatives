from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import EventCategory, EventTheme, CartItem, Order

# -------------------- Home & Themes --------------------

def home(request):
    categories = EventCategory.objects.all()
<<<<<<< HEAD
    return render(request, 'events/home.html', {'categories': categories})
=======
    themes = EventTheme.objects.all()[:6]  # Fetch top 6 themes for display
    return render(request, 'events/home.html', {'categories': categories, 'themes': themes})

def themes(request, category_id):
    category = get_object_or_404(EventCategory, id=category_id)
    themes = EventTheme.objects.filter(category=category)
    return render(request, 'events/themes.html', {'category': category, 'themes': themes})
>>>>>>> f7b8409 (Initial commit with cart functionality)

def themes_by_category(request, category_id):
    category = get_object_or_404(EventCategory, id=category_id)
    themes = EventTheme.objects.filter(category=category)
    return render(request, 'events/themes.html', {'category': category, 'themes': themes})

# -------------------- Cart --------------------

@login_required
<<<<<<< HEAD
def view_cart(request):
=======
def cart(request):
>>>>>>> f7b8409 (Initial commit with cart functionality)
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
<<<<<<< HEAD
    return redirect('view_cart')
=======
    return redirect('cart')
>>>>>>> f7b8409 (Initial commit with cart functionality)

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
<<<<<<< HEAD
    return redirect('view_cart')
=======
    return redirect('cart')
>>>>>>> f7b8409 (Initial commit with cart functionality)

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
<<<<<<< HEAD
    return redirect('view_cart')
=======
    return redirect('cart')
>>>>>>> f7b8409 (Initial commit with cart functionality)

# -------------------- Checkout & Orders --------------------

@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.theme.price * item.quantity for item in items)
<<<<<<< HEAD
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
=======

    if request.method == 'POST':
        address = request.POST.get('address', '')
        payment_method = request.POST.get('payment_method', 'COD')
        order = Order.objects.create(
            user=request.user,
            total_price=total,
            address=address,
            status="Pending",
        )
        # You can store payment_method in the Order model if you add a field for it
        items.delete()
        return redirect('orders')

    return render(request, 'events/checkout.html', {
        'items': items,
        'total': total,
    })


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import razorpay
from django.conf import settings

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        data = request.POST

        # Verify signature using Razorpay utility
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        try:
            client.utility.verify_payment_signature(data)
            # TODO: Update the corresponding Order in your DB
            # e.g., Order.objects.filter(id=data['order_id']).update(status="Paid")
            return JsonResponse({"status": "success"})
        except:
            return JsonResponse({"status": "failed"})




@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'events/orders.html', {'orders': orders})

@login_required
def generate_bill(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # Ensure customers can only print their own bill, while admins can access any bill.
    if not request.user.is_staff and order.user != request.user:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("You are not allowed to view this bill.")
    return render(request, 'events/bill.html', {'order': order})
# -------------------- Authentication --------------------

def signup(request):
>>>>>>> f7b8409 (Initial commit with cart functionality)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
<<<<<<< HEAD
            login(request, user)  # log in after signup
=======
            login(request, user)
>>>>>>> f7b8409 (Initial commit with cart functionality)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'events/signup.html', {'form': form})

<<<<<<< HEAD
def login_view(request):   # Login existing user
=======
def login_view(request):
>>>>>>> f7b8409 (Initial commit with cart functionality)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})

<<<<<<< HEAD
def logout_view(request):   # Logout user
    logout(request)
    return redirect('signup')
=======
def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order, Feedback

def dashboard_view(request):
    context = {
        "total_orders": Order.objects.count(),
        "pending_orders": Order.objects.filter(status="Pending").count(),
        "completed_orders": Order.objects.filter(status="Completed").count(),
        "total_revenue": sum(o.total_price for o in Order.objects.all()),
        "feedback_count": Feedback.objects.count(),
        "user_count": User.objects.count(),
    }
    return render(request, "events/dashboard.html", context)

from django.contrib import messages

@login_required
def submit_feedback(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Feedback.objects.create(user=request.user, message=message)
            messages.success(request, 'Thank you for your feedback!')
            return redirect('home')
    return render(request, 'events/feedback.html')



>>>>>>> f7b8409 (Initial commit with cart functionality)
