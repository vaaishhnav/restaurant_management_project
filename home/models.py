from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
        address = models.TextField(blank=True)   # <-- address field added
            phone = models.CharField(max_length=30, blank=True)  # optional
                opening_hours = models.JSONField(default=dict, blank=True)  # optional

                    def __str__(self):
                            return self.name
                            

class Feedback(models.Model):
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} - {self.submitted_at:%Y-%m-%d %H:%M}"

class RestaurantLocation(models.Model):
        address = models.CharField(max_length=255)
            city = models.CharField(max_length=100)
                state = models.CharField(max_length=100)
                    zip_code = models.CharField(max_length=20)

                        def __str__(self):
                                return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"

class Contact(models.Model):
        name = models.CharField(max_length=100)
            email = models.EmailField()
                submitted_at = models.DateTimeField(auto_now_add=True)

                    def __str__(self):
                            return f"{self.name} - {self.email}"