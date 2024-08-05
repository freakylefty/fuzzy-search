import unittest

from search.model import Item
from search.matcher import Matcher

class TestSearch(unittest.TestCase):

    def test_getBestMatch(self):
        items = [Item('Title / Subtitle'), Item('Section / Subsection')]
        manager = Matcher(items)
        self.assertEqual(manager.getBestMatch('section'), items[1])
        self.assertEqual(manager.getBestMatch('title'), items[0])

        items = [
            Item('More Control Flow Tools / break and continue Statements, and else Clauses on Loops'),
            Item('Classes / A Word About Names and Objects')
            ]
        manager = Matcher(items)
        self.assertEqual(manager.getBestMatch('loocla'), items[0])

        items = [
            Item('Brief Tour of the Standard Library'),
            Item('Brief Tour of the Standard Library - Part II'),
            Item('Brief Tour of the Standard Library - Part II / Templating')
            ]
        manager = Matcher(items)
        self.assertEqual(manager.getBestMatch('brieftem'), items[2])

    def test_getScore(self):
        manager = Matcher([])
        item = Item('Title / Subsection')
        self.assertEqual(manager.getScore(item, 'ti').value, 'ti')
        self.assertEqual(manager.getScore(item, 'ti').score, 26)
        self.assertEqual(manager.getScore(item, 'tit').value, 'tit')
        self.assertEqual(manager.getScore(item, 'tle').score, 24)
        self.assertEqual(manager.getScore(item, 'x').value, 'x')
        self.assertEqual(manager.getScore(item, 'x').score, 0)

    def test_strMatch(self):
        manager = Matcher([])
        item = Item('More Control Flow Tools / break and continue Statements, and else Clauses on Loops')
        self.assertEqual(manager.strMatch(item, 'loocla').score, 72)
        item = Item('Classes / A Word About Names and Objects')
        self.assertEqual(manager.strMatch(item, 'loocla').score, 1)
