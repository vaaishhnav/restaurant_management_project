from django import forms
from .models import ContactSubmission, Feedabck


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
            fields = ['name', 'email']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Tell us what you think..."
           })
        }
        labels = {"comment": "Your feedback"}