from django.db import models

# Create your models here.
class Apiinfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.CharField(max_length=200)
    documentation_url = models.CharField(max_length=200)
    auth_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField()