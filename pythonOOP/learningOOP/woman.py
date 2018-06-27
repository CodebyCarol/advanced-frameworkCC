# in Python you refer to the .py file where from you import class name!
# (because you dont have to give the same name to the class and to the file...)
from learn import Person 


class Woman(Person):
    'sublcass of the base Person class'
    def __init__(self, name):
        self.name = name
        print("Calling child (woman) constructor")

    def childMethod(self):
        print("Calling child method")    

woman1 = Woman("Sara")

woman1.childMethod()
woman1.display_count()
print("Woman.__bases__:  ", Woman.__bases__)
print("Woman.__module__:", Woman.__module__)

print(woman1.name + "also can call the parent class, so she can tell that already " +
                    (str)(woman1.count_dudes) + " instance has beencreated")


class Blondie(Woman):

    haircolor = "blonde"

    def __init__(self, name):
        self.name = name
        print("initialize Blondies")

    def blondie_method(self):
        print("method of the blondie class")

    def display_haircolor(self):
        print("Haircolor: " + self.haircolor)

    def blondie_method(self):
        print("this is a very unique Blondie method")    

blondie1 = Blondie("Monica")

print(blondie1.name, "'s hair is: ", blondie1.haircolor)
print("bases: ", Blondie.__bases__)