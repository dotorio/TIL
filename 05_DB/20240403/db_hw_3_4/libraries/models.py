from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()
    nationality = models.TextField()

    def __str__(self):
        return self.name
    
    def book_count(self):
        cnt = len(self.book_set.all())
        return f'{cnt}권 '

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    adult = models.BooleanField()
    price = models.IntegerField()