class Person:
    '~~it is a very basic excercise~~'
    count_dudes = 0
    dudes = []

    def __init__(self, name):
        self.name = name
        Person.count_dudes += 1
        Person.dudes.append(name)

    def display_count(self):
        print("The total number of instances (dudes): %d" % Person.count_dudes)

    def display_dude_name(self):
        print("Name: " + self.name)

    def display_dudes(self):
        print(self.dudes)

    def say_hello(self):
        print("Hello, my name is " + self.name)

print(Person.__doc__)
dude1 = Person("Newbie")
dude2 = Person("Oldie")

dude1.display_count()
dude1.display_dude_name()
dude1.display_dudes()

dude2.say_hello()
print("let's see some built-in classes")
print("Person.__name__:", Person.__name__)
print("Person.__module__:", Person.__module__)
print("Person.__bases__:", Person.__bases__)
# print("Person.__dict__:", Person.__dict__)
