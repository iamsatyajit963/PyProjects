class Student:
    def __init__(self,id,marks):
        self.id=id
        self.__marks=marks
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def __add__(self,other): #overload
        print(other.get_marks()-self.get_marks())
        
s1=Student(1,90)
s2=Student(2,40)
print(s1+s2)
print()