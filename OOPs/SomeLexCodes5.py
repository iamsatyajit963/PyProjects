class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        # print(cover.color)
        cover.color="yellow"
class Cover:
    def __init__(self):
        self.color="red"
    # def get_colors(self):
    #     return self.__color
Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())
print(Cover().color)