import turtle as t

a = t.Turtle()
b = t.Turtle()
c = t.Turtle()

a.shape("turtle")
b.shape("turtle")
c.shape("circle")

a.color("blue")
b.color("red")
c.color("green")

a.speed(0)
b.speed(0)
c.speed(0)

b.up()
b.goto(0, 200)

c.up()
c.goto(0, -200)
