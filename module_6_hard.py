class Figure:
    sides_count = 0
    def __init__(self, __color, __sides):
        self.__color = __color
        self.__sides = __sides
        filled = True    # заливка фигуры

    @property
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r and g and b is int and r and g and b in [0, 255]:
           return True

    # @set_color.setter
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.r = r
            self.g = g
            self.b = b
            self.__color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *args):
        #for sides in args:
        if args is int and args > 0:
           return True
        else:
            return False

    @property
    def get_sides(self):
        return (self.__sides)

    def __len__(self):
        return (sum[self.sides])


    def set_sides(self, *new_sides):
        if self.new_sides == self.sides_count:
            self.new_sides = new_sides


class Circle(Figure):
    sides_count = 1

    # object_Figure__self.__color = [r, g, b]
    # def __init__(self, _radius):
    # super().__init__()
    # _radius = super().__len__() / (2 * 3, 14)

    @property
    def get_square(self):
        return (3,14 * self.__radius^2)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color)
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())