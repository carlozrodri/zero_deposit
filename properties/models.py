from django.db import models
from users.models import User


class Property(models.Model):
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    rooms = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address