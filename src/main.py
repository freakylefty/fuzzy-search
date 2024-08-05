from search.loader import Loader
from search.model import Item
from search.matcher import Matcher

manager = Matcher(Loader.getItems('data/sections.txt'))

loop = True
while loop:
    searchTerm = input("Search: ")
    if (searchTerm != ''):
        result: Item = manager.getBestMatch(searchTerm)
        print(result)
    else:
        loop = False