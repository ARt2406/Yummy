from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='events/')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Create your models here.
