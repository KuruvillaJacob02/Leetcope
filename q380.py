from random import choice
class RandomizedSet(object):

    def __init__(self):
        self.data = set()

    def insert(self, val):
        if val in self.data:
            return False
        self.data.add(val)
        return True

        
    def remove(self, val):
        if val in self.data:
            self.data.discard(val)
            return True
        return False
 
    def getRandom(self):
        return random.choice(tuple(self.data))
        
