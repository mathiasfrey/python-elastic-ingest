from django.db import models

class Sales(models.Model):
    """A bare minimum example"""
    date = models.DateField()
    product = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.date}: {self.product} ({self.count})'


class Entity(models.Model):
    name = models.CharField(max_length=32)
    
    class Meta:
        verbose_name_plural = 'entities'

    def __str__(self):
        return f'{self.name}'

class Channel(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'    

class SalesPerformance(models.Model):
    # time
    date = models.DateField()

    # dimensions
    entity = models.ForeignKey(to=Entity, blank=False, on_delete=models.CASCADE)
    channel = models.ForeignKey(to=Channel, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, blank=False, on_delete=models.CASCADE)

    # metrics
    contracts = models.IntegerField()
    volume = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'entity', 'channel', 'product'],
                name='unique entity/channel/product per date')
        ]
    
    def __str__(self):
        return f'{self.entity} {self.date}: {self.product}@{self.channel} ({self.contracts}/{self.volume})'