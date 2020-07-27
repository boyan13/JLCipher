from abc import ABC, abstractmethod


class Cipher(ABC):
    __slots__ = ['name', '__text', 'key']

    def __init__(self, name, text, key):
        self.name = name
        self.__text = text
        self.key = key

    def get(self):
        return self.text

    @abstractmethod
    def cipher(self):
        return

    @abstractmethod
    def decipher(self):
        return
