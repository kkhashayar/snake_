import turtle, time, random, math
#from pygame import mixer

screen = turtle.Screen()
screen.setup(800,600,100)
screen.bgcolor("black")
screen.tracer(1)


#mixer.init()
#eat = mixer.Sound("slide2.wav")
#sliding = mixer.Sound("walk.wav")
font = ("arial","12","bold")

arrow = turtle.Turtle()
arrow.penup()
arrow.shapesize(5)
arrow.setpos(-340, 120)
arrow.pencolor("blue")
arrow.speed(7)

score = 0
class Pen(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.setpos(x,y)
        self.pencolor(color)

###########################################
'''On screen texts. Levels - Score - movements  '''
# for score text       
pen_score = Pen(-390,270, "white")
pen_score.write("Score: ", font = font)
# for score  number
pen_score_counter = Pen(-330, 270,"white")
# For game over
pen_game_over = Pen(-120,0, "red")

def game_over():
    pen_game_over.write("Game over", font = ("arial", "30","bold"))

    
        
class Board(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.pencolor("orange")
        self.pensize(2)
        self.speed(0)
        self.setpos(-275,-275)
    def draw(self):
        for i in range (4):
            self.pendown()
            self.forward(550)
            self.left(90)
        self.penup()

class A_snake(turtle.Turtle):
    def __init__(self, snake, apple):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color("green")
        self.fillcolor("black")
        self.speed(0)
        self.shape("square")
        self.shapesize(0.5)
        self.direction = "up"
        self.blink = "on"
        self.step = 12
        self.tail = 3
        self.body = []
        self.stamp_list = []
        self.n_x = 0
        self.n_y = 0
        
class Apple(turtle.Turtle):
    def __init__(self, snake):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.pencolor("red")
        self.fillcolor("black")
        self.shape("circle")
        self.shapesize(0.5)
        self.setpos(random.randrange(-245,245), random.randrange(-245,245))
        self.blink = "on"
        

    def is_contact(self, object_2):
        a = self.xcor() - object_2.xcor()
        b = self.ycor() - object_2.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 10:
            return True
        else:
            return False

    def jump(self):
        x = random.randrange(-245,245)
        x = (12 * round(x/12))
        y = random.randrange(-245,245)
        y = (12 * round(y/12))
        if (x,y) in snake.body:
            self.jump()
        else:
            self.setpos(x,y)

    def blinking(self):
        if self.blink == "on":
            turtle.ontimer(self.pencolor("black"), t= 70)
            self.blink = "off"
        if self.blink =="off":
            self.pencolor("gold")
            self.blink = "on"

class Snake(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color("green")
        self.fillcolor("black")
        self.speed(0)
        self.shape("square")
        self.shapesize(0.5)
        self.direction = "up"
        self.blink = "on"
        self.step = 12
        self.tail = 3
        self.body = []
        self.stamp_list = []
        self.n_x = 0
        self.n_y = 0

    def blinking(self):
        if self.blink == "on":
            turtle.ontimer(self.pencolor("red"), t= 100)
            self.blink = "off"
        if self.blink =="off":
            self.pencolor("green")
            self.blink = "on"

    def update(self):
        if self.direction == "right":
            self.goto(self.xcor() + self.step, self.ycor())
        if self.direction == "left":
            self.goto(self.xcor() - self.step, self.ycor())
        if self.direction == "up":
            self.goto(self.xcor(), self.ycor() + self.step)
        if self.direction == "down":
            self.goto(self.xcor(), self.ycor() - self.step)
        else:
            self.goto(self.xcor(), self.ycor())   
        
    def left(self):
        self.direction= "left"
 #       sliding.play()
        arrow.setheading(-180)
    def right(self):
        self.direction=  "right"
  #      sliding.play()
        arrow.setheading(0)
    def up(self):
        self.direction= "up"
   #     sliding.play()
        arrow.setheading(90)
    def down(self):
        self.direction= "down"
    #    sliding.play()
        arrow.setheading(-90)
        

board = Board()
board.draw()
snake = Snake()
apple = Apple(snake)

turtle.listen()
turtle.onkey(snake.left,"Left")
turtle.onkey(snake.right,"Right")
turtle.onkey(snake.up,"Up")
turtle.onkey(snake.down,"Down")


arrow.setheading(90)

ticking = 0.1
def main():
    global score
    running = True
    while running:
        #time.sleep(ticking)
        screen.update()
        apple.blinking()
        screen.update()
        if snake.xcor() >264 or snake.xcor() < -264 or snake.ycor() > 264 or snake.ycor() < -264:
            game_over()
            running = False
            exit()
        snake.update()
        snake.body.append((snake.pos()))
        snake.stamp()
        if len(snake.body) > snake.tail:
            del snake.body[0]
            snake.clearstamps(1)
        if apple.is_contact(snake):
     #      eat.play()
            snake.blinking()
            apple.jump()
            snake.tail += 1
            score += 1
            pen_score_counter.clear()
            pen_score_counter.write(score, font = font)

        p = [i for i in snake.body]
        #print("list with head: ", p)
        f = [ i for i in snake.body[:-1]]
        #print("list without head: ", f)
        #print("-----------------------------------")
        if snake.pos() in f :
            game_over()
            running = False
    turtle.mainloop()

if __name__ =="__main__":
    main()

