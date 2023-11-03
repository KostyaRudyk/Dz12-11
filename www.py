class TriangleChecker:
    def __init__(self, side1, side2, side3):
        if side1 > 0 and side2 > 0 and side3 > 0:
            self.sides = sorted([side1, side2, side3])
        else:
            self.sides = None

    def is_triangle(self):
        if self.sides:
            if self.sides[0] + self.sides[1] > self.sides[2]:
                return "Ура, можна збудувати трикутник!"
            else:
                return "Жаль, але з цього трикутник не зробити"
        else:
            return "Із негативними числами нічого не вийде!"


