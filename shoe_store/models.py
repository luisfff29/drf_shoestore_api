from django.db import models
# https://stackoverflow.com/questions/33772947/django-set-range-for-integer-model-field-as-constraint
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    SHOE_TYPE = [
        ('sneaker', 'Sneaker'),
        ('boot', 'Boot'),
        ('sandal', 'Sandal'),
        ('dress', 'Dress'),
        ('other', 'Other')
    ]
    style = models.CharField(max_length=200, choices=SHOE_TYPE)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    SHOE_COLORS = [
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('indigo', 'Indigo'),
        ('violet', 'Violet'),
        ('white', 'White'),
        ('black', 'Black')
    ]
    color_name = models.CharField(max_length=200, choices=SHOE_COLORS)

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.PositiveIntegerField(
        help_text="Max shoe size is 22",
        validators=[MaxValueValidator(1), MinValueValidator(22)]
    )
    brand = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=200)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=200)
