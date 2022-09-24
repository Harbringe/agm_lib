class person():
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        area = self.l * self.b
        print(f"The area of rectangle is{area}")

    def perimeter(self):
        perimeter = (2*self.l) + (2*self.b)
        print(f"The perimeter of rectangle is {perimeter}")

l = int(input("Input length: "))
b = int(input("Input breadth: "))

r = person(l,b)
r.area()
r.perimeter()