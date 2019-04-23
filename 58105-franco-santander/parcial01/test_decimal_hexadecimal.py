""" ESTE MODULO SIRVE PARA TESTEAR QUE LA CONVERSION A DE NUMEROS DECIMALES A NUMEROS HEXADECIMALES 
ESTE BIEN """

import unittest
from decimal_hexadecimal import hexad_to_decimal


class TestDecimalNumbers(unittest.TestCase):
     def test_decimal_1_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(1)
        self.assertEqual(hexad_number,'001')
     def test_decimal_2_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(2)
        self.assertEqual(hexad_number,'002')
     def test_decimal_3_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(3)
        self.assertEqual(hexad_number,'003')
     def test_decimal_4_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(4)
        self.assertEqual(hexad_number,'004')
     def test_decimal_5_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(5)
        self.assertEqual(hexad_number,'005')
     def test_decimal_6_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(6)
        self.assertEqual(hexad_number,'006')
     def test_decimal_7_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(7)
        self.assertEqual(hexad_number,'007')
     def test_decimal_8_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(8)
        self.assertEqual(hexad_number,'008')
     def test_decimal_9_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(9)
        self.assertEqual(hexad_number,'009')
     def test_decimal_10_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(10)
        self.assertEqual(hexad_number,'00A')
     def test_decimal_11_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(11)
        self.assertEqual(hexad_number,'00B')
     def test_decimal_12_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(12)
        self.assertEqual(hexad_number,'00C')
     def test_decimal_13_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(13)
        self.assertEqual(hexad_number,'00D')
     def test_decimal_14_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(14)
        self.assertEqual(hexad_number,'00E')
     def test_decimal_15_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(15)
        self.assertEqual(hexad_number,'00F')
     def test_decimal_017_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(17)
        self.assertEqual(hexad_number,'011')
     def test_decimal_016_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(16)
        self.assertEqual(hexad_number,'010')
     def test_decimal_4095_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(4095)
        self.assertEqual(hexad_number,'FFF')
     def test_decimal_1234_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(1234)
        self.assertEqual(hexad_number,'4D2')
     def test_decimal_234_to_hexadecimal_(self):
        hexad_number = hexad_to_decimal(234)
        self.assertEqual(hexad_number,'0EA')
     
if __name__ == '__main__':
    unittest.main()