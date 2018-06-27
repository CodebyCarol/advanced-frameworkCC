class Person:
    'it is a very basic excercise'
    
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


dude1 = Person("Newbie")
dude2 = Person("Oldie")

dude1.display_count()
dude1.display_dude_name()
dude1.display_dudes()
    # def say_hello(self):
    #     print("Hello, my name is " + self.name)

