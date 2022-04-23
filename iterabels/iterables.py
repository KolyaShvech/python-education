
"""
Create container Sentence and iterator SentenceIterator for him.
"""


class SentenceIterator:
    """
    Create class SentenceIterator with parameters word and word_id (index word).
    """
    def __init__(self, words):
        self._words = words
        self.word_id = 0

    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(self._words)[item.start:item.stop:item.step]
        if not (0 <= item < len(self._words)):
            raise IndexError
        return self._words[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self.word_id < len(self._words):
            word = self._words[self.word_id]
            self.word_id += 1
            return word
        else:
            raise StopIteration


class Sentence:
    """
    Create class Sentence with parameters text and function _validate().
    Class have some attribute PUNCTUATION_SIGNS = '.', '!' and '?'
    """
    PUNCTUATION_SIGNS = {'.', '!', '?'}

    def __init__(self, text: str):
        self.text = text
        self._validate(text)

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def _validate(self, text):
        """
        Create method _validate. In this method doing the validity of the text,
        which only accepts string and which ends with PUNCTUATION_SIGNS = {'.', '!', '?'}.
        """
        if not isinstance(text, str):
            raise TypeError('Only string allows.')

        if text[-1] not in self.PUNCTUATION_SIGNS:
            raise ValueError('Sentence is not complete.')

    def _words(self):
        return (word for word in self.words)

    @property
    def words(self):
        """
        Create decorator Property for words, where text must be only letter or spaces.
        """
        return ''.join(char for char in self.text if char.isalpha() or char.isspace()).split()

    @property
    def other_chars(self):
        """
        Create decorator Property for words, where text must not only letter or spaces.
        """
        return [char for char in self.text if not char.isalpha() and not char.isspace()]


sentence = Sentence("Hello, my name is Nikolay! & your? My name Platon.")
print(sentence)
for w in sentence:
    print(w)
sent = SentenceIterator("Hello world!")
print(sent[:])
