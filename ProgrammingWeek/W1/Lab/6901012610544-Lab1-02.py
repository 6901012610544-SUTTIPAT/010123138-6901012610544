'''
6901012610544 สุทธิภัทร เอื้อพัฒนากิจ
Graphic-mode 2
'''

size(750, 400)
background(255)
strokeWeight(15)

#Setting
startX = 60
startY = 140
w = 60 #Alphabet width
h = 120 #Alphabet height
gap = 40 #Gap between alphabet
step = w + gap #Kerning
    
#X-coordinate from left to right(slot1 is the far left... slot5 is the far right)
slot1 = startX + (0 * step)
slot2 = startX + (1 * step)
slot3 = startX + (2 * step)
slot4 = startX + (3 * step)
slot5 = startX + (4 * step)
offscreen = -200 #X-coordinate for unused alphabet

#For writing words!!!
'''
Example: if you want word LINE
x_N1 = slot3
x_I1 = slot2
x_L  = slot1      
x_E  = slot4
x_N2 = offscreen
x_I2 = offscreen
'''
x_N1 = slot3
x_I1 = slot2
x_L  = slot1      
x_E  = offscreen
x_N2 = slot5
x_I2 = slot4
    

#Drawing section

#L
line(x_L, startY, x_L, startY + h)
line(x_L, startY + h, x_L + w, startY + h)
    
#I1
line(x_I1 + w/2, startY, x_I1 + w/2, startY + h)
line(x_I1, startY, x_I1 + w, startY) 
line(x_I1, startY + h, x_I1 + w, startY + h)
   
#I2
line(x_I2 + w/2, startY, x_I2 + w/2, startY + h)
line(x_I2, startY, x_I2 + w, startY) 
line(x_I2, startY + h, x_I2 + w, startY + h)
    
#N1
line(x_N1, startY + h, x_N1, startY)
line(x_N1, startY, x_N1 + w, startY + h)
line(x_N1 + w, startY + h, x_N1 + w, startY)
    
#N2
line(x_N2, startY + h, x_N2, startY)
line(x_N2, startY, x_N2 + w, startY + h)
line(x_N2 + w, startY + h, x_N2 + w, startY)
    
#E
line(x_E, startY, x_E, startY + h)
line(x_E, startY, x_E + w, startY)
line(x_E, startY + h/2, x_E + w, startY + h/2)
line(x_E, startY + h, x_E + w, startY + h)