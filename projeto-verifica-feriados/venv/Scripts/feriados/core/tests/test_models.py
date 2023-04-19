from django.test import TestCase

from core.models import feriadoModel
from datetime import date

class FeriadoModelTest(TestCase):
 def setUp(self):
    self.cadastro = FeriadoModel(
    nome='hoje',
    dia=date.today())
    self.cadastro.save()