from woman import Blondie


class Longie(Blondie):
    'try to reach parent class from Longie (the long hair blondies)'

    long = 50

    def __init__(self, name, long):
        self.name = name
        self.long = long
        haircolor = super
        print("initialize Longie")

    # override
    def blondie_method(self):
        print("this is a very unique Blondie method overrided in Longie")

longie1 = Longie("Rapunzel", 400)
blondie2 = Blondie("Summer")

print(longie1.haircolor)        
longie1.blondie_method() 
blondie2.blondie_method()
