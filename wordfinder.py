"""Word Finder: finds random words from a dictionary."""
#from random import randint
import random

class WordFinder:
    """Read words from a given file and pick a random word.

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True
    """

    def __init__(self, path):
        """Read words from a given file and print # of words read"""
        dict_file = open(path)
        self.words = self.readFile(dict_file)
        print(f"{len(self.words)} words read") 

    def readFile(self, dict_file):
        """Read words from a file and remove whitespace"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return a random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Read words from a file that has blank line and '#' line, 
       pick a random word without space or '#'

    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    
    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    """

    def readFile(self, dict_file):
        """Read words from a file"""
        return [w.strip() for w in dict_file if w.strip() and (not w.startswith('#'))]
