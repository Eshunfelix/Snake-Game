from turtle import Turtle , Screen
screen = Screen()


class Snake:
    # class Variables. Reference to them require
    # the use of cls.variablename
    UP = 90
    RIGHT = 0
    LEFT = 180
    DOWN = 270

    def __init__(self):
        self.pos = [(0, 0), (-20, 0), (-40, 0)]
        self.segs = []
        self.distance = 20
        self.currentpos = []
        #self.xcor = segs[0]

    def create_snake(self):
        for i in self.pos:
            new_seg = Turtle(shape="square")
            new_seg.pu()
            new_seg.color("white")
            new_seg.goto(i)
            new_seg.speed("fastest")
            self.segs.append(new_seg)
            self.currentpos.append(new_seg.position())

    def add_segments(self):
        cordinates = self.segs[-1].position()
        new_turtle = Turtle(shape="square")
        new_turtle.pu()
        new_turtle.color("white")
        new_turtle.speed("fastest")
        new_turtle.goto(int(cordinates[0]), int(cordinates[1]))
        self.segs.append(new_turtle)
        self.currentpos.append(new_turtle.position())

    def move(self):
        for seg_num in range(len(self.segs) - 1, 0, -1):
            self.segs[seg_num].setx(self.segs[seg_num - 1].xcor())
            self.segs[seg_num].sety(self.segs[seg_num - 1].ycor())
            # new_x = self.segs[seg_num - 1].xcor()
            # new_y = self.segs[seg_num - 1].ycor()
            # self.segs[seg_num].goto(new_x, new_y)
        self.segs[0].fd(self.distance)

    def up(self):
        if self.segs[0].heading() != 270:
            self.segs[0].setheading(90)

    def down(self):
        if self.segs[0].heading() != 90:
            self.segs[0].setheading(270)

    def left(self):
        if self.segs[0].heading() != 0:
            self.segs[0].setheading(180)

    def right(self):
        if self.segs[0].heading() != 180:
            self.segs[0].setheading(0)

    def hey(self):
        print("hey")
