from src.model import Item

class Loader:
    @staticmethod
    def getItems(filename: str) -> list[Item]:
        items = []
        with open(filename) as file:
            lines = file.readlines()
        for line in lines:
            curr = Item(line)
            if (len(curr.words) > 0):
                items.append(Item(line))
        return items