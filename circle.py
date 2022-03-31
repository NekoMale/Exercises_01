import math

class Circle:
    def __init__(self, x_center, y_center, radius):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    @property
    def center(self):
        return self.x_center, self.y_center

    def translate(self, delta_x, delta_y):
        self.x_center += delta_x
        self.y_center += delta_y

    def translate_to(self, new_x, new_y):
        self.x_center = new_x
        self.y_center = new_y

    def scale(self, delta_radius):
        self.radius += delta_radius

    def rescale(self, new_radius):
        self.radius = new_radius

    def get_circumference(self):
        return 2 * self.radius * math.pi

    def get_area(self):
        return self.radius * self.radius * math.pi

    def __add__(self, other):
        return Circle(self.x_center + other.x_center, self.y_center + other.y_center, self.radius + other.radius)

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()
