#Global variables
x_pos = 200
y_pos = 200
box_size = 40
step = 150

def setup():
    size(1000, 300)
    rectMode(CENTER)
    noFill()
    stroke(70, 130, 180)
    strokeWeight(1.5)

def draw():
    global x_pos, y_pos, box_size, step
    background(255)
    i = 0
    
    while i < 5:
        draw_positive(x_pos + i * step, y_pos, box_size)
        i = i + 1


#Function that draws a single square
def draw_square(x, y, size_val):
    rect(x, y, size_val, size_val)

#Function that draws a plus sign using draw_square()
def draw_positive(x, y, size_val):
    draw_square(x, y, size_val)
    draw_square(x, y - size_val, size_val)
    draw_square(x, y + size_val, size_val)
    draw_square(x - size_val, y, size_val)
    draw_square(x + size_val, y, size_val)
