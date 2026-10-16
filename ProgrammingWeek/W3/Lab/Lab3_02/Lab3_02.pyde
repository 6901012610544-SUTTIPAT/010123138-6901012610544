#Global variables for animation and interaction
x_pos = 200      
y_pos = 200      
box_size = 40    
scaling = 1.0    
growing = True   

#Each element will be a dictionary containing: {'x': x, 'y': y, 'size': size}
placed_shapes = []

def setup():
    size(1000, 600)
    rectMode(CENTER)        
    noFill()                
    stroke(70, 130, 180)    
    strokeWeight(1.5)       

def draw():
    global x_pos, y_pos, box_size, scaling, growing
    background(255)         
    
    #Draw permanently placed shapes
    # Loop through the list and redraw all previously placed plus signs
    for value in placed_shapes:
        draw_positive(value['x'], value['y'], value['size'])
    
    #Animation logic
    if growing:
        if scaling < 1.5:
            scaling += 0.01  
        else:
            growing = False  
    else:
        if scaling > 0.6:
            scaling -= 0.01  
        else:
            growing = True   
            
    current_size = box_size * scaling
    
    #Interaction logic : follow cursor
    x_pos += (mouseX - x_pos) * 0.05
    y_pos += (mouseY - y_pos) * 0.05
    
    #Draw the active floating plus sign that follows the cursor
    draw_positive(x_pos, y_pos, current_size)

def mousePressed():
    global x_pos, y_pos, box_size, scaling
    
    if mouseButton == LEFT:
        current_size = box_size * scaling
        
        # Save the current state (position and current size) into the list
        placed_shapes.append({
            'x': x_pos,
            'y': y_pos,
            'size': current_size
        })

#Function to draw a single square
def draw_square(x, y, size_val):
    rect(x, y, size_val, size_val)

#Function to draw a plus sign using draw_square()
def draw_positive(x, y, size_val):
    draw_square(x, y, size_val)
    draw_square(x, y - size_val, size_val)
    draw_square(x, y + size_val, size_val)
    draw_square(x - size_val, y, size_val)
    draw_square(x + size_val, y, size_val)
