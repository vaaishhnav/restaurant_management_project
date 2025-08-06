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
