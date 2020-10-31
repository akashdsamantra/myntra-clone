from django.db import models

SIZES_CHOICES = [
    ('s', 'Small'),
    ('m', 'Medium'),
    ('l', 'Large'),
    ('xl', 'Extra Large')
]

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    address = models.CharField(max_length=16000)
    country_of_origin = models.CharField(max_length = 256)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    alternate_phone_number = models.CharField(max_length=10, unique=True, null=True, blank=True)

class Product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=16000, null=True, blank=True)
    price = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    discount = models.CharField(max_length=10)
    # images = ArrayField(models.CharField(max_length=256))
    # sizes_available = ArrayField(models.CharField(choices=SIZES_CHOICES, max_length=3))
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
