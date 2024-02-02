class Demo:
    counter=10
    def change_counter(self):
        self.counter+=1
    
obj1=Demo()
print(Demo.counter,end=' ')
obj1.change_counter()
print(Demo.counter)