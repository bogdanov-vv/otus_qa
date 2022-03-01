from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    @property
    def area(self):
        return (self.a * self.b) / 2

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    def add_area(self, other):
        if not isinstance(other, Figure):
            raise ValueError('Передан не правильный класс!')
        return self.area + other.area
