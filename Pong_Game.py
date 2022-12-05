import turtle

#Creating the game Screen
wn=turtle.Screen()
wn.title("Pong Game By Jai Trivedi")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score of the Players
score_a=0
score_b=0


#Paddle A
paddle_A=turtle.Turtle()
'''Sets the speed of the paddle'''
paddle_A.speed(0)
'''Name Of the content inside shape and side should be checked carefully
   and should be in lower case'''
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

#Paddle B
paddle_B=turtle.Turtle()
'''Sets the speed of the paddle'''
paddle_B.speed(0)
'''Name Of the content inside shape and side should be checked carefully
   and should be in lower case'''
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5,stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

#Ball
Ball=turtle.Turtle()
'''Sets the speed of the paddle'''
Ball.speed(0)
'''Name Of the content inside shape and side should be checked carefully
   and should be in lower case'''
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)

#Ball Movement on Game Display
Ball.dx=0.2
Ball.dy=0.2

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier", 24, "normal"))

#Function For Paddle A Movement

def paddle_A_up():
    y=paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y=paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

#Function For Paddle B Movement

def paddle_B_up():
    y=paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_down():
    y=paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)
#Keyboard Binding Defining Keys From The keyboard (Check The Indentation First)
wn.listen()
wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")


#main Game Loop

while True:
    wn.update()

    #Move The Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border Checking / Creating Top/Bottom For Game Window
    if Ball.ycor() > 290:
         Ball.sety(290)
         Ball.dy *= -1

    if Ball.ycor() < -290:
         Ball.sety(-290)
         Ball.dy *= -1

    #Border Creating For the Left and Right Game Window
    if Ball.xcor() > 390:
         Ball.goto(0,0)
         Ball.dx *= -1
         score_a += 1
         pen.clear()
         pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
         Ball.goto(0,0)
         Ball.dx *= -1
         score_b += 1
         pen.clear()
         pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier", 24, "normal"))


    #Paddle And Ball Collision
    if Ball.xcor() < -340 and Ball.ycor() < paddle_A.ycor() + 50 and Ball.ycor() > paddle_A.ycor() - 50:
        
        Ball.dx *=-1

    #Paddle And Ball Collision
    elif Ball.xcor() > 340 and Ball.ycor() < paddle_B.ycor() + 50 and Ball.ycor() > paddle_B.ycor() - 50:
        
        Ball.dx *=-1
         
