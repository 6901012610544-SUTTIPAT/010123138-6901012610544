# ==========================================================
# Program 2: Balloon Animation with Subclass EsBalloon
# ==========================================================

class Balloon(object):
    def __init__(self, x, y, speed, col, r=60):
        """Initialize balloon attributes."""
        self.x = x
        self.y = y
        self.speed = speed
        self.color = col  # (R, G, B) tuple
        self.r = r        # Base width / radius reference

    def update(self):
        """Move the balloon upward and wrap around when off-screen."""
        self.y -= self.speed
        if self.y < -100:
            self.y = height + 50

    def show(self):
        """Draw the balloon using instance attributes."""
        h = self.r * (76.0 / 60.0)
        bottom_y = self.y + h / 2.0
        
        # Draw string
        stroke(120)
        strokeWeight(1.5)
        line(self.x, bottom_y, self.x, bottom_y + 55)
        
        # Draw balloon body
        noStroke()
        fill(self.color[0], self.color[1], self.color[2])
        ellipse(self.x, self.y, self.r, h)
        
        # Draw balloon knot
        triangle(self.x - 5, bottom_y + 4, self.x + 5, bottom_y + 4, self.x, bottom_y - 1)


class EsBalloon(Balloon):
    def __init__(self, x, y, speed, col, r=60):
        super(EsBalloon, self).__init__(x, y, speed, col, r)
        self.change = 1

    def expand_shrink(self):
        self.r = self.r + self.change

        if self.r >= 60:
            self.change = -1
        elif self.r <= 30:
            self.change = 1

    def update(self):
        # Pass (EsBalloon, self) here as well
        super(EsBalloon, self).update()
        self.expand_shrink()


#List containing Balloon and EsBalloon objects
balloons = []

def setup():
    size(600, 600)
    
    #Standard Balloon instances
    balloons.append(Balloon(100, 600, 2.0, (255, 99, 132)))
    balloons.append(Balloon(300, 580, 1.5, (255, 206, 86)))
    balloons.append(Balloon(500, 670, 2.2, (153, 102, 255)))
    
    #EsBalloon instances
    balloons.append(EsBalloon(200, 650, 3.2, (54, 162, 235), r=45))
    balloons.append(EsBalloon(400, 620, 2.8, (75, 192, 192), r=30))

def draw():
    background(235, 245, 255)
    
    for b in balloons:
        b.update()
        b.show()
