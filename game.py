from random import randrange

class Pet:

    threshold_hunger = 10
    threshold_boredom = 10
    sounds = ['Mrrp']
    boredom_decrement = 3
    hunger_decrement = 2

    def __init__(self, name):
        self.name = name
        self.hunger = randrange(self.threshold_hunger)
        self.boredom = randrange(self.threshold_boredom)
        self.sounds = self.sounds[:] # creating a new listr of sounds with the same variable name though

    def clock_tick(self):
        self.hunger += 1
        self.boredom += 1

    def teach(self, new_word):
        self.sounds.append(new_word)
        self.reduce_boredom()

    def Hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def __str__(self):
        return "{} is {} Hungry and {} Moody".format(self.name, self.hunger, self.boredom)
