from src.loader import Loader
from src.model import Item
from src.search import Search

manager = Search(Loader.getItems('data/sections.txt'))

while True:
    searchTerm = input("Search: ")
    result: Item = manager.search(searchTerm)
    print(result)