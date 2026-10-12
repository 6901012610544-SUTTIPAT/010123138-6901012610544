x = 50
speed = 3
circle_color = 255

def setup():
    size(400, 400)

def draw_bg_lines():
    background(30)
    stroke(80)
    i = 0
    while i < width:
        line(i, 0, i, height)
        i += 40

def draw():
    global x, speed
    
    draw_bg_lines()
    
    fill(circle_color, 100, 200)
    noStroke()
    ellipse(x, 200, 40, 40)
    
    x = x + speed
    
    if x > width or x < 0:
        speed = -speed

def mousePressed():
    global circle_color
    circle_color = (circle_color + 50) % 255

def keyPressed():
    global speed
    if key == ' ':
        speed = -speed
