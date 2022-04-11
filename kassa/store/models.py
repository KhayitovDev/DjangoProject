from django.db import models

class Expenses(models.Model):
    TYPE=(
        ('KIRIM', 'KIRIM'),
        ('CHIQIM', 'CHIQIM'),
        ('DIVIDEND', 'DIVIDEND'),
        ('PERSONAL', 'PERSONAL'),

    )
    objects = models.Manager()
    typee = models.CharField(max_length=100, blank=True, null=True, choices=TYPE)
    byWho = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField()
    valuta = models.CharField(max_length=100, blank=True, null=True)
    Kurs = models.IntegerField()
    summa = models.IntegerField()
    category = models.CharField(max_length=100, blank=True, null=True)
    izoh = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.typee
