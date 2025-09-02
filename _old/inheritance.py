from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def __repr__(self):
        return f'Circle(radius={self.radius})'

# Проверка
rectangle = Rectangle(4, 3)
circle = Circle(9)

print(rectangle.area())  # 12
print(circle.area())     # 254.34

print(rectangle)
print(circle)