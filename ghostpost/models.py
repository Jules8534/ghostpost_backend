from django.db import models
from django.utils import timezone

# Create your models here.
class Post (models.Model):
    boast = models.BooleanField(default=False)
    roast = models.BooleanField(default=False)
    text = models.CharField(blank=False, null=True, max_length=280)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


