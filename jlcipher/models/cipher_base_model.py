from collections.abc import Iterable
from abc import ABC, abstractmethod


class UnicodeCipher(ABC):
    """
    Base class for ciphers.

    Args:
        (string) name = the cipher's name
        (string) _text = the message
        (?) key = the cipher's key, can be anything,
        depending on the inheriting class
        (string) language = the name of the language
    """

    # Used Unicode Range: 0000-E007F (0 - 917631)

    supported_languages = {
        # (string) Key: language name
        # (tuple) Value: Tuple of tuples, where each inner
        # tuple is either a pair of 2 hexadecimal values representing
        # a range of unicode characters or just a single one
        #
        # Together, these ranges cover all letters belonging to a
        # certain alphabet
        "English": ((0x0041, 0x005A), (0x0061, 0x007A)),
        "Bulgarian": ((0x0410, 0x042A), (0x042E, 0x044A), (0x044E, 0x044F))
    }

    def __init__(self, name, text, key, language=None):
        self.__class__.validate_language(language)
        self.name = name
        self._text = text
        self.key = key
        self.language = language

    @abstractmethod
    def cipher(self):
        return

    @abstractmethod
    def decipher(self):
        return

    def inlanguage(self, ch):
        '''
        Checks if the given character is part
        of the selected language (self.language).
        '''

        o = ord(ch)
        l = self.__class__.supported_languages[self.language]  # noqa:E741

        for t in l:
            if len(t) == 1:
                if o == t[0]:
                    return True
            elif len(t) == 2:
                if o >= t[0] and o <= t[1]:
                    return True

        return False

    @classmethod
    def validate_language(cls, language):
        if language is not None:
            lang = cls.supported_languages[language]
            overlap = -1  # Check if ranges overlap
            if not isinstance(lang, Iterable):
                raise TypeError("Received a non-iterale structure.")
            for it in lang:
                if not isinstance(it, Iterable):
                    raise TypeError("An inner structure of the language is not iterable.")  # noqa:E501
                if len(it) not in [1, 2]:
                    raise ValueError("An inner iterable with length != 1 or 2")
                if overlap > it[0]:
                    raise ValueError("Overlapping ranges in language.")
                overlap = it[0]
                if len(it) == 2:
                    if overlap > it[1]:
                        raise ValueError("Inverted range is language.")
                    overlap = it[1]
