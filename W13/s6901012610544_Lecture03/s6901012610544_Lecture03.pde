//Slide Title "Function Parameter" and "Function Call"

void setup(){
  size(500, 500);
  draw_balloon(50, 50);
}

void draw_balloon(int x, int y){
  ellipse(x, y, 100, 100);
  line(x, y+50, x, y+200);
}
