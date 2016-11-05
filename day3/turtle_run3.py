import turtle as t



move = 10

def moveUp():
    global move
    move = move + 1

def moveDown():
    global move
    move = move + 1

def turn_right():
    t.setheading(0)      # 거북이의 머리 방향을 0도로 돌린다.
    t.forward(move)
    trace()
    run()

def turn_left():
    t.setheading(180)    # 거북이의 머리 방향을 180도로 돌린다.
    t.forward(move)
    run()

def turn_up():
    t.setheading(90)
    t.forward(move)
    trace()
    run()

def turn_down():
    t.setheading(270)
    t.forward(move)
    trace()
    run()

def reset():
    t.clear()            # 화면을 리셋


def run():
    if c.pos()[0] >= 150:
        c.setheading(180)
    elif c.pos()[0] <= -150:
        c.setheading(0)
    c.forward(15)

def trace():
    angle = b.towards(t.pos())
    b.setheading(angle)
    b.forward(5)




t.shape("turtle")
t.color("black", "red")
b = t.Turtle()
c = t.Turtle()
b.shape("turtle")
c.shape("circle")
b.color("blue")
c.color("green")
t.speed(0)
b.speed(0)
c.speed(0)
b.up()
b.goto(0, 200)
c.up()
c.goto(0, -200)
t.onkeypress(moveUp, "q")
t.onkeypress(moveDown, "w")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(reset, "R")
t.listen()
