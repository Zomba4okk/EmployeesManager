from django.db import models


class Computer(models.Model):
    PC = 'PC'
    LAPTOP = 'LAPTOP'

    TYPE_CHOICES = (
        (PC, 'PC'),
        (LAPTOP, 'LAPTOP')
    )

    model = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    purchase_date = models.DateField(null=False)

    def __str__(self):
        return self.model