class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides
    
    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all((num > 0) for num in self.sides):
                sort_sides = sorted(self.sides)
                if sort_sides[0] + sort_sides[1] > sort_sides[2]:
                    return 'Ура! Из этого можно слепить треугольник!'
                return 'Из этих отрезков треугольника не получится!'    
            return 'Необходимы только положительные числа!'    
        return 'Необходимы числа!'

triangle_1 = TriangleChecker([71, 3, 1])
print(triangle_1.is_triangle())

triangle_2 = TriangleChecker(['1', 2, 1])
print(triangle_2.is_triangle())

triangle_3 = TriangleChecker([2, 3, 4])
print(triangle_3.is_triangle())

triangle_4 = TriangleChecker([-2, 2, 2])
print(triangle_4.is_triangle())
