from string import printable
from .cipher_base_model import UnicodeCipher
from ..mixins import WithCustomShiftingTable


class CaesarCipher(UnicodeCipher, WithCustomShiftingTable):
    def __init__(self, text, key, language):
        try:
            self.__class__.validate_key(key)
        except(ValueError):
            raise RuntimeError("Bad key")

        UnicodeCipher.__init__(self, name="Caesar", text=text, key=key, language=language)  # noqa:E501
        WithCustomShiftingTable.__init__(self, self.supported_languages[language])  # noqa:E501

    @staticmethod
    def validate_key(k):
        if type(k) is not int:
            raise ValueError("Key must be integer.")

    def cipher(self):
        # Turn the text into a C-style char array
        chararr = list(self._text)

        for i in range(len(chararr)):

            # Check if it is printable
            ch = chararr[i]
            if ch not in printable:
                continue

            # Check if it is part of the language
            if not self.__class__.inlanguage(ch, self.language):
                continue

            # If uppercase: make it lowercase and flag it
            is_upper = False
            if ch.isupper():
                is_upper = True
                ch = ch.lower()

            p = self.pos_of[ch]  # Find the order in the custom table
            shift = (p + self.key) % self.letters  # Find new position within the custom table # noqa:E501
            c = self.char_of[shift]  # Determine which character it is according to the custom table # noqa:E501

            # If it was flagged, restore uppercase
            if is_upper:
                c = c.upper()

            chararr[i] = c

        return "".join(chararr)

    def decipher(self):
        # Turn the text into a C-style char array
        chararr = list(self._text)

        for i in range(len(chararr)):

            # Check if it is printable
            ch = chararr[i]
            if ch not in printable:
                continue

            # Check if it is part of the language
            if not self.__class__.inlanguage(ch, self.language):
                continue

            # If uppercase: make it lowercase and flag it
            is_upper = False
            if ch.isupper():
                is_upper = True
                ch = ch.lower()

            p = self.pos_of[ch]  # Find the order in the custom table
            shift = (p - self.key) % self.letters  # Find new position within the custom table # noqa:E501
            c = self.char_of[shift]  # Determine which character it is according to the custom table # noqa:E501

            # If it was flagged, restore uppercase
            if is_upper:
                c = c.upper()

            chararr[i] = c

        return "".join(chararr)
