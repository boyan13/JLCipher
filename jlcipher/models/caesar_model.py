from .cipher_base_model import Cipher


class CaesarCipher(Cipher):
    __slots__ = []

    def __init__(self, text, key):
        self.__class__.validate_key(key)
        super().__init__("Caesar", text, key)

    @staticmethod
    def validate_key(k):
        if type(k) is not int:
            raise ValueError("Key must be integer.")

    def cipher(self):
        pass

    def decipher(self):
        pass
