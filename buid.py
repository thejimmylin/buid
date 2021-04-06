import random


class BUID:
    VOWEL = 'V'
    CONSONAT = 'C'
    SEPARATOR = '-'
    VOWEL_CHARS = 'aeiou'
    CONSONAT_CHARS = 'bcdfghjklmnpqrstvwxyz'
    SEPARATOR_CHARS = '-'

    def __init__(
        self, phrases=None, format='CVCV-CVCV-CVCV-CVCV', VOWEL=None, CONSONAT=None,
        SEPARATOR=None, VOWEL_CHARS=None, CONSONAT_CHARS=None, SEPARATOR_CHARS=None,
    ):
        if not format:
            raise ValueError("The format can't be empty.")
        self.VOWEL_CHARS = VOWEL_CHARS if VOWEL_CHARS else self.VOWEL_CHARS
        self.CONSONAT_CHARS = CONSONAT_CHARS if CONSONAT_CHARS else self.CONSONAT_CHARS
        self.SEPARATOR_CHARS = SEPARATOR_CHARS if SEPARATOR_CHARS else self.SEPARATOR_CHARS
        self.format = format
        self.phrases = self.get_phrases(phrases=phrases, format=self.format)
        if len(self.phrases) != len(self.format):
            raise ValueError('The lengths of the given phrases and format do not match.')
        for f, p in zip(self.format, self.phrases):
            if f == self.VOWEL:
                assert p in self.VOWEL_CHARS, ValueError(f'{p} is not a vowel character.')
            elif f == self.CONSONAT:
                assert p in self.CONSONAT_CHARS, ValueError(f'{p} is not a consonat character.')
            elif f == self.SEPARATOR:
                assert p in self.SEPARATOR_CHARS, ValueError(f'{p} is not a separator character.')
            else:
                raise ValueError(f'{f} is not a known format character.')

    def get_phrases(self, phrases, format):
        if phrases:
            return phrases
        phrases = ''
        for f in format:
            if f == self.VOWEL:
                phrases += random.choice(self.VOWEL_CHARS)
            elif f == self.CONSONAT:
                phrases += random.choice(self.CONSONAT_CHARS)
            elif f == self.SEPARATOR:
                phrases += random.choice(self.SEPARATOR_CHARS)
            else:
                raise ValueError(f'{f} is not a known format character.')
        return phrases

    def __str__(self):
        return self.phrases

    def __repr__(self):
        return f"{self.__class__.__name__}({self.phrases.__repr__()}, {self.format.__repr__()})"
