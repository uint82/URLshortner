from django.db import models
from django.utils import timezone

# Create your models here.

class URLMapping(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.short_code} -> {self.original_url[:50]}"
    
    class Meta:
        ordering = ['-created_at']
