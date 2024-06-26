import random


from point import point

COLORS = ["red", "blue", "green", "yellow", "purple", "pink", "beige","turquoise", "saffron", "peach", "magenta"]


class ColoredPoint(point): #this class inherits from point
    def __init__(self,x ,y, color):
        self.x = x
        self.y = y
        if color in self.COLORS:
            slef.color = color
        else:
            raise Exception(f"That is an ivalid color. Accepted colors are {self.COLORS}")


    def __str__(self):
        return f"self.color({self.x}, {self.y})"

    @classmethod
    def add_extra_color(self, color):
        self.COLORS.append(color)

    @property
    def distance_origin(self):
        result = (self.x**2 +self.y**2)**0.5
        if result == int(result):
            return int(result)
        else:
            return result


p1 = ColoredPoint(10, 10, "red")
# Let's create a list of 5 random colored points
colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.choice(COLORS)
                     )
    )
if __name__ == "__main__":
    print(colored_points)
    # lets add orange as an extra color
    ColoredPoint.add_extra_color("orange")
    p2 = ColoredPoint(5,5, "orange")
    p2.x = 77
    print(p2)
    print(f"p2={p2} and has distance to origin={p2.distance_origin()}")


