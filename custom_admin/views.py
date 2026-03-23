from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from events.models import EventCategory, EventTheme, Order, Feedback
from django.contrib.auth.models import User

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def dashboard(request):
    pending = Order.objects.filter(status='Pending').count()
    confirmed = Order.objects.filter(status='Confirmed').count()
    completed = Order.objects.filter(status='Completed').count()

    context = {
        'total_orders': Order.objects.count(),
        'pending_orders': pending,
        'completed_orders': completed,
        'total_revenue': sum(o.total_price for o in Order.objects.all()),
        'feedback_count': Feedback.objects.count(),
        'user_count': User.objects.filter(is_staff=False).count(),
        'chart_labels': ['Pending', 'Confirmed', 'Completed'],
        'chart_data': [pending, confirmed, completed],
    }
    return render(request, 'custom_admin/dashboard.html', context)

@user_passes_test(is_admin)
def category_list(request):
    categories = EventCategory.objects.all()
    return render(request, 'custom_admin/category_list.html', {'categories': categories})

@user_passes_test(is_admin)
def category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            EventCategory.objects.create(name=name)
            messages.success(request, 'Category added successfully!')
            return redirect('custom_admin:category_list')
    return render(request, 'custom_admin/category_add.html')

@user_passes_test(is_admin)
def theme_list(request):
    themes = EventTheme.objects.select_related('category').all()
    return render(request, 'custom_admin/theme_list.html', {'themes': themes})

@user_passes_test(is_admin)
def theme_add(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        price = request.POST.get('price', 0)
        image = request.FILES.get('image')
        caste_preference = request.POST.get('caste_preference', '')
        
        category = get_object_or_404(EventCategory, id=category_id)
        if name and image:
            EventTheme.objects.create(
                category=category, name=name, description=description, price=price,
                image=image, caste_preference=caste_preference
            )
            messages.success(request, 'Theme added successfully!')
            return redirect('custom_admin:theme_list')
    
    categories = EventCategory.objects.all()
    return render(request, 'custom_admin/theme_add.html', {'categories': categories})

@user_passes_test(is_admin)
def order_list(request):
    orders = Order.objects.select_related('user').order_by('-created_at')
    return render(request, 'custom_admin/order_list.html', {'orders': orders})

@user_passes_test(is_admin)
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        # Check choices correctly, the choices are [("Pending", "Pending"), etc.]
        choices = [c[0] for c in order._meta.get_field('status').choices]
        if status in choices:
            order.status = status
            order.save()
            messages.success(request, 'Order status updated!')
            return redirect('custom_admin:order_detail', order_id=order.id)
    return render(request, 'custom_admin/order_detail.html', {'order': order})

@user_passes_test(is_admin)
def feedback_list(request):
    feedbacks = Feedback.objects.select_related('user').order_by('-created_at')
    return render(request, 'custom_admin/feedback_list.html', {'feedbacks': feedbacks})

@user_passes_test(is_admin)
def customer_list(request):
    customers = User.objects.filter(is_staff=False)
    return render(request, 'custom_admin/customer_list.html', {'customers': customers})
