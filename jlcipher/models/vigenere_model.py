from .cipher_base_model import UnicodeCipher


class VigenereCipher(UnicodeCipher):
    def __init__(self, text, key, languages):
        self.__class__.validate_key(key)
        super().__init__(name='Vigenère', text=text, key=key, language=languages)  # noqa:E501

    @staticmethod
    def validate_key(k):
        if type(k) is not str:
            raise ValueError("Key must be a of type str.")

    def cipher(self, ignore_punctuation=True, alphabets=None):
        pass

    def decipher(self, ignore_punctuation=True, alphabets=None):
        pass
