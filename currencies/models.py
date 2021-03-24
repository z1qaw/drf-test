from django.db import models


class Currency(models.Model):
    name = models.CharField(verbose_name='Currency name', max_length=100)
    rate = models.FloatField(verbose_name='Currency rate to Rouble')

    class Meta:
        db_table = 'currency'