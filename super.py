
class Shape:
 def __init__(self, color,filled):
    self.color = color
    self.filled = filled
    
def describe(self):
 print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
 def __init__(self, color,filled, radius):
      super().__init__(color, filled)
      self.radius = radius

 def describe(self):
    print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shape):
 def __init__(self, color,filled, width):
      super().__init__(color, filled)
      self.width = width

 def describe(self):
    print(f"It is a square with an area of {self.width * self.width}cm^2")

class Triangle(Shape):
 def __init__(self, color,filled, base, height):
    super().__init__(color, filled)
    self.base = base
    self.height = height

 def describe(self):
    print(f"It is a traingle with an area of {self.base * self.height / 2}cm^2")



circle = Circle(color="red",filled=True, radius=5)
square = Square(color="blue", filled = False, width = 10)
triangle=Triangle(color ="green", filled = True, base = 8, height = 6)

triangle.describe()
