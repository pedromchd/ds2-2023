import unittest
from carro import Carro

class TestCarro(unittest.TestCase):
    def setUp(self):
        self.carro = Carro('Versa', 'Nissan', 2019)

    def tearDown(self):
        self.carro = None

    def teste_modelo(self):
        self.assertEqual(self.carro.modelo, 'Versa')    
        
    @unittest.skip
    def test_ano(self):
        self.assertEqual(self.carro.ano, 2019)

