
class suma_rectangle:
        def __init__(self,side_a,side_b,side_a1,side_b1):
            self.side_a = side_a
            self.side_b = side_b
            self.side_a1 = side_a1
            self.side_b1 = side_b1
        def square(self):
            square_a = self.side_a * self.side_b
            square_b = self.side_a1 * self.side_b1
            self.square_a = square_a
            self.square_b = square_b
            print(f'площадь первой фигуры {square_a}  второй {self.square_b} ')

        def general_figuere(self):
            self.general_square = self.square_a + self.square_b
            self.general_side1 = self.side_a + self.side_b
            self.general_side2 = self.side_a1 + self.side_b1
            print(f'Площадь 3 фигуры {self.general_square} \n сторона1 = {self.general_side1}\n сторона2  = {self.general_side2}')

a = suma_rectangle(14,32,11,12)
a.square()
a.general_figuere()