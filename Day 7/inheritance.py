class Shape:
    def print_shape_area(self):
        print("Function for area")
        print("Call by super()")


class Circle(Shape):
    def print_shape_area(self):
        super().print_shape_area()
        self.r = 5
        area = 3.14*self.r**2
        return area

class Rectangle(Shape):
    def print_shape_area(self,):
        self.l = 10
        self.b = 20
        area = self.l * self.b
        return area

def print_shape_areas(shape):
    print(f"Area is {shape.print_shape_area()} ")



c1 = Circle()
#print(c1.print_shape_area())
print_shape_areas(c1)

r1 = Rectangle()
#print(r1.print_shape_area())



