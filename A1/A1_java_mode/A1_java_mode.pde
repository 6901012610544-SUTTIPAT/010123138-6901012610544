// Main variables
int mass_count = 1;         // number of mass block hanging
float mass_unit = 0.01;     // mass per 1 block
float k_true = 4.0;         // theoretical spring constant
int max_blocks = 8;         // maximum number of blocks for dynamic scaling

// Var for simulation
boolean is_oscillating = false; // oscillating state
float sim_time = 0.0;            // stopwatch
float current_T = 0.0;           // Period per lap
float t_total_measured = 0.0;    // total sim time
float current_mass = 0.0;        // mass_count * mass_unit

// Latest record
float last_time_10 = 0.0;
float last_T = 0.0;

// Dynamic list variables for plotting graph
FloatList mass_list; // X-Axis
FloatList t_sq_list; // Y-Axis

// Result variables
float best_fit_m = 0.0;          // for finding slope
float best_fit_c = 0.0;          // for finding y-intercept
float k_exp = 0.0;               // experimental spring constant
boolean experiment_done = false; // True when complete 6 simulation -> plot the graph

void setup() {
  size(1000, 600);
  mass_list = new FloatList();
  t_sq_list = new FloatList();
}

void draw() {
  background(245);

  // line separating left-right
  stroke(180);
  strokeWeight(2);
  line(480, 0, 480, 600);

  // updating spring
  float y_offset = 0;
  if (is_oscillating) {
    float dt = 1.0 / 60.0; // simulation at 60 fps
    sim_time += dt;

    // Simple Harmonic Motion
    y_offset = 50 * cos(2 * PI * sim_time / current_T);

    // pause after 10 oscillations
    if (sim_time >= t_total_measured) {
      is_oscillating = false;
      record_data();
    }
  }

  // show result
  draw_simulation_panel(y_offset);
  draw_graph_panel();
}

// Proportional scaling function
float map_val(float val, float in_min, float in_max, float out_min, float out_max) {
  return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void draw_simulation_panel(float y_offset) {
  // left title
  fill(0);
  textSize(24);
  textAlign(CENTER);
  text("Spring Constant Experiment", 240, 40);

  // ceiling
  fill(100);
  noStroke();
  rect(190, 80, 100, 20);

  // equilibrium point 
  float base_y = 200 + (mass_count * 8);

  // draw spring and mass block
  draw_spring(240, 100, base_y + y_offset);
  draw_masses(240, base_y + y_offset);

  // Instruction (Controls)
  textAlign(LEFT);
  textSize(16);
  fill(30);

  text("[ Controls ]", 30, 415);
  text("UP / DOWN : Add / Remove Mass", 30, 440);
  text("SPACEBAR  : Start 10 Oscillations", 30, 465);
  text("R         : Reset Experiment", 30, 490);

  // mass information display and timer
  fill(0, 102, 153);
  text("Mass : " + nf(mass_count * mass_unit, 0, 2) + " kg", 30, 540);

  // stopwatch
  if (is_oscillating) {
    fill(200, 50, 50); // red while timing is in progress
    text("Stopwatch : " + nf(sim_time, 0, 2) + " s", 30, 570);
  } else {
    if (last_time_10 > 0) {
      fill(0, 150, 0); // green when the timer has finished
      text("Stopwatch : " + nf(last_time_10, 0, 2) + " s", 30, 570);

      // display calculated value
      fill(0, 102, 153);
      text("Period (T) : " + nf(last_T, 0, 3) + " s", 220, 540);
      text("T^2 : " + nf(last_T * last_T, 0, 4) + " s^2", 220, 570);
    } else {
      fill(100); // gray before starting
      text("Stopwatch : 0.00 s", 30, 570);
    }
  }
}

void draw_spring(float x, float y_start, float y_end) {
  int num_coils = 14;
  float coil_width = 15;
  float dist = y_end - y_start;
  float dy = dist / num_coils;

  stroke(80);
  strokeWeight(3);
  noFill();

  beginShape();
  vertex(x, y_start);

  for (int i = 1; i < num_coils; i++) {
    float cx = (i % 2 == 1) ? (x + coil_width) : (x - coil_width);
    float cy = y_start + i * dy;
    vertex(cx, cy);
  }

  vertex(x, y_end);
  endShape();
}

void draw_masses(float x, float y) {
  float block_h = 16;
  float block_w = 46;
  float start_y = y;

  for (int i = 0; i < mass_count; i++) {
    fill(220, 80, 50);
    stroke(0);
    strokeWeight(1);
    rect(x - block_w / 2.0, start_y + i * block_h, block_w, block_h);
  }
}

void draw_graph_panel() {
  fill(0);
  textSize(24);
  textAlign(CENTER);
  text("Graph : Mass vs T^2", 740, 40);

  float origin_x = 560;
  float origin_y = 450;
  float max_x = 940;
  float max_y = 120;

  // Calculate dynamic boundaries based on theoretical physics formula
  float max_mass_limit = max_blocks * mass_unit;
  float max_t2_limit = (4 * PI * PI * max_mass_limit / k_true) * 1.15; // 15% margin for random error

  // draw axis
  stroke(0);
  strokeWeight(2);
  line(origin_x, origin_y, max_x + 20, origin_y);
  line(origin_x, origin_y, origin_x, max_y - 20);

  // axis title
  textSize(14);
  fill(0);
  textAlign(CENTER);
  text("Mass (kg)", max_x, origin_y + 40);
  textAlign(RIGHT);
  text("T^2 (s^2)", origin_x - 10, max_y - 30);

  // X-axis scale (Dynamic)
  for (int i = 0; i <= max_blocks; i++) {
    float val = i * mass_unit;
    float px = map_val(val, 0, max_mass_limit, origin_x, max_x);
    stroke(150);
    strokeWeight(1);
    line(px, origin_y, px, origin_y + 5);

    fill(0);
    textAlign(CENTER);
    text(nf(val, 0, 3), px, origin_y + 20);
  }

  // Y-axis scale (Dynamic)
  for (int i = 0; i <= 10; i++) {
    float val = i * (max_t2_limit / 10.0);
    float py = map_val(val, 0, max_t2_limit, origin_y, max_y);
    stroke(150);
    strokeWeight(1);
    line(origin_x - 5, py, origin_x, py);

    fill(0);
    textAlign(RIGHT);
    text(nf(val, 0, 2), origin_x - 10, py + 5);
  }

  // draw best-fit line
  if (experiment_done) {
    float x1 = 0.0;
    float y1 = best_fit_c;
    float x2 = max_mass_limit;
    float y2 = best_fit_m * x2 + best_fit_c;

    float px1 = map_val(x1, 0, max_mass_limit, origin_x, max_x);
    float py1 = map_val(y1, 0, max_t2_limit, origin_y, max_y);
    float px2 = map_val(x2, 0, max_mass_limit, origin_x, max_x);
    float py2 = map_val(y2, 0, max_t2_limit, origin_y, max_y);

    stroke(200, 50, 50);
    strokeWeight(2);
    line(px1, py1, px2, py2);
  }

  // plot points
  for (int i = 0; i < mass_list.size(); i++) {
    float mx = mass_list.get(i);
    float my = t_sq_list.get(i);
    float px = map_val(mx, 0, max_mass_limit, origin_x, max_x);
    float py = map_val(my, 0, max_t2_limit, origin_y, max_y);

    fill(40, 120, 220);
    noStroke();
    ellipse(px, py, 10, 10);
  }

  // show conclusion data
  if (experiment_done) {
    fill(0);
    textAlign(LEFT);
    textSize(18);
    text("Experiment Completed (6 Trials)", 560, 520);

    textSize(16);
    text("Slope (m) = " + nf(best_fit_m, 0, 4) + " s^2/kg", 560, 550);

    fill(200, 0, 0);
    text("Experimental k = " + nf(k_exp, 0, 2) + " N/m", 560, 580);

    fill(0, 120, 0);
    text("True k = " + k_true + " N/m", 780, 580);
  } else {
    fill(100);
    textAlign(LEFT);
    textSize(16);
    text("Trials done: " + mass_list.size() + " / 6", 560, 520);
  }
}

void keyPressed() {
  // press r or R to reset
  if (key == 'r' || key == 'R') {
    reset_experiment();
  } else if (!is_oscillating && !experiment_done) {
    if (keyCode == UP) {
      if (mass_count < max_blocks) {
        mass_count++;
      }
    } else if (keyCode == DOWN) {
      if (mass_count > 1) {
        mass_count--;
      }
    } else if (key == ' ') {
      start_oscillation();
    }
  }
}

void start_oscillation() {
  is_oscillating = true;
  sim_time = 0.0;
  current_mass = mass_count * mass_unit;

  float T_true = 2 * PI * sqrt(current_mass / k_true);
  float error_factor = random(0.96, 1.04);

  current_T = T_true * error_factor;
  t_total_measured = 10 * current_T;
}

void record_data() {
  last_time_10 = t_total_measured;
  last_T = current_T;

  mass_list.append(current_mass);
  t_sq_list.append(current_T * current_T);

  if (mass_list.size() == 6) {
    experiment_done = true;
    calculate_k();
  }
}

void calculate_k() {
  int n = mass_list.size();
  float sum_x = 0.0;
  float sum_y = 0.0;
  float sum_xy = 0.0;
  float sum_xx = 0.0;

  for (int i = 0; i < n; i++) {
    float x = mass_list.get(i);
    float y = t_sq_list.get(i);
    sum_x += x;
    sum_y += y;
    sum_xy += (x * y);
    sum_xx += (x * x);
  }

  float denominator = (n * sum_xx) - (sum_x * sum_x);

  if (denominator != 0) {
    best_fit_m = ((n * sum_xy) - (sum_x * sum_y)) / denominator;
    best_fit_c = (sum_y - best_fit_m * sum_x) / n;
    k_exp = (4 * PI * PI) / best_fit_m;
  }
}

void reset_experiment() {
  mass_count = 1;
  is_oscillating = false;
  sim_time = 0.0;
  current_T = 0.0;
  t_total_measured = 0.0;
  current_mass = 0.0;
  last_time_10 = 0.0;
  last_T = 0.0;
  mass_list.clear();
  t_sq_list.clear();
  experiment_done = false;
  best_fit_m = 0.0;
  best_fit_c = 0.0;
  k_exp = 0.0;
}
