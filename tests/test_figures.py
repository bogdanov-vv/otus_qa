from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
import pytest


@pytest.mark.triangle
class TestTriangle:
    def test_triangle_name(self):
        tri = Triangle()
        assert tri.name == 'Triangle', "Figure is have not name Triangle"

    def test_triangle_area(self):
        tri = Triangle(10, 13, 10)
        assert tri.area == 65, "Triangle area is not true"

    def test_triangle_perimeter(self):
        tri = Triangle(10, 13, 10)
        assert tri.perimeter == 33, "Triangle perimiter is not true"

    def test_triangle_sum_rectangle(self):
        rec = Rectangle(10)
        print()
        print(rec.area)
        tri = Triangle(10, 13, 10)
        print(tri.area)
        print(tri.add_area(rec))
        assert tri.add_area(rec) == 165, "Res not 165!"
        assert rec.add_area(tri) == 165, "Res not 165!"


@pytest.mark.square
class TestSquare:
    def test_square_name(self):
        sq = Square()
        assert sq.name == 'Square', "Figure is have not name Square"

    def test_square_area(self):
        sq = Square(10)
        assert sq.area == 100, "Square area is not true"

    def test_square_perimeter(self):
        sq = Square(10)
        assert sq.perimeter == 40, "Square perimiter is not true"


@pytest.mark.circle
class TestCircle:
    def test_circle_name(self):
        cr = Circle()
        assert cr.name == 'Circle', "Figure is have not name Circle"

    def test_circle_area(self):
        cr = Circle(10)
        assert cr.area == 100, "Circle area is not true"

    def test_circle_perimeter(self):
        cr = Circle(10)
        assert cr.perimeter == 40, "Circle perimiter is not true"


@pytest.mark.rectangle
class TestRectangle:
    def test_rectangle_name(self):
        rec = Rectangle()
        assert rec.name == 'Rectangle', "Figure is have not name Rectangle"

    def test_rectangle_area(self):
        rec = Rectangle(10)
        assert rec.area == 100, "Rectangle area is not true"

    def test_rectangle_perimeter(self):
        rec = Rectangle(10)
        assert rec.perimeter == 40, "Rectangle perimiter is not true"
