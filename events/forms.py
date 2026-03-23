from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, EventBooking, Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']


from django import forms
from .models import EventBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = ['theme', 'date', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }


