from django.db import models


class Currency(models.Model):
    name = models.CharField(verbose_name='Currency name', max_length=100, unique=True)
    rate = models.FloatField(verbose_name='Currency rate to Rouble')

    def __repr__(self):
        return f'{self.name}: {self.rate} Roubles'

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'currency'
        verbose_name_plural = 'Currencies'