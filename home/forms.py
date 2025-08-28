from django import forms
from .models import ContactSubmission, Feedabck, Contact


class ContactForm(forms.ModelForm):
        class Meta:
                model = Contact
                        fields = ['name', 'email', 'message']

                            def clean_message(self):
                                    message = self.cleaned_data.get('message')
                                            if not message or len(message.strip()) < 5:
                                                        raise forms.ValidationError("Message must be at least 5 characters long.")
                                                                return message

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
            model = ContactMessage
            fields = ['name', 'email', 'message']