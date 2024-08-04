import re

class StringScore:
    value: str = ''
    score: int = 0

    def __init__(self, value, score):
        self.value = value
        self.score = score

    def __str__(self):
        return self.value + ' [' + str(self.score) + ']'

    def __repr__(self):
        return self.value + ' [' + str(self.score) + ']'
    
class Word:
    value: str = ''
    depth: int = 0
    index: int = 0
    isLeaf: bool

    def __init__(self, value: str, depth: int, index: int, isLeaf: bool):
        self.value = value
        self.depth = depth
        self.index = index
        self.isLeaf = isLeaf

class Item:
    chunks: list[str] = []
    words: list[Word] = []
    value: str = ''

    def __init__(self, value: str):
        if (not value):
            return
        self.value = value
        self.chunks = value.replace('\n', '').split(' / ')
        self.words = []
        for chunkIdx, chunk in enumerate(self.chunks):
            wordStrs = re.sub('[^A-Za-z -]', '', chunk).lower().split(' ')
            for wordIdx, wordStr in enumerate(wordStrs):
                word = Word(wordStr, chunkIdx, wordIdx, chunkIdx == (len(self.chunks) - 1))
                self.words.append(word)

    def __str__(self):
        return ' / '.join(chunk for chunk in self.chunks)

    def __repr__(self):
        return ' / '.join(chunk for chunk in self.chunks)
    
class ItemScore:
    item: Item = None
    score: int = 0

    def __init__(self, item: Item, score: int):
        self.item = item
        self.score = score

    def __str__(self):
        return str(self.item) + ' [' + str(self.score) + ']'

    def __repr__(self):
        return str(self.item) + ' [' + str(self.score) + ']'