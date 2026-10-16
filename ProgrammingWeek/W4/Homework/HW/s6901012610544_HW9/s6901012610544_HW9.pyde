'''
6901012610544 Suttipat Euaphattanakit
Item: Loop: fixed number(draw_ladder)
'''

def setup():
    size(500, 500)
    stroke(0)
    strokeWeight(2)
    noLoop()

def draw():
    background(255,255,255)
    draw_ladder(220, 450, 5)

def draw_ladder(x, y, s):
    ladder_width = 60
    step_spacing = 30
    total_height = s * step_spacing
    
    line(x, y, x, y - total_height)
    line(x + ladder_width, y, x + ladder_width, y - total_height)
    
    i = 0
    while i <= s:
        current_y = y - (i * step_spacing)
        line(x, current_y, x + ladder_width, current_y)

        i = i + 1
