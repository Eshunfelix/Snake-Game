from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 15, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.ht()
       # self.screen.bgcolor("white")
        self.goto(0,280)
        self.speed("fastest")
        self.color("white")
        self.update_screen()

    def update_screen(self):
        self.goto(0, 275)
        self.write(arg=f"Score:  {str(self.score)} ", align=ALIGNMENT, move=True, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_screen()
    def game_over(self):
        self.home()
        self.write(arg=f"Game Over ", align=ALIGNMENT, move=True, font=FONT)


