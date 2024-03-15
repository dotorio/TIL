from django.contrib import admin
from .models import Product

# Register your models here.
# admin site에 등록한다. Aritcle 클래스를
admin.site.register(Product)
