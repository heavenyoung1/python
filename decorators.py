class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Радиус не может быть отрицательным')
        self._radius = value

    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(-1)
print(circle.radius)
print(circle.area)


