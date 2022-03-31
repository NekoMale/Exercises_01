import math

class Circle:
    def __init__(self, x_center, y_center, radius):
        self.x_center = x_center
        self.y_center = y_center
        self.__radius = radius

    @property
    def center(self):
        return self.x_center, self.y_center

    @property
    def radius(self):
        return self.__radius

    def translate(self, delta_x, delta_y):
        self.x_center += delta_x
        self.y_center += delta_y

    def translate_to(self, new_x, new_y):
        self.x_center = new_x
        self.y_center = new_y

    def scale(self, delta_radius):
        self.__radius += delta_radius

    def rescale(self, new_radius):
        self.__radius = new_radius

    def get_circumference(self):
        return 2 * self.radius * math.pi

    def get_area(self):
        return self.radius ** 2 * math.pi

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

    def __str__(self):
        text_iter = iter('')
        for i in range(-self.radius, self.radius + 1):
            num = math.ceil(math.sqrt(self.radius ** 2 - i ** 2))
            if i == 0:
                txt = "".join("_" for _ in range(self.radius))
                txt = txt[0:-int(len(str(self.center))*0.5)] + str(self.center) + txt[0:-int(len(str(self.center))*0.5)] + f' Radius: {self.radius}'
                print(txt)
            else:
                print("{:^{}}".format("".join("_" for _ in range(2 * num)), 2 * self.radius))
