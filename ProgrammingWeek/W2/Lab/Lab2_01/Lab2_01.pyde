def setup():
    size(500, 500)

def draw_balloon(x, y):
    fill(255, 0, 0)
    ellipse(x, y, 100, 100)
    line(x, y+50, x, y+200)

x = 100

def draw():
    global x
    draw_balloon(x, 200)
    x = x+10
    if x > width:
        x = 100
