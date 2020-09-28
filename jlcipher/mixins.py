class WithCustomShiftingTable:
    '''
    Grabs a set of characters and arranges them in an array next to each other.
    Used for shifting characters in isolation, independently of their position
    in unicdoe. Ignores uppercase.
    (For example A-Z, skipping B makes 24 letters total.
    and shiftin with key 1 then gives: A + 1 = C)
    '''
    def __init__(self, language):
        '''
        Create the shifting table.
        Add attributes:
        (dict) table: the shifting table(array), where
        key is the position (used for shifting) and value is the character
        (int) letters: total amount of charactes in the table

        Args:
        (iterable) language: An iterable of iterables, where each inner
        iterable is either a pair of 2 hexadecimal values representing
        a range of unicode characters or just a single one (to be included
        alone).
        '''

        p, c = self._make_table(language)

        self.pos_of = p  # use character as key to find its position
        self.char_of = c  # use position as key to find the corresponding character # noqa: E501
        self.letters = len(p)

    def _make_table(self, language):
        '''
        Create the shifting table.
        Gets a language and parses it into 2 dicts which make up the table.
        One dict to find the position of a character in the new table.
        Another dict to find the character corresponding to a position in
        the new table.

        Args:
        (iterable) language: An iterable of iterables, where each inner
        iterable is either a pair of 2 hexadecimal values representing
        a range of unicode characters or just a single one (to be included
        alone).
        '''

        li = []

        # Collect all characters in the specified
        # ranges into a list.
        for it in language:
            if len(it) == 1:
                li += it[0]
            elif len(it) == 2:
                g = self._extract_range(it[0], it[1])
                li += g

        # Remove uppercase
        li = [m for m in li if not m.isupper()]

        # Create the table dicts
        pos_of = {}
        char_of = {}
        for i in range(len(li)):
            char_of[i] = li[i]
            pos_of[li[i]] = i

        return (pos_of, char_of)

    def _extract_range(self, left, right):
        for i in range(left, right+1):
            yield chr(i)
        return
