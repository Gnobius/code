a = 12

class Person():
    def __init__(self, age=10, name="John"):
        super().__init__()
        self.age = age + a
        self.name = name

    def get_person_age(self):
        """Gets the age of the person"""
        return self.age

    def print_person_age(self):
        print(self.age)

my_person = Person()
my_person.print_person_age()

