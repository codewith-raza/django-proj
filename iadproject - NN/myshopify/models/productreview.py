from django.db import models
from .product import Product
from .customer import Customer
from django.utils.timezone import now
class Productreview(models.Model):
    sno=models.AutoField(primary_key=True)
    review=models.TextField()
    product=models.ForeignKey(Product,
                                 on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,
                                  on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.review[0:13]+"....."+"by" + self.customer.first_name
