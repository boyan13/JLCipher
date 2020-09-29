from string import printable
from .cipher_base_model import UnicodeCipher
from ..mixins import WithCustomShiftingTable


class VigenereCipher(UnicodeCipher, WithCustomShiftingTable):
    def __init__(self, text, key, language):
        try:
            self.__class__.validate_key(key, language)
        except(ValueError):
            raise RuntimeError("Bad key")

        UnicodeCipher.__init__(self, name='Vigenère', text=text, key=key, language=language)  # noqa:E501
        WithCustomShiftingTable.__init__(self, self.supported_languages[language])  # noqa:E501
        self.keyseq = self.parse_key()
        self.keylen = len(self.keyseq)

    @classmethod
    def validate_key(cls, k, language):
        if type(k) is not str:
            raise ValueError("Key must be a of type str.")
        for c in k:
            if not cls.inlanguage(ch=c, lang_str=language):
                raise ValueError("Key does not belong to \
                the specified language.")

    def parse_key(self):
        '''
        Translate the sequence of characters that is the key into
        a sequence of shifts corresponding with the custom shifting table.
        '''
        keyarr = list(self.key)
        shifts = []
        for k in keyarr:
            shifts.append(self.pos_of[k])
        return shifts

    def cipher(self, ignore_punctuation=True, alphabets=None):
        # Turn the text into a C-style char array
        chararr = list(self._text)
        j = 0

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
            shift = (p + self.keyseq[j]) % self.letters  # Find new position within the custom table # noqa:E501
            c = self.char_of[shift]  # Determine which character it is according to the custom table # noqa:E501

            # If it was flagged, restore uppercase
            if is_upper:
                c = c.upper()

            chararr[i] = c

            # Next key in the sequence
            if j == self.keylen - 1:
                j = 0
            else:
                j += 1

        return "".join(chararr)

    def decipher(self, ignore_punctuation=True, alphabets=None):
        # Turn the text into a C-style char array
        chararr = list(self._text)
        j = 0

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
            shift = (p - self.keyseq[j]) % self.letters  # Find new position within the custom table # noqa:E501
            c = self.char_of[shift]  # Determine which character it is according to the custom table # noqa:E501

            # If it was flagged, restore uppercase
            if is_upper:
                c = c.upper()

            chararr[i] = c

            # Next key in the sequence
            if j == self.keylen - 1:
                j = 0
            else:
                j += 1

        return "".join(chararr)
