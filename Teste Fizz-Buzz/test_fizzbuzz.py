import unittest
from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fb = FizzBuzz()

    def test_numero_comum_retorna_o_proprio_numero(self):
        self.assertEqual("1", self.fb.answer(1))
        self.assertEqual("2", self.fb.answer(2))
        self.assertEqual("4", self.fb.answer(4))
        self.assertEqual("7", self.fb.answer(7))

    def test_multiplos_de_tres_retorna_fizz(self):
        self.assertEqual("fizz", self.fb.answer(3))
        self.assertEqual("fizz", self.fb.answer(6))
        self.assertEqual("fizz", self.fb.answer(9))
        self.assertEqual("fizz", self.fb.answer(12))

    def test_multiplos_de_cinco_retorna_buzz(self):
        self.assertEqual("buzz", self.fb.answer(5))
        self.assertEqual("buzz", self.fb.answer(10))
        self.assertEqual("buzz", self.fb.answer(20))

    def test_multiplos_de_tres_e_cinco_retorna_fizzbuzz(self):
        self.assertEqual("fizzbuzz", self.fb.answer(15))
        self.assertEqual("fizzbuzz", self.fb.answer(30))
        self.assertEqual("fizzbuzz", self.fb.answer(45))

    def test_zero_deve_lancar_erro(self):
        with self.assertRaises(ValueError):
            self.fb.answer(0)

    def test_numero_negativo_deve_lancar_erro(self):
        with self.assertRaises(ValueError):
            self.fb.answer(-3)

    def test_string_deve_lancar_erro(self):
        with self.assertRaises(TypeError):
            self.fb.answer("15")

    def test_float_deve_lancar_erro(self):
        with self.assertRaises(TypeError):
            self.fb.answer(3.5)

    def test_none_deve_lancar_erro(self):
        with self.assertRaises(TypeError):
            self.fb.answer(None)


if __name__ == "__main__":
    unittest.main()