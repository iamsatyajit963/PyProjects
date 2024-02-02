class Parent:
    def __init__(self,var1):
        self.__var1=var1
    def get_var1(self):
        return self.__var1
    
class Child(Parent):
    def __init__(self, var1,var2):
        super().__init__(var1)
        self.var2=var2
    
ob1=Child(10,20)
print(ob1.get_var1(), ob1.var2)