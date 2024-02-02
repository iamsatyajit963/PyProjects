class Lion:
    __water_source="well in the circus"

    def __init__(self,name, gender):
        self.__name=name
        self.__gender=gender

    def drink_water(self):
        print(self.__name,"drinks water from the",Lion.__water_source)

simba=Lion("Simba","Male")
nala=Lion("Nala","Female")
simba.drink_water()
nala.drink_water()