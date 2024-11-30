class Figure:
    sides_count = 0
    def __init__(self, __color, *__sides):
        self.__color =  list(__color)
        self.__sides = list(__sides)
        self.filled = False                                 # по умолчанию заливка фигуры отсутствует

    def __is_valid_color(self, r, g, b):                     # проверка корректности цветов
        if (type(r) is int and type(g) is int and type(b) is int
                and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
           return True

    def set_color(self, r, g, b):                            # проверка корректности цветов и их установка
        if self.__is_valid_color(r, g, b) is True:
                self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):                  # проверка корректности сторон
        if len(new_sides) == self.sides_count and all(isinstance(i, int) and i > 0 for i in new_sides):
            return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):                        # проверка корректности сторон и их установка
        massive_lst = []
        if self.__is_valid_sides(*new_sides) is True:
           self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self._radius = sides / (2 * 3.14)

    def get_square(self):
        return 3.14 * self._radius**2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        sides = [side] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())

circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади окружности:
print(circle1.get_square())
