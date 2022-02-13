import turtle
t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.width(2)
t.speed(20)
col=('red','cyan','blue','green')

for i in range (350):
    t.pencolor(col[i%4])
    t.forward(i*4)
    t.right(140)