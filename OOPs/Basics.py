class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def area(self): # Calculating Area of the rectangle
        return self.width * self.height

    def perimeter(self): # Calculating Perimeter of the rectangle
        return 2 * (self.height + self.width) 
    
    # def __str__(self): #dunder method / magic commands `__` -> dunder special commands, that runs bts
    #     return 'Rectangle with (width {0}, height {1})'.format(self.width, self.height)

    def __eq__(self, other):
        print('self{0}, other{1}'.format(self, other)) # printing address
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if (width <= 0):
            raise ValueError('Width must be positive.')
        self._width = width
        
        
        

# ============================================
# r = Rectangle(10,20)

# print("Width: " + str(r.width))
# print("Height: " + str(r.height))
# print("Area = " + str(r.area()))
# print("Permiter: "+  str(r.perimeter()))
# print(str(r))     #str(r) -> will print the address of the instance.
# print(r) # this will also print the address of the instance, but if we want to print any specific string/sentence, \
           # then we can use dunder function of the string to override the function in runtime

# ===========================================

# r1 = Rectangle(10,20) #<__main__.Rectangle object at 0x000002D4AF16F850>
# r2 = Rectangle(10,20) #<__main__.Rectangle object at 0x000002D4AF16F890>

# print(r1 == r2) # False, why because the address of both the instances are different.
#                 # If in general these to rectangle instances should be equal,as its height and width are equal.
#                 # in order to do so, we need to override the __eq__ function in the runtime and create the custom conditions.
                  # Similarly, we can implement less than __lt__, greatere than __gt__ etc...
# ===========================================


r = Rectangle(10,20)
print(r._width)
print(r._height)

r.width = -10 # reallocation of the width to a newer value. Let's say we dont want our users to change the value of the rectangle 
              # after the instance creation, what should we do to acheive that? Here comes decorators -> private in Java
print(r._width)
print(r._height)