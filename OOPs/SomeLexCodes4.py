class Mobile:
    def __init__(self,brand,case):
        self.brand=brand
        self.case=case
    def display(self):
        print(self.case.color)

class Case:
    def __init__(self,color):
        self.color=color
        
c1=Case("Black")
c2=Case("White")
m1=Mobile("Hony",c1)
c1.color="Green"
m1.display()
 