
# implement __init__( name , type , tricks ):
# eat() - increases the pet's energy by 5 & health by 10
class Ninja:
#__init__(self, first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        # implement the following methods:
        #     # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self#?? why feels wrong?
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.make_noise()
        print("very wellllll")
class Pet:
    def __init__(self, name, type, tricks,health, energy, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = noise
        # implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 250
        print("its time to goooo")
        return self
    def eat(self):
        self.energy += 100
        print("i finished") #how much increases when used?
        return self 
    def make_noise(self):# noise() - prints out the pet's sound
        print(self.noise) 
    def play(self):
        self.health =+10
        return self
# play() - increases the pet's health by 5
Amorzinho = Pet("Amorzinho", "Dinossaur", "breaths under water for 50 minutes",1000, 1000, "singer opera")
Christopher = Ninja("Christpher", "lindo", 100, "lions", Amorzinho)

Amorzinho.sleep()
