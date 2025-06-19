from django.db.models import Model, CharField, URLField, DecimalField, TextChoices, TextField, IntegerField, \
    BooleanField


class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=0)
    quantity = IntegerField()
    total_price = DecimalField(max_digits=10, decimal_places=2)
    remove = BooleanField(default=False)
    icon = URLField()

class Order(Model):




