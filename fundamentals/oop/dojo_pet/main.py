from pet import Pet 
from ninja import Ninja 
# Create a pet instance
dog= Pet("dog","Spike",["Sit", "barking", "Roll Over"]) 
cat= Pet("cat","Tom",["Sit", "Meowing", "Fetch"])
treats = ["snausage","bacon"]
pet_food =["pizza","burger",]
# Create a Ninja instance
omar=Ninja("Omar","Hanchi",dog,treats,pet_food)
omar.feed()
omar.bathe()
omar.walk()