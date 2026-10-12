import random

#Main variables
mass_count = 1 #number of mass block hanging
mass_unit = 0.01 #mass per 1 block
k_true = 4.0 #theoretical spring constant
max_blocks = 8 #maximum number of blocks for dynamic scaling

#Var for simulation
is_oscillating = False #oscillating state
sim_time = 0.0 #stopwatch
current_T = 0.0 #Period per lap
t_total_measured = 0.0 #total sim time
current_mass = 0.0 #mass_count * mass_unit

#Latest record
last_time_10 = 0.0
last_T = 0.0

#list variable for plotting graph
mass_list = [] #X-Axis
t_sq_list = [] #Y-Axis

#result variable
best_fit_m = 0.0 #for finding slope
best_fit_c = 0.0 #for finding y-intercept
k_exp = 0.0 #experimental spring constant
experiment_done = False #True when complete 6 simulation -> plot the graph

def setup():
    size(1000, 600)

def draw():
    global sim_time, is_oscillating
    background(245)

    #line separating left-right
    stroke(180)
    strokeWeight(2)
    line(480, 0, 480, 600)

    #updating spring
    y_offset = 0
    if is_oscillating:
        dt = 1.0 / 60.0 #simulation at 60 fps
        sim_time += dt
        
        #Simple Harmonic Motion
        y_offset = 50 * cos(2 * PI * sim_time / current_T)

        #pause after 10 times
        if sim_time >= t_total_measured:
            is_oscillating = False
            record_data()

    #show result
    draw_simulation_panel(y_offset)
    draw_graph_panel()

#Proportional scaling function
def map_val(val, in_min, in_max, out_min, out_max):
    return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def draw_simulation_panel(y_offset):
    #left title
    fill(0)
    textSize(24)
    textAlign(CENTER)
    text("Spring Constant Experiment", 240, 40)

    #ceiling
    fill(100)
    noStroke()
    rect(190, 80, 100, 20)

    #equilibrium point 
    base_y = 200 + (mass_count * 8) 
    
    #draw spring and mass block
    draw_spring(240, 100, base_y + y_offset)
    draw_masses(240, base_y + y_offset)

    # Instruction (Controls)
    textAlign(LEFT)
    textSize(16)
    fill(30)
    
    text("[ Controls ]", 30, 415)
    text("UP / DOWN : Add / Remove Mass", 30, 440)
    text("SPACEBAR  : Start 10 Oscillations", 30, 465)
    text("R         : Reset Experiment", 30, 490)

    #mass information display and timer
    fill(0, 102, 153)
    text("Mass : " + str(round(mass_count * mass_unit, 2)) + " kg", 30, 540)
    
    #stopwatch
    if is_oscillating:
        fill(200, 50, 50) #red while timing is in progress.
        text("Stopwatch : " + str(round(sim_time, 2)) + " s", 30, 570)
    else:
        if last_time_10 > 0:
            fill(0, 150, 0) #green when the timer has finished.
            text("Stopwatch : " + str(round(last_time_10, 2)) + " s", 30, 570)
            
            #display calculate value
            fill(0, 102, 153)
            text("Period (T) : " + str(round(last_T, 3)) + " s", 220, 540)
            text("T^2 : " + str(round(last_T * last_T, 4)) + " s^2", 220, 570)
        else:
            fill(100) #gray before starting
            text("Stopwatch : 0.00 s", 30, 570)

def draw_spring(x, y_start, y_end):
    num_coils = 14
    coil_width = 15
    dist = y_end - y_start
    dy = dist / num_coils

    stroke(80)
    strokeWeight(3)
    noFill()

    beginShape()
    vertex(x, y_start)
    
    i = 1
    while i < num_coils:
        if i % 2 == 1:
            cx = x + coil_width
        else:
            cx = x - coil_width
            
        cy = y_start + i * dy
        vertex(cx, cy)
        i += 1
        
    vertex(x, y_end)
    endShape()

def draw_masses(x, y):
    block_h = 16
    block_w = 46
    start_y = y
    
    i = 0
    while i < mass_count:
        fill(220, 80, 50)
        stroke(0)
        strokeWeight(1)
        rect(x - block_w / 2.0, start_y + i * block_h, block_w, block_h)
        i += 1

def draw_graph_panel():
    fill(0)
    textSize(24)
    textAlign(CENTER)
    text("Graph : Mass vs T^2", 740, 40)

    origin_x = 560
    origin_y = 450
    max_x = 940
    max_y = 120
    
    # Calculate dynamic boundaries based on theoretical physics formula
    max_mass_limit = max_blocks * mass_unit
    max_t2_limit = (4 * PI * PI * max_mass_limit / k_true) * 1.15 # 15% margin for random error

    # draw axis
    stroke(0)
    strokeWeight(2)
    line(origin_x, origin_y, max_x + 20, origin_y) 
    line(origin_x, origin_y, origin_x, max_y - 20) 

    # axis title
    textSize(14)
    fill(0)
    textAlign(CENTER)
    text("Mass (kg)", max_x, origin_y + 40)
    textAlign(RIGHT)
    text("T^2 (s^2)", origin_x - 10, max_y - 30)

    # X-axis scale (Dynamic)
    i = 0
    while i <= max_blocks:
        val = i * mass_unit
        px = map_val(val, 0, max_mass_limit, origin_x, max_x)
        stroke(150)
        strokeWeight(1)
        line(px, origin_y, px, origin_y + 5)
        
        fill(0)
        textAlign(CENTER)
        text(str(round(val, 3)), px, origin_y + 20)
        i += 1

    # Y-axis scale (Dynamic)
    i = 0
    while i <= 10:
        val = i * (max_t2_limit / 10.0)
        py = map_val(val, 0, max_t2_limit, origin_y, max_y)
        stroke(150)
        strokeWeight(1)
        line(origin_x - 5, py, origin_x, py)
        
        fill(0)
        textAlign(RIGHT)
        text(str(round(val, 2)), origin_x - 10, py + 5)
        i += 1

    # draw line
    if experiment_done:
        x1 = 0.0
        y1 = best_fit_c
        x2 = max_mass_limit
        y2 = best_fit_m * x2 + best_fit_c

        px1 = map_val(x1, 0, max_mass_limit, origin_x, max_x)
        py1 = map_val(y1, 0, max_t2_limit, origin_y, max_y)
        px2 = map_val(x2, 0, max_mass_limit, origin_x, max_x)
        py2 = map_val(y2, 0, max_t2_limit, origin_y, max_y)

        stroke(200, 50, 50)
        strokeWeight(2)
        line(px1, py1, px2, py2)

    # plot points
    i = 0
    while i < len(mass_list):
        mx = mass_list[i]
        my = t_sq_list[i]
        px = map_val(mx, 0, max_mass_limit, origin_x, max_x)
        py = map_val(my, 0, max_t2_limit, origin_y, max_y)

        fill(40, 120, 220)
        noStroke()
        ellipse(px, py, 10, 10)
        i += 1

    # show conclusion data
    if experiment_done:
        fill(0)
        textAlign(LEFT)
        textSize(18)
        text("Experiment Completed (6 Trials)", 560, 520)
        
        textSize(16)
        text("Slope (m) = " + str(round(best_fit_m, 4)) + " s^2/kg", 560, 550)
        
        fill(200, 0, 0)
        text("Experimental k = " + str(round(k_exp, 2)) + " N/m", 560, 580)
        
        fill(0, 120, 0)
        text("True k = " + str(k_true) + " N/m", 780, 580)
    else:
        fill(100)
        textAlign(LEFT)
        textSize(16)
        text("Trials done: " + str(len(mass_list)) + " / 6", 560, 520)

def keyPressed():
    global mass_count
    
    #press r or R to reset
    if key == 'r' or key == 'R':
        reset_experiment()
        
    elif not is_oscillating and not experiment_done:
        if keyCode == UP:
            if mass_count < max_blocks:
                mass_count += 1
        elif keyCode == DOWN:
            if mass_count > 1:
                mass_count -= 1
        elif key == ' ':
            start_oscillation()

def start_oscillation():
    global is_oscillating, sim_time, current_T, t_total_measured, current_mass
    
    is_oscillating = True
    sim_time = 0.0
    current_mass = mass_count * mass_unit

    T_true = 2 * PI * sqrt(current_mass / k_true)
    error_factor = random.uniform(0.96, 1.04) 
    
    current_T = T_true * error_factor
    t_total_measured = 10 * current_T

def record_data():
    global mass_list, t_sq_list, experiment_done, last_time_10, last_T
    
    last_time_10 = t_total_measured
    last_T = current_T

    mass_list.append(current_mass)
    t_sq_list.append(current_T * current_T)

    if len(mass_list) == 6:
        experiment_done = True
        calculate_k()

def calculate_k():
    global best_fit_m, best_fit_c, k_exp
    
    n = len(mass_list)
    sum_x = 0.0
    sum_y = 0.0
    sum_xy = 0.0
    sum_xx = 0.0

    i = 0
    while i < n:
        x = mass_list[i]
        y = t_sq_list[i]
        sum_x += x
        sum_y += y
        sum_xy += (x * y)
        sum_xx += (x * x)
        i += 1

    denominator = (n * sum_xx) - (sum_x * sum_x)
    
    if denominator != 0:
        best_fit_m = ((n * sum_xy) - (sum_x * sum_y)) / denominator
        best_fit_c = (sum_y - best_fit_m * sum_x) / n
        k_exp = (4 * PI * PI) / best_fit_m

def reset_experiment():
    #Reset all variable
    global mass_count, is_oscillating, sim_time, current_T, t_total_measured
    global current_mass, last_time_10, last_T, mass_list, t_sq_list
    global experiment_done, best_fit_m, best_fit_c, k_exp

    mass_count = 1
    is_oscillating = False
    sim_time = 0.0
    current_T = 0.0
    t_total_measured = 0.0
    current_mass = 0.0
    last_time_10 = 0.0
    last_T = 0.0
    mass_list = []
    t_sq_list = []
    experiment_done = False
    best_fit_m = 0.0
    best_fit_c = 0.0
    k_exp = 0.0
