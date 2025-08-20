from django import forms
from .models import ContactSubmission, Feedabck, Contact


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

class ContactForm(forms.ModelForm):
        class Meta:
                model = Contact
                        fields = ['name', 'email']