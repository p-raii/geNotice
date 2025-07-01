from django.db import models
from django.contrib.auth.models import User
from notice.models import Location  # assuming you'll create this in notice app

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"
