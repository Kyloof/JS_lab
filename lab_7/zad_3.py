from string import ascii_letters, digits
from random import randint

class PasswordGenerator:

    def __init__(self, length, count, charset = ascii_letters + digits):
        self.length = length
        self.count = count
        self.charset = charset

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        self.count -= 1
        result = ''

        l = len(self.charset) - 1

        for i in range(self.length):
            result += self.charset[randint(0,l)]

        return result