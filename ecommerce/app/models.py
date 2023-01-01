from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('spotwear','spotwear'),
    ('shirt','shirt'),
    ('outwear','outwear'),  
)
condition_choices=(
    ('new','new'),
    ('Used','Used'),
    ('Fresh','Fresh'),  
)

class Product(models.Model):
    title = models.CharField(max_length=100,null=True)
    condition = models.CharField(choices=condition_choices, max_length=20,null=True)
    details = models.TextField(null=True)
    description = models.TextField(null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20,null=True)
    selling_price = models.FloatField(null=True)
    discounted_price = models.FloatField(null=True)
    brand = models.CharField(max_length=100,null=True)
    product_image = models.ImageField(upload_to='static/img/product',null=True)
    def __str__(self):
        return self.title
    