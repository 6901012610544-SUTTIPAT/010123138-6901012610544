'''
6901012610544 Suttipat Euaphattanakit
Item: draw_rain_drops() slide page 47-49
'''

def setup():
    size(500, 500)
    background(30, 40, 60)

def draw():
    background(30, 40, 60)
    #OPTION : 1
    #fill(100, 180, 255, 150)
    #draw_rain_drops(50)

    #OPTION : 2
    #fill(0, 255, 150, 100)
    #draw_rain_drops_until(500) 
    
    #OPTION : 3
    fill(255, 100, 100, 100)
    draw_rain_drops_until_r_below(5)
    delay(100)

def draw_circle(x, y, r):
    circle(x, y, r * 2)


#Slide page 47
def draw_rain_drops(n):
    i = 0
    while i < n:
        x = random(0, 500)
        y = random(0, 500)
        r = random(3, 30)
        draw_circle(x, y, r)
        i = i + 1


#Slide page 48
def draw_rain_drops_until(volume):
    sum = 0
    while sum < volume:
        x = random(0, 500)
        y = random(0, 500)
        r = random(3, 30)
        draw_circle(x, y, r)
        
        sum = sum + r


#Slide page 49
def draw_rain_drops_until_r_below(value):
    r_flag = True
    while r_flag:
        x = random(0, 500)
        y = random(0, 500)
        r = random(3, 30)
        draw_circle(x, y, r)
        
        if r < value:
            r_flag = False
