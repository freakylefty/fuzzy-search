import re
from src.model import StringScore, Item, ItemScore
from src.score import Score
from src.logger import Logger

class Search:

    items: list[Item]

    def __init__(self, items: list[Item]):
        self.items = items

    def getScore(self, item: Item, strValue: str) -> StringScore:
        """
        Searches all instances of the given substring in all words and returns the one with the best score.
    
        Words are guaranteed to be present, but there are not necessarily any string matches, in which
        case a score of 0 will be returned.  The same is true if the search term is empty.
        """
        bestScore: StringScore = StringScore(strValue, 0)        
        for word in item.words:
            indexes = [m.start() for m in re.finditer(strValue, word.value)]
            for index in indexes:
                currScore = Score.getWordScore(word, index, strValue)
                if (bestScore.score < currScore):
                    bestScore = StringScore(strValue, currScore)

        return bestScore
    
    def strMatch(self, item, searchTerm) -> StringScore:
        """
        Iteratively gets the best score for the given search term.

        - Starts with the first character, gets the best score of all possible matches in the item's words.
        - If a match is found, try again with the first two characters.
        - Continue until either no match is found or the
        latest match has a lower score than the previous.
        - Return the best match.
        """
        currScore: StringScore = StringScore(searchTerm[0:1], 0)
        currLen: int = 0
        while True:
            currLen += 1
            subStr: str = searchTerm[0:currLen]
            newScore: StringScore = self.getScore(item, subStr)
            Logger.log('>> ' + str(newScore) + ' (newScore) ' + str(currScore) + ' (currScore)')
            if (newScore.score <= currScore.score):
                break
            currScore = newScore
            if (currLen == len(searchTerm)):
                break
        return currScore

    def match(self, item, searchTerm) -> ItemScore:
        """
        Get score for the current item with the given search string

        Works iteratively:
        - Gets the score for the whole search term, which will return a substring with a value
        - If score is 0, remove the first character from the search term and loop
        - If the score is non-zero, add to the running total, remove the associated substring 
          from the search term, and loop
        - Once the search string is exhausted, return the running total
        """
        Logger.log('Getting best score for ' + str(item))
        score: ItemScore = ItemScore(item, 0)
        remainingText = searchTerm
        numZeroes = 0
        while True:
            nextScore = self.strMatch(item, remainingText)
            Logger.log('> ' + str(nextScore))
            # Add next score to running total, even if it's 0
            score.score += nextScore.score
            if (nextScore.score == 0):
                numZeroes += 1

            if (remainingText == nextScore.value):
                # No text left, break out of the loop
                break
            remainingText = remainingText[len(nextScore.value):]

        Logger.log('Best score: ' + str(score))
        Logger.log('Unused characters: ' + str(numZeroes))
        if (numZeroes > 0):
            score.score = Score.adjustForUnusedChars(score.score, numZeroes)
            Logger.log('Score adjusted for unused characters: ' + str(score))
        return score

    def search(self, text: str) -> Item | None:
        """
        Iterates through each item in the list and gets the score for each for the search term.

        Stores the best and returns it at the end.
        """
        Logger.log('\nSearching\n')
        best: ItemScore = None
        for item in self.items:
            result = self.match(item, text.lower())
            if (result != None and (best == None or result.score > best.score)):
                best = result
        if (best != None):
            Logger.log(str(best))
        return best.item if best != None else best