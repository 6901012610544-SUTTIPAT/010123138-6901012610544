'''
6901012610544 Suttipat Euaphattanakit
Item: draw_vertical_lines slide page 45-46
'''


def setup():
    size(500, 400)
    stroke(0)
    strokeWeight(3)
    noLoop()

def draw():
    background(255)
    draw_vertical_lines(100, 200, 200, 200)

def draw_vertical_lines(x1, y1, x2, y2):
    space = abs(x1 - x2)/5
    
    while x1 <= x2: 
        line(x1, y1 - 50, x1, y1 + 50)
        x1 = x1 + space
