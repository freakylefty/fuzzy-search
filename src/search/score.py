import math
from search.model import Word

class Score:

    SCORE_WORD_BREAK_START: int = 10
    SCORE_WORD_BREAK_END: int = 5
    SCORE_IS_LEAF: int = 10
    SCORE_DEPTH_WEIGHT: int = 1
    SCORE_LENGTH_WEIGHT: int = 1
    SCORE_LENGTH_MULTIPLIER: int = 1
    SCORED_ZERO_FACTOR: float = 0.9

    @staticmethod
    def adjustForUnusedChars(score: int, unusedChars: int) -> int:
        if (unusedChars == 0):
            return score
        return (int)(math.pow(0.9, unusedChars) * score)

    @staticmethod
    def getWordScore(word: Word, index: int, strValue: str) -> int:
        score = 0

        # Bonus for start of word
        if index == 0:
            score += Score.SCORE_WORD_BREAK_START

        # Bonus for end of word
        if (index + len(strValue)) == len(word.value):
            score += Score.SCORE_WORD_BREAK_END

        # Bonus if word is in final section
        if word.isLeaf:
            score += Score.SCORE_IS_LEAF
        
        # Bonus for word section depth
        score += (Score.SCORE_DEPTH_WEIGHT * word.depth)

        # Bonus for length of match
        score += (Score.SCORE_LENGTH_WEIGHT * len(strValue))

        # Multiply everything by length of match
        score *= (Score.SCORE_LENGTH_MULTIPLIER * len(strValue))
        
        return score