class CipherController:
    def __init__(self, cipher_or_decipher, cipher_which, key):
        self.cipher = cipher_or_decipher
        self.cipher_which = cipher_which
        self.key = key

    def set_operation(self, cipher_or_decipher):
        if cipher_or_decipher == 1:
            self.cipher = True  # Cipher
        else:
            self.cipher = False  # Decipher

    def set_cipher(self, cipher_which):
        if cipher_which == 'Caesar':
            self.cipher_which = 'Caesar'
        elif cipher_which == 'Vigenère':
            self.cipher_which = 'Vigenère'

    def set_key(self, key):
        self.key = key

    def translate(self, text):
        output = str()

        if self.cipher_which == 'Caesar':
            if self.cipher:
                output = self.translate_caesar(text)
            else:
                output = self.translate_caesar(text, False)

        elif self.cipher_which == 'Vigenère':
            if self.cipher:
                output = self.translate_vigenere(text)
            else:
                output = self.translate_vigenere(text, False)

        return output

    def translate_caesar(self, text, to_cipher=True):
        print("IN FUNCTION: CAESAR")
        print("RECEIVED:", self.cipher, self.cipher_which, self.key)
        print(text)

    def translate_vigenere(self, text, to_cipher=True):
        print("IN FUNCTION: VIGENERE")
        print("RECEIVED:", self.cipher, self.cipher_which, self.key)
        print(text)
