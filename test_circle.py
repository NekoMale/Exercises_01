import math
import pytest
from circle import Circle

@pytest.fixture
def circle():
    return Circle(2, 2, 4)

def test_translate(circle):
    circle.translate(2, 2)
    assert circle.center == (4, 4)

def test_translate_to(circle):
    circle.translate_to(5, 5)
    assert circle.center == (5, 5)

def test_scale(circle):
    circle.scale(2)
    assert circle.radius == 6

def test_rescale(circle):
    circle.rescale(2)
    assert circle.radius == 2

def test_get_circumference(circle):
    assert circle.get_circumference() == 2 * 4 * math.pi

def test_get_area(circle):
    circle = Circle(0, 0, 4)
    assert circle.get_area() == 4 * 4 * math.pi

def test_le(circle):
    circle2 = Circle(0, 0, 3)
    assert circle2 < circle