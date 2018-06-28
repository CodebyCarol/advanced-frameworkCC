class Plant:
    '''represents the common propertis of all the plants in the garden'''
    
    plants = []
    live = True

    def __init__(self, name):
        self.name = name
        self.__class__.plants.append(self)

    def die(self):
        print("~~I am dying~~")
        Plant.plants.remove(self)
        live = False

    def tell_my_name(self):
        print(self.name)
