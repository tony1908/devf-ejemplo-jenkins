from ejemplo import *
import unittest

class TestEjemplo(unittest.TestCase):

	def setUp(self):
		self.ejemplo = Ejemplo("Tony")

	def test_obteter_nombre(self):
		self.assertEqual(self.ejemplo.obtenerNombre(), "Tony")

if __name__ == '__main__':
    unittest.main()
