#Simple PingpOOng

import turtle # basic graphics
import os
import time

#window 
wn = turtle.Screen()
wn.title('PingPong')
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) # stops the window from updating, we can speed up our game a bit 

#Counting the score
scoreA = 0 
scoreB = 0 

#Paddle A
paddleA= turtle.Turtle()    #class name Turtle()
paddleA.speed(0)            #speed of animation 
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)        #place of a paddle 

#Paddle B 
paddleB= turtle.Turtle()    #class name Turtle()
paddleB.speed(0)            #speed of animation 
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)        #place of animation 

#Ball
ball= turtle.Turtle()      #class name Turtle()
ball.speed(0)              #speed of animation 
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0) 
ball.dx = 0.3              #every time our ball moves it moves by 2 pixels
ball.dy = -0.3

#Scoring default 
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()                 #we do not want to draw a line 
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Move the paddles Functions
def paddleA_up():
    y = paddleA.ycor()      #ycor() from the turtle module 
    y += 20                 #add pixels
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()      #ycor() from the turtle module 
    y -= 20                 #add pixels
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()      #ycor() from the turtle module 
    y += 20                 #add pixels
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()      #ycor() from the turtle module 
    y -= 20                 #add pixels
    paddleB.sety(y)

#Keyboard binding 
wn.listen()                         #listen to keaybord input 
wn.onkeypress(paddleA_up, "a")       #when users clics w call the functiuon paddleA_up
wn.onkeypress(paddleA_down, "s") 
wn.onkeypress(paddleB_up, "Up") 
wn.onkeypress(paddleB_down, "Down") 


#Main game loop, every time the while goes updates the screen 
while True: 
    wn.update()

    #Move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check 
    if ball.ycor() > 290:           #top boarder
        ball.sety(290)
        ball.dy *= -1               #reverses the direction 
        os.system("afplay bounce.wav&")
    
    if ball.ycor() < -290:          #bottom border
        ball.sety(-290)
        ball.dy *= -1  
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)              #right side
        ball.dx *= -1
        scoreA += 1 
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)              #left side
        ball.dx *= -1 
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball bounce 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40): 
        ball.setx(340)
        ball.dx  *= -1
        # ball.dx -= 0.02
        
        os.system("afplay bounce.wav&")
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40): 
        ball.setx(-340)
        ball.dx  *= -1
        # ball.dx += 0.02
        os.system("afplay bounce.wav&")