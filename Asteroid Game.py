#201931397_이승하_프로그래밍 기초_중간고사 대체 과제물(1)
import turtle
import random
import math

player = turtle.Turtle()
player.color("yellow")
player.shape("arrow")
player.penup()
player.speed(0)
s=player.screen
screen = player.getscreen()
colors=["pink","purple","black","white","grey"]
screen.bgpic("asteroids.gif")


asteroids=[]
for i in range (10):
    a1=turtle.Turtle()
    a1.color(colors[i%5])
    a1.shape("circle")
    a1.penup()
    a1.speed(0)
    a1.goto(random.randint(-300,300),random.randint(-300,300))
    asteroids.append(a1)

    
def turnleft():
	player.left(30) # 왼쪽으로 30도 회전한다.

def turnright():
	player.right(30) # 오른쪽으로 30도 회전한다.
def turnup():
    player.setheading(90) #player의 방향을 위쪽으로 전환한다.
def turndown():
    player.setheading(270) #player의 방향을 아래쪽으로 전환한다.

screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(turnup,"Up")
screen.onkeypress(turndown,"Down")
screen.listen()

def play():
    player.forward(3) # 2픽셀 전진
    for b in asteroids:
        b.right(random.randint(-180,180))
        b.fd(3)
        if player.distance(b)<10:
            player.write("HIT!\n",False,"center")  #소행성과 충돌 시 문자열"HIT!" 출력
            b.hideturtle()

        
    screen.ontimer(play, 10) # 10ms가 지나면 play()를 다시 호출.
    
screen.ontimer(play, 10) # 10ms가 지나면 play()를 다시 호출.
