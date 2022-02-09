from django.db import models

class Sales(models.Model):
    """A bare minimum example"""
    date = models.DateField()
    product = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.date}: {self.product} ({self.count})'