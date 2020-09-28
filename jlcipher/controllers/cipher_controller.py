from ..models.caesar_model import CaesarCipher
from ..models.vigenere_model import VigenereCipher


class CipherController:
    def __init__(self):
        #  The cipher variable holds the active cipher,
        #  which is translated by the translate() method.

        self.cipher = None

    def load(self, cipher_which, text, key):
        """
        Instantiates the appropriate cipher model
        and stores it in this class.
        """

        if cipher_which == 'Caesar':
            self.cipher = CaesarCipher(text=text, key=key, language="English")
        elif cipher_which == 'Vigenère':
            pass  # todo

    def translate(self, to_cipher=True):
        """
        Ciphers or deciphers the currently loaded
        cipher and returns the result.
        """

        if to_cipher:
            return self.cipher.cipher()
        return self.cipher.decipher()
