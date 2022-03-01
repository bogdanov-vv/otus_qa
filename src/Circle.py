from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    @property
    def area(self):
        return self.a * self.a

    @property
    def perimeter(self):
        return self.a * 4

    def add_area(self, other):
        if not isinstance(other, Figure):
            raise ValueError('Передан неправильный класс!')
        return self.area + other.area
