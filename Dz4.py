import random

class NumberEncryptor:
    def __init__(self, number):
        self.number = number
        self.operation = random.choice(['+', '-', '*', '/'])

    def encrypt(self):
        if self.operation == '+':
            return self.number + random.randint(1, 10)
        elif self.operation == '-':
            return self.number - random.randint(1, 10)
        elif self.operation == '*':
            return self.number * random.randint(1, 10)
        elif self.operation == '/':
            divisor = random.randint(1, 10)
            if divisor == 0:
                divisor = 1
            return self.number / divisor

    def decrypt(self):
        return f"Number: {self.number}, Operation: {self.operation}"


original_number = 42
encryptor = NumberEncryptor(original_number)
encrypted_result = encryptor.encrypt()
print(f"Зашифроване значення: {encrypted_result}")
decrypted_result = encryptor.decrypt()
print(f"Результат дешифрування: {decrypted_result}")
