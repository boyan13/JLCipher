from ..models.caesar_model import CaesarCipher
from ..models.vigenere_model import VigenereCipher


class CipherController:
    def __init__(self):
        self.cipher = None

    def load(self, cipher_which, text, key):
        if cipher_which == 'Caesar':
            self.cipher = CaesarCipher(text, key)
        elif cipher_which == 'Vigenère':
            self.cipher = VigenereCipher(text, key)

    def translate(self, decipher=False):
        if decipher:
            return self.cipher.decipher()
        else:
            return self.cipher.cipher()
