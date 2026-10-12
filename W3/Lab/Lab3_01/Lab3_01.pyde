import random


def setup():
    size(600, 600)
    strokeWeight(2)
    frameRate(60)


def draw():
    background(255, 255, 255)

    x = random.randint(0, 600)
    y = random.randint(0, 600)

    draw_balloon(mouseX, mouseY)

    d = cal_distance(x, 200, mouseX, mouseY)

    if mouseX > x:
        line(x, y, x + d, y + d)
    else:
        line(x, y, x - d, y - d)



def cal_distance(x1, y1, x2, y2):
    diffX = abs(x1 - x2)
    diffY = abs(y1 - y2)

    result = sqrt(diffX * diffX + diffY * diffY)

    return result


def draw_circle(x, y, r):
    ellipse(x, y, 2 * r, 2 * r)


def draw_balloon(x, y):
    fill(255, 0, 0)
    draw_circle(x, y, 50)
    line(x, y + 50, x, y + 200)
