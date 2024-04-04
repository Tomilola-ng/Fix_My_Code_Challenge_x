#!/usr/bin/python3
""" SQUARE """

class Square:
    """ SQUARE """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ SQUARE """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ SQUARE """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return f"Square(width={self.width}, height={self.height})"

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
