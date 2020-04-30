import random


class Meme:
    def __init__(self, spread):
        self.spread = spread

    def mutate(self):
        if 1 >= random.randint(0, 100):
            mutated_spread = self.spread + random.randint(0, 10) - 5
            if mutated_spread > 250:
                mutated_spread = 250
            if mutated_spread < 1:
                mutated_spread = 1
            return Meme(mutated_spread)
        else:
            return self

    def color(self):
        return (self.spread, 255 - self.spread, self.spread)
