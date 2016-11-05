import turtle as t


move = 50

def turn_right():
    t.setheading(0)      # 거북이의 머리 방향을 0도로 돌린다.
    t.forward(move)

def turn_left():
    t.setheading(180)    # 거북이의 머리 방향을 180도로 돌린다.
    t.forward(move)

def turn_up():
    t.setheading(90)
    t.forward(move)

def turn_down():
    t.setheading(270)
    t.forward(move)

def reset():
    t.clear()            # 화면을 리셋




t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(reset, "R")
t.listen()
