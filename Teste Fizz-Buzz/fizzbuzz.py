class FizzBuzz:
    def answer(self, number):
        if not isinstance(number, int):
            raise TypeError("O valor deve ser um número inteiro.")

        if number <= 0:
            raise ValueError("O número deve ser maior que zero.")

        if number % 3 == 0 and number % 5 == 0:
            return "fizzbuzz"

        if number % 3 == 0:
            return "fizz"

        if number % 5 == 0:
            return "buzz"

        return str(number)