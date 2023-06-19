# OOP - Object Oriented Programming

OOP is turning code into objects that can be manipulated.

## Classes

Classes are a way of bringing data and functionality together. Like bringing in variables and ways to use those variables into the same object.

A class is like a blueprint or a template. You can create a class using the *class* keyword.

```commandline
class Dog:

    animal_kind = "canine"

    def bark(self):
        return "woof"
```
*animal_kind* is a **class variable**. Because the variable is in a class, it changes the scope of where the variable can be used and where it can be accessed. 

*def bark(self)* is a **class function**, or **method**.

*self* refers to the current class. 