num_shapes = 5
base_x = 100.0
spacing = 150.0
y_pos = 150.0
square_size = 35.0
speed = 10.0

current_x = []
target_x = []

is_expanding = False
is_collapsing = False

def setup():
    size(800, 300)
    rectMode(CENTER)
    
    i = 0
    while i < num_shapes:
        current_x.append(base_x)
        target_x.append(base_x + (i * spacing))
        i += 1

def draw_square(x, y, s):
    rect(x, y, s, s)

def draw_positive(x, y, s):
    draw_square(x, y, s)
    draw_square(x, y - s, s)
    draw_square(x, y + s, s)
    draw_square(x - s, y, s)
    draw_square(x + s, y, s)

def draw():
    global is_expanding, is_collapsing
    background(185)
    
    if is_expanding:
        i = 1
        while i < num_shapes:
            if current_x[i] < target_x[i]:
                current_x[i] += speed
                if current_x[i] > target_x[i]:
                    current_x[i] = target_x[i]
                break
            i += 1
            
        if current_x[num_shapes - 1] >= target_x[num_shapes - 1]:
            is_expanding = False

    elif is_collapsing:
        i = num_shapes - 1
        while i >= 1:
            if current_x[i] > base_x:
                current_x[i] -= speed
                if current_x[i] < base_x:
                    current_x[i] = base_x
                break
            i -= 1
            
        if current_x[1] <= base_x:
            is_collapsing = False

    fill(185)
    stroke(50)
    strokeWeight(1.5)
    
    i = 0
    while i < num_shapes:
        if i == 0 or current_x[i] > base_x:
            draw_positive(current_x[i], y_pos, square_size)
        i += 1

def mousePressed():
    global is_expanding, is_collapsing
    if mouseButton == LEFT:
        is_expanding = True
        is_collapsing = False
    elif mouseButton == RIGHT:
        is_collapsing = True
        is_expanding = False
