from django.test import TestCase

from ..models import Pessoa

# Create your tests here.


class PessoaTestCase(TestCase):

    def setUp(self):
        Pessoa.objects.create(
            nome="Fulano de tal",
            idade=38
        )

    def test_retorno_str(self):
        p1 = Pessoa.objects.get(nome='Fulano de tal')
        self.assertEquals(p1.__str__(), 'Fulano de tal')
