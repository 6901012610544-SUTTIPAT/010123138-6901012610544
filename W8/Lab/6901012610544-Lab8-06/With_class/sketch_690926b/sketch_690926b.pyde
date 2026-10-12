# ==========================================================
# Program 2: Balloon Animation with Class
# ==========================================================

class Balloon:
    def __init__(self, x, y, speed, col):
        """Initialize balloon attributes."""
        self.x = x
        self.y = y
        self.speed = speed
        self.color = col  # (R, G, B) tuple

    def update(self):
        """Move the balloon upward and wrap around when off-screen."""
        self.y -= self.speed
        if self.y < -100:
            self.y = height + 50

    def show(self):
        """Draw the balloon using instance attributes."""
        # Draw string
        stroke(120)
        strokeWeight(1.5)
        line(self.x, self.y + 38, self.x, self.y + 95)
        
        # Draw balloon body
        noStroke()
        fill(self.color[0], self.color[1], self.color[2])
        ellipse(self.x, self.y, 60, 76)
        
        # Draw balloon knot
        triangle(self.x - 5, self.y + 42, self.x + 5, self.y + 42, self.x, self.y + 37)


# List containing 5 Balloon objects
balloons = []

def setup():
    size(600, 600)
    
    # Populate the array with 5 Balloon instances
    balloons.append(Balloon(100, 600, 2.0, (255, 99, 132)))
    balloons.append(Balloon(200, 650, 3.2, (54, 162, 235)))
    balloons.append(Balloon(300, 580, 1.5, (255, 206, 86)))
    balloons.append(Balloon(400, 620, 2.8, (75, 192, 192)))
    balloons.append(Balloon(500, 670, 2.2, (153, 102, 255)))

def draw():
    background(235, 245, 255)
    
    # Update and display each balloon object
    for b in balloons:
        b.update()
        b.show()
