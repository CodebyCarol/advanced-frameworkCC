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

print(woman1.name + "also can call the parent class, so she can tell that already " +
                    (str)(woman1.count_dudes) + " instance has beencreated")