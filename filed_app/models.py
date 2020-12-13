from django.db import models

# Create your models here.
class Details(models.Model):
    CreditCardNumber = models.CharField(max_length=16,null=False)
    CardHolder = models.CharField(max_length=50,null=False)
    ExpirationDate = models.DateField(null= False)
    SecurityCode = models.CharField(max_length=3)
    Amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.CardHolder)