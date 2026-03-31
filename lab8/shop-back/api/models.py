from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255) # [cite: 21]

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=255) # [cite: 15]
    price = models.FloatField() # [cite: 16]
    description = models.TextField() # [cite: 17]
    count = models.IntegerField() # [cite: 18]
    is_active = models.BooleanField(default=True) # [cite: 19]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # 

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
            'category_id': self.category.id
        }