import turtle
t = turtle.Pen()
turtle.bgcolor("#fabebe")
t.speed(100)
t.color("#fcc5dc", "#f0ccdb")

def main_heart():

    def center():
        t.up()
        t.left(180)
        t.forward(45)
        t.right(180)

        t.left(90)
        t.forward(110)
        t.right(90)
        t.down()

    center()

    for x in range (36):
        t.up()
        t.forward(100)
        t.down()
        t.pencolor("#fcc5dc")
        t.begin_fill()
        t.fillcolor("#f0ccdb")
        t.pensize(7)
        t.left(50)
        t.forward(133)
        t.circle(50,200)
        t.right(140)
        t.circle(50,200)
        t.forward(133)
        t.end_fill()

    def gaint_heart():
        t.up()
        t.right(80)
        t.forward(305)
        t.left(80)
        t.down()

        t.color("#e65757") 
        t.begin_fill()
        t.pensize(7)
        t.left(50)
        t.forward(266)
        t.circle(100,200)
        t.left(140)
        t.right(280)
        t.circle(100,200)
        t.forward(266)
        t.end_fill()

    gaint_heart()

main_heart()

def spirral():
    colors = ["#996a88", "#8ebdb5", "#8eb8bd", "#6496d9", "#916a99", "#9c8ebd"]
    t = turtle.Pen()
    turtle.bgcolor("black")
    t.speed(-999)
    for x in range(600):
        t.pencolor(colors[x%6])
        t.width(x//200+1)
        t.forward(x)
        t.right(100)

spirral()