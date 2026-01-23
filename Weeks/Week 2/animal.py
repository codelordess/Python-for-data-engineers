class Animal:
    def __init__(self):
        print("Initializing Animal Constructor")
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic animal sound"

    def eat(self):
        return f"{self.name} is eating."


class Mammal(Animal):


    def make_sound(self):
        return "Some generic mammal sound"

    def nurse_young(self):
        return f"{self.name} is nursing its young."
    
    def walk(self):
        return f"{self.name} is walking on four legs."
        print("Mammal walk method called")  
