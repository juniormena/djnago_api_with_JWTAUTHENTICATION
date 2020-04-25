from django.db import models

# Create your models here.
class articles(models.Model):
    description = models.CharField(max_length=120)
    choices =(
    ('A', 'Available'),
    ('S', 'Sold'),
    ('R', 'Restocking'),
    )
    status = models.CharField(max_length=10, choices=choices, default='S')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description