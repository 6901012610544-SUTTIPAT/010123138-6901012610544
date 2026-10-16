import random
import math


def setup():
    background(0,255,255)
    size(500,500)
    
def draw():
    global COLOR
    COLOR = color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    x = random.randint(100, 400)
    y = random.randint(150, 350)
    d = cal_distance(x, 200, mouseX, mouseY)
    draw_balloon(x, y, 40)
    if mouseX > x:
        line(x, 20, x, y+d)
    else:
        line(x, 20, x, y-d)
        
    delay(250)
     
    
def cal_distance(x1, y1, x2, y2):
    diffX = abs(x1-x2)
    diffY = abs(y1-y2)
    result = sqrt(diffX*diffX + diffY*diffY)
    return result
    
def draw_balloon(x, y, r):
    draw_circle(x, y, r)
    line(x, y+(r/2), x, y+200)

def draw_circle(x, y, r):
    global COLOR
    fill(COLOR)
    ellipse(x, y, 2*r, 2*r)
