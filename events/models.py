from django.db import models
from django.contrib.auth.models import User

class EventCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EventTheme(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(default="No description available")
<<<<<<< HEAD
    price = models.FloatField(default=0.0)   # ✅ float to avoid conversion errors
    image = models.ImageField(upload_to='themes/')

=======
    price = models.FloatField(default=0.0)   # float for simplicity
    image = models.ImageField(upload_to='themes/')
    caste_preference = models.CharField(max_length=100, blank=True, null=True, help_text="For marriage events")
>>>>>>> f7b8409 (Initial commit with cart functionality)

    def __str__(self):
        return self.name


<<<<<<< HEAD


=======
>>>>>>> f7b8409 (Initial commit with cart functionality)
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(EventTheme, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.theme.name} x {self.quantity}"


<<<<<<< HEAD

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


=======
>>>>>>> f7b8409 (Initial commit with cart functionality)
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"
<<<<<<< HEAD
=======


# events/models.py
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    payment_method = models.CharField(max_length=50, default="COD")
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Confirmed", "Confirmed"), ("Completed", "Completed")],
        default="Pending"
    )
    special_request = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"



>>>>>>> f7b8409 (Initial commit with cart functionality)
