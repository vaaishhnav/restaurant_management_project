from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)



class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        description = models.TextField(blank=True)
            price = models.DecimalField(max_digits=7, decimal_places=2)
                image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # <-- NEW
                    created_at = models.DateTimeField(auto_now_add=True)

                        def __str__(self):
                                return self.name

                                    def get_image_url(self):
                                            """
                                                    Helper: returns URL if image exists, else empty string (useful in templates).
                                                            """
                                                                    if self.image and hasattr(self.image, 'url'):
                                                                                return self.image.url
                                                                                        return ''

class Restaurant(models.Model):
        name = models.CharField(max_length=100)
            address = models.TextField(blank=True)
                phone = models.CharField(max_length=20, blank=True)
                    # Store opening hours as JSON/dict: {"Mon-Fri": "11am-9pm", "Sat-Sun": "10am-10pm"}
                        opening_hours = models.JSONField(default=dict, blank=True)

                            def __str__(self):
                                    return self.item_name