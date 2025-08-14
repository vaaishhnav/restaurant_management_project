from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)



class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} - {self.submitted_at:%Y-%m-%d %H:%M}"