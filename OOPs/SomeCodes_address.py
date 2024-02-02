class Address:
    def __init__(self, city):
        self.__city=city
    def get_city(self):
        return self.__city
    
class Student:
    def __init__(self,id,marks,address):
        self.__address=address #Memory Ref ID
        self.id=id
        self.marks=marks
    
    def get_address(self):
        return self.__address
    
s1=Student(1,90,Address('Mysore'))
# add=Address('Mysore')
# print(add.get_city())
# print(id(add))
print(id(s1))
print(s1.get_address().get_city())