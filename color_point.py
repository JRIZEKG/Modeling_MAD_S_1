from point import point

colors = ["red", "blue", "green", "yellow", "purple", "pink", "beige","turquoise", "saffron", "peach", "magenta"]

class Coloredpoint(Point): #this class inherits from point
    def __init__(self,x ,y, color):
        self.x = x
        self.y = y
        slef.color = color

    def __str__(self):
        return f"self.color({self.x}, {self.y})"
#Let's create a list of 5 random colored points
colored points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.choice(colors)
                     )
    )
