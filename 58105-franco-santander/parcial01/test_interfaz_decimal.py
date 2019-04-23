"""ESTE MODULO SIRVE PARA LOS NUMEROS INGRESADOS NO SEAN LETRAS"""
import unittest
from decimal_hexadecimal import hexad_to_decimal


class TestInterfaz(unittest.TestCase):
     def test_decimal_hola_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal('hola')
        self.assertEqual(result, 'Disculpe, solo acepto numeros')
if __name__ == '__main__':
    unittest.main()