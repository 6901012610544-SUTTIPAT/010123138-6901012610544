balloon_y = 250
timer = 0

def setup():
    size(500, 500)

def draw():
    global balloon_y, timer
    background(220, 240, 255) #Clear sky blue
    timer += 1
    
    #Draw the kid
    ellipse(200, 380, 40, 40) #Head
    line(200, 400, 200, 460)   #Body
    line(200, 460, 180, 480)   #Left Leg
    line(200, 460, 220, 480)   #Right Leg
    line(200, 420, 180, 440)   #Left Arm
    line(200, 420, 240, 400)   #Right Arm
    
    #Balloon logic
    if timer < 100:
        #State 1: Holding the balloon
        line(240, 400, 240, balloon_y + 25)
    else:
        #State 2: Release Balloon
        balloon_y -= 3 
        #String floats dynamically underneath the balloon
        line(240, balloon_y + 25, 240, balloon_y + 75)
        
    #Draw balloon
    ellipse(240, balloon_y, 40, 50)
    
    #loop
    if balloon_y < -50:
        balloon_y = 250
        timer = 0
