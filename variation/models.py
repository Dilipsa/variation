from django.db import models
from multiselectfield import MultiSelectField


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


category = Category.objects.all().values_list('category', 'category')
try:
    choice_list = []
    for item in category:
        choice_list.append(item)
except:
    pass


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img')
    # product_category = models.CharField(max_length=255)
    product_category = MultiSelectField(choices=choice_list, blank=True, null=True)

    def __str__(self):
        return self.name
