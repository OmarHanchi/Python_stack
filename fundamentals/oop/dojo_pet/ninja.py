from pet import Pet
class Ninja :
    def __init__(self ,first_name,last_name,pet,treats,pet_food) :
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet = pet 
        self.pet_food = pet_food
    #adding walk function
    def walk (self):
        print(f"{self.first_name} is walking {self.pet.name}")
        self.pet.play()
    #adding feed function 
    def feed (self) :
        print(f"{self.first_name} is feeding {self.pet.name}")
        self.pet.eat()
    #adding bathe function 
    def bathe (self):
        print(f"{self.first_name} is bathing {self.pet.name}")
        self.pet.noise()
