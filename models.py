from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=200, null=True)  
    email = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    CATEGORY_CHOICES = (
         ('math', 'Math'),
         ('technology', 'Technology'),
         ('bacci', 'Bacci'),
         ('learn_ai', 'Learn AI'),
    )

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='books/')  
    link = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    category = models.CharField (
        max_length=20,
    choices=CATEGORY_CHOICES,
            default='math' 

    ) 

    def __str__(self):
        return f"{self.title} ({self.category})"