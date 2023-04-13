from django.db import models

# Create your models here.

class FeriadoModel(models.Model):
 nome = models.CharField('Feriado',max_length=50)
 dia = models.DateField('Data')