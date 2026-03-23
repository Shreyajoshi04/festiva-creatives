from django.contrib import admin
<<<<<<< HEAD
from .models import EventCategory, EventTheme, Feedback

admin.site.register(EventCategory)
admin.site.register(EventTheme)
admin.site.register(Feedback)

# Register your models here.
=======
from django.contrib.auth.models import User
from .models import EventCategory, EventTheme, Feedback, Order

# ---------------------------
# Event Category Admin
# ---------------------------
@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)

# ---------------------------
# Event Theme Admin
# ---------------------------
@admin.register(EventTheme)
class EventThemeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "description")
    ordering = ("category", "name")

# ---------------------------
# Feedback Admin
# ---------------------------
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "message", "created_at")
    search_fields = ("user__username", "message")
    ordering = ("-created_at",)

# ---------------------------
# Order Admin
# ---------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_price", "payment_method", "status", "created_at")
    list_filter = ("status", "payment_method", "created_at")
    search_fields = ("user__username", "address", "special_request")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Order Info", {
            "fields": ("user", "total_price", "payment_method", "status")
        }),
        ("Delivery Details", {
            "fields": ("address", "special_request")
        }),
        ("Timestamps", {
            "fields": ("created_at",)
        }),
    )

# ---------------------------
# Branding for Admin Panel
# ---------------------------
admin.site.site_header = "Festiva Creatives Dashboard"
admin.site.site_title = "Festiva Creatives Control Panel"
admin.site.index_title = "Welcome to Festiva Management"

from django.contrib.admin import AdminSite
from django.contrib.auth.models import User

class FestivaAdmin(AdminSite):
    site_header = "Festiva Creatives Dashboard"
    site_title = "Festiva Creatives Control Panel"
    index_title = "Welcome to Festiva Management"

    def each_context(self, request):
        context = super().each_context(request)
        context['total_orders'] = Order.objects.count()
        context['pending_orders'] = Order.objects.filter(status="Pending").count()
        context['completed_orders'] = Order.objects.filter(status="Completed").count()
        context['total_revenue'] = sum(o.total_price for o in Order.objects.all())
        context['feedback_count'] = Feedback.objects.count()
        context['user_count'] = User.objects.count()
        return context

festiva_admin = FestivaAdmin(name="festiva_admin")
>>>>>>> f7b8409 (Initial commit with cart functionality)
