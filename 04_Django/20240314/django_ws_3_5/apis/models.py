from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_api_url_length(value):
    if len(value) < 15 or len(value) > 60:
        raise ValidationError('API URL length should be between 15 and 60 characters.')

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(validators=[URLValidator(), validate_api_url_length])
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
