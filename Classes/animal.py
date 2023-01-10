class Animal:
    # constructor - defines the rules on how to create an instance of a class
    def __init__(self, name, eyes, ears, legs, tail, fur):
        # set the class instance variables
        self.name = name
        self.eyes = eyes
        self.ears = ears
        self.legs = legs
        self.tail = tail
        self.fur = fur

    # TODO: add other methods later
    def __repr__(self):
        return f"Name: {self.name}, Eyes: {self.eyes}, Ears: {self.ears}, Legs: {self.legs}, Tail: {self.tail}, Fur: {self.fur}"

    def eat(self, food):
        """Return a string with the food the animal eats"""
        return f"Eats {food}"


# How to inherit from another class:
class Person(Animal):
    def __init__(self, name, eyes, ears, legs, tail, fur, city):
        super().__init__(name, eyes, ears, legs, tail, fur)
        self.city = city

    def __repr__(self):
        # also call the parent's repr and add the missing attributes:
        return f"{super().__repr__()}, City: {self.city}"

    def eat(self, food, drink):
        # also call the parent's eat method and using the extra variable drink:
        return f"{super().eat(food)} and drinks {drink}"


if __name__ == "__main__":
    person_a = Person("Diego", 2, 2, 2, 0, "nothing", "Berlin")
    print(person_a)
    print(person_a.eat("pasta", "wine"))

    animal = Animal("wolf", 2, 2, 2, 1, "gray")
    print(animal)
    print(animal.eat("meat"))
