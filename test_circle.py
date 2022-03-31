import math
import pytest
from circle import Circle

@pytest.fixture
def circle():
    return Circle(2, 2, 4)

def test_translate(circle):
    circle.translate(2, 2)
    assert circle.center == (4, 4)

def test_get_circumference(circle):
    assert circle.get_circumference() == 2 * 4 * math.pi

def test_get_area(circle):
    circle = Circle(0, 0, 4)
    assert circle.get_area() == 4 * 4 * math.pi

def test_le(circle):
    circle2 = Circle(0, 0, 3)
    assert circle2 < circle