"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n
- метод generate, который принимает длину последовательности n
- метод print_seq, который выводит последовательность на экран
"""

import random


class RandSequence:
    sequence: list
    n: int

    def __init__(self, n):
        self.n = n

    def generate(self):
        for _ in range(self.n):
            self.sequence.append(random.randint(-10, 10))
            return self.sequence

    def print_seq(self):
        print(self.sequence)


print(random.uniform(-10, 10))