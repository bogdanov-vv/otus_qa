from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    @property
    def area(self):
        return self.a * self.a

    @property
    def perimeter(self):
        return self.a * 4

    def add_area(self, other):
        if not isinstance(other, Figure):
            raise ValueError('Передан не правильный класс!')
        return self.area + other.area
