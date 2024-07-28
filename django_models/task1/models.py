from django.db import models


# Create your models here.
class Buyer(models.Model):
      id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=120)
      balance = models.DecimalField(max_digits=10, decimal_places=2)
      age = models.IntegerField()

      def __str__(self) -> str:
            return self.name

class Games(models.Model):
      id = models.AutoField(primary_key=True)
      title = models.CharField(max_length=140)
      cost = models.DecimalField(max_digits=10, decimal_places=2)
      size = models.FloatField()
      description = models.TextField()
      age_limited = models.BooleanField(default=False)
      buyer = models.ManyToManyField(Buyer, related_name='buyer')

      def __str__(self) -> str:
            return self.name
