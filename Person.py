class TooOldError(ValueError):
    pass

class Person:
    genre = ['Male', 'Female']
    def __init__(self, gender):
        self.title = "Person Class"
        self.gender = gender

    def __str__(self):
        return f"Here is a {self.gender} in the {self.title}"

    # No need to create an instance to call this kind of functions
    @classmethod
    def Male(cls,):
        return Person(Person.genre[0])

    @classmethod
    def Female(cls,) -> 'Person':
        return Person(Person.genre[1])

    # No need of an instance nor a parameter to call a static Method
    @staticmethod
    def someFunc():
        return "A class that creates Persons !"

# Omar = Person.Male()
# print(Omar)

# ------------- Inheritance

class Child(Person):
    def __init__(self, gender, age):
        super().__init__(gender)
        self.age = age

    def __str__(self):
        return f"Here is probably a child {self.gender} in the {self.title}"

    def checkAge(self):
        if self.age < 11:
            print("A little {}".format(self.gender))
        elif self.age < 18 and self.age >= 11:
            print("A big little {}".format(self.gender))
        else:
            print("Not a child ANYMORE !")

    @classmethod
    def Male(cls, age):
        if age > 18 :
            raise TooOldError(
                f"Too Old apparently to be a child !!! "
            )
        return cls(Person.genre[0], age)

try :
    Ted = Child.Male(19)
    print(Ted)
    Ted.checkAge()
except TooOldError as e:
    print(e)

