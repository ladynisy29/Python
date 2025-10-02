class Shape:
    def __init__(self,x=0,y=1):
        self.x=x
        self.y=y
    def __str__(self,x,y):
        return f"Area is: {self.computer_area(self.x,self.y)}"
    

class Circle(Shape):
    def computer_area(self, x):
        return 3.14*self.x**2
  
    
class Square(Shape):
    def computer_area(self, x):
        return self.x**2

    

class Rectangle(Shape):
    def computer_area(self, x, y):
        return self.x*self.y
   
    

    
Dim = Rectangle(3,4)
Di = Square(3)
D = Circle(3)
print(D.computer_area(3))
print(Dim.computer_area(3,4))
print(Di.computer_area(3))

if __name__=="__main__":
    pass