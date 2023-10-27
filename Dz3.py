class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Box:
    def __init__(self):
        self.squares = []

    def add_square(self, square):
        self.squares.append(square)

    def total_area(self):
        total = 0
        for square in self.squares:
            total += square.area()
        return total

square1 = Square(2)
square2 = Square(3)

box = Box()

box.add_square(square1)
box.add_square(square2)

# Виведення інформації
print(f"Площа першого квадрата: {square1.area()}")
print(f"Площа другого квадрата: {square2.area()}")
print(f"Загальна площа коробки: {box.total_area()}")

