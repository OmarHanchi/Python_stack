class Pet : 
    def __init__(self,type,name,tricks,health=100) :
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100 
    def sleep (self) :
        self.enegy += 25
        print(f"after sleeping your {self.type} {self.name} energy is {self.energy}")
    def eat (self ) : 
        self.energy += 5 
        self.health += 10
        print(f"after eating your {self.type} {self.name} energy is {self.energy} and his health is {self.health}")
    def play (self) : 
        self.health += 5
        print(f"after playing your {self.type} {self.name} health is {self.health}")
    def noise ( self) : 
        print (f"your {self.type} {self.name}  {self.tricks} ")
# Subclass Dog
class Dog(Pet):
    """This is a subclass of Pet that represents a dog."""

    def __init__(self, name, tricks):
        """Initialize the dog's attributes."""
        super().__init__(name, "Dog", tricks)
        self.breed = "Unknown"

    def bark(self):
        """Prints a message that the dog is barking."""
        print(f"{self.name} barks loudly!")


# Subclass Cat
class Cat(Pet):
    """This is a subclass of Pet that represents a cat."""
    def __init__(self, name, tricks):
        """Initialize the cat's attributes."""
        super().__init__(name, "Cat", tricks)
        self.color = "Unknown"
    def purr(self):
        """Prints a message that the cat is purring."""
        print(f"{self.name} purrs softly.")
