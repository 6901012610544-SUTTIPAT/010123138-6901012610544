x = 300
y = 300
easing = 0.05
time_step = 0

#Interaction variables
shock_radius = 0      #For left click : shock wave
is_invisible = False  #For right click : invisible

def setup():
    size(600, 600)
    strokeWeight(2)
    frameRate(60)

def draw():
    global x, y, time_step, shock_radius
    
    background(10, 20, 40)
    
    #Follow cursor
    posX = mouseX
    posY = mouseY
    x += (posX - x) * easing
    y += (posY - y) * easing
    
    time_step += 0.08
    
    #Left click : shock wave
    #increase shock wave radius
    if shock_radius > 0:
        noFill()
        stroke(0, 255, 255, 255 - (shock_radius * 2)) #slowly disappear in linear
        ellipse(x, y, shock_radius, shock_radius)
        shock_radius += 5
        if shock_radius > 120: #max radius condition
            shock_radius = 0
            
    #draw jellyfish
    draw_cyber_jellyfish(x, y)

#Mouse interaction
def mousePressed():
    global shock_radius, is_invisible
    
    if mouseButton == LEFT:
        #shock wave
        shock_radius = 10 
        
    elif mouseButton == RIGHT:
        #invisible mode
        is_invisible = not is_invisible

#Subroutines

def draw_cyber_jellyfish(pos_x, pos_y):
    draw_tentacles(pos_x, pos_y)
    draw_head(pos_x, pos_y)

def draw_head(hx, hy):
    global is_invisible
    
    #Check for invisible mode
    if is_invisible:
        #if yes, fill inside with tranparent, left only stroke
        noFill()
        stroke(0, 255, 255, 70) 
        ellipse(hx, hy, 100, 80)
        ellipse(hx, hy, 50, 40)
    else:
        #if no, fill normally
        fill(0, 255, 255, 100)
        stroke(0, 255, 255)
        ellipse(hx, hy, 100, 80)
        
        fill(255, 0, 128, 200)
        ellipse(hx, hy, 50, 40)
        
        fill(255)
        ellipse(hx - 15, hy, 10, 10)
        ellipse(hx + 15, hy, 10, 10)

def draw_tentacles(tx, ty):
    global is_invisible
    
    #Check for invisible
    if is_invisible:
        stroke(0, 255, 255, 40)
    else:
        stroke(0, 255, 255, 150)
        
    for i in range(5):
        start_x = tx - 40 + (i * 20)
        start_y = ty + 20
        
        offset = sin(time_step + i) * 25
        end_x = start_x + offset
        end_y = start_y + 80
        
        line(start_x, start_y, end_x, end_y)
        
        if is_invisible:
            noFill()
        else:
            fill(0, 255, 255)
        ellipse(end_x, end_y, 8, 8)
