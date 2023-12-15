from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.item_name  # this we can see in table row instead of Item object(1)

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField("Item Name", max_length=255)
    item_desc = models.CharField("Item Description", max_length=255)
    item_price = models.IntegerField("Item Price")
    item_image = models.CharField("Item Image", max_length=500,
                                  default="https://images.unsplash.com/photo-1430163393927-3dab9af7ea38?q=80&w=1470")

    def get_absolute_url(self):
        return reverse("food:details", kwargs={"pk": self.pk})
