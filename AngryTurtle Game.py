#201931397_이승하_프로그래밍 기초_중간고사 대체 과제물(2)

import turtle
import math
import random


g=turtle.Turtle()
g.shape("square")
g.color("brown")
g.pensize(10)
g.hideturtle()
g.fd(500)

t = turtle.Turtle()
t.color("green")
t.shape("circle")
t.penup()
t.speed(0)
t.goto(470,-20)
t.turtlesize(None,None,8)

player = turtle.Turtle()
player.shape("turtle")
player.color("red")
screen = player.getscreen()
screen.bgpic("field.gif")                       #배경화면 변경(free image 사용)

def turnleft():
        player.left(5)				# 왼쪽으로 5도 회전
	
def turnright():
        player.right(5)				# 오른쪽으로 5도 회전

def fire():
    x = 0
    y = 0
    s = turtle.textinput("", "Angry Turtle:(\n거북이의 속도를 설정하세요:")
    v=int(s)
    velocity = v				# 초기 속도 50픽셀/sec
    angle = player.heading()		# 초기 각도 
    vx = velocity * math.cos(angle * 3.14 / 180.0)	# 도 -> 라디안
    vy = velocity * math.sin(angle * 3.14 / 180.0)	# 도 -> 라디안
    while player.ycor() >= 0 :		# y좌표가 음수가 될 때까지
            vx = vx
            vy = vy - 10
            x = x + vx
            y = y + vy
            player.goto(x, y)
            if (player.distance(t)<20):
                if True :
                    t.hideturtle()         #게임 방법: 대략 turnleft 7회, v=74 일때에 목표물에 도달
                    player.penup()
                    player.color("green")
                    player.write("Mission Complete!\n",False,"center")
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(fire, "space")		# 사용자가 스페이스키를 누르면
screen.listen()


    
