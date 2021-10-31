from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
  address = models.CharField(max_length=256, blank=False)
  name = models.CharField(max_length=32, blank=False)

  def __str__(self):
    return self.address

class Seat(models.Model):
  store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="seats")
  user = user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="seat")
  number = models.IntegerField(default=0, null=True, blank=True, verbose_name="number")
