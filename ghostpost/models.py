from django.db import models


# Create your models here.
class Post (models.Model):
    boast = models.BooleanField(default=True)
    roast = models.BooleanField(default=False)
    text = models.CharField(blank=False, null=True, max_length=280)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    public_url = models.CharField(null=True, max_length=30)
    private_url = models.CharField(null=True, max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.score = self.up - self.down
        return super().save(*args, **kwargs)

class Sorter(models.Model):
    sort_by =models.CharField(
        max_length=3)


