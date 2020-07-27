from .cipher_base_model import Cipher


class VigenereCipher(Cipher):
    __slots__ = []

    def __init__(self, text, key):
        self.__class__.validate_key(key)
        super().__init__('Vigenère', text, key)

    @staticmethod
    def validate_key(k):
        if type(k) is not str:
            raise ValueError("Key must be a of type str.")

    def cipher(self):
        pass

    def decipher(self):
        pass
