# Classes

#Creating a class
class Dog:

    animal_kind = "canine" # class variable

    def bark(self): # class function = methods
        print(self.animal_kind)
        return "woof"

print(Dog.animal_kind)
print(Dog.bark(Dog))

# Instantiation of a class

# creating the dog from the above blueprint

kipo = Dog() # the () tell Python it's an object, not a variable
mr_benedict = Dog()

print(type(kipo)) # <class '__main__.Dog'>
print(mr_benedict.animal_kind)
print(kipo.bark()) # we don't need to include self here since python is already aware Kipo and Mr_Ben are of the Dog class

# You can overwrite cass attribute per instantiation of each object.
kipo.animal_kind = "Black Dog"
print(kipo.animal_kind) # Black Dog
print(mr_benedict.animal_kind) # canine

# Be careful of class variables

Dog.animal_kind = "Dolphin"
print(mr_benedict.animal_kind)
print(mr_benedict.bark())
# mr_ben is now a dolphin but still barks woof