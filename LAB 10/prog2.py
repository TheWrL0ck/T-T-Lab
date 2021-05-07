class Rectangle:
    def __init__(self, l=0, b=0):
        self.length = l
        self.breadth = b

    def get_area(self):
        print(f'Area = {self.length*self.breadth}')
recA=Rectangle(4,5)
recA.get_area()
