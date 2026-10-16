# ==========================================================
# Program 1: Balloon Animation without Class
# ==========================================================

# List storing initial data (attributes) for 5 balloons:
# x: horizontal position, y: vertical position, speed: rise rate, color: (R, G, B)
balloons = [
    {"x": 100, "y": 600, "speed": 2.0, "color": (255, 99, 132)},
    {"x": 200, "y": 650, "speed": 3.2, "color": (54, 162, 235)},
    {"x": 300, "y": 580, "speed": 1.5, "color": (255, 206, 86)},
    {"x": 400, "y": 620, "speed": 2.8, "color": (75, 192, 192)},
    {"x": 500, "y": 670, "speed": 2.2, "color": (153, 102, 255)}
]

def setup():
    size(600, 600)

def draw_balloon(x, y, col):
    """Draws a single balloon and its string at (x, y) with color col."""
    # Draw string
    stroke(120)
    strokeWeight(1.5)
    line(x, y + 38, x, y + 95)
    
    # Draw balloon body
    noStroke()
    fill(col[0], col[1], col[2])
    ellipse(x, y, 60, 76)
    
    # Draw balloon knot
    triangle(x - 5, y + 42, x + 5, y + 42, x, y + 37)

def draw():
    background(235, 245, 255)  # Sky blue background
    
    # Loop through each balloon to update animation and draw
    for b in balloons:
        # Move balloon upward
        b["y"] -= b["speed"]
        
        # Reset to bottom when floating off the top edge
        if b["y"] < -100:
            b["y"] = height + 50
        
        # Render balloon
        draw_balloon(b["x"], b["y"], b["color"])
