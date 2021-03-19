import random
import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("파이썬 가위바위보 게임")

USER_SCORE = 0
COMP_SCORE = 0
TIE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps = {'바위':0,'보':1,'가위':2}
    return rps[choice]
def number_to_choice(number):
    rps={0:'바위',1:'보',2:'가위'}
    return rps[number]

def random_computer_choice():
    return random.choice(['바위','보','가위']) 

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    global TIE
    global WIN_GAME
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    text = tk.Text(master=window,height=1,width=30,bg="light grey")
    text.grid(column=1,row=3)
   
    if(user==comp):
        text.insert(tk.END,"현재 사용자 승패 상황 : 무")
        TIE+=1
    elif((user-comp)%3==1):
        text.insert(tk.END,"현재 사용자 승패 상황 : 승")
        USER_SCORE+=1
    else:
        text.insert(tk.END,"현재 사용자 승패 상황 : 패")
        COMP_SCORE+=1
    if(USER_SCORE>=3):
        print("GAME OVER!\nYOU WIN :)")
        window.destroy()
    if(COMP_SCORE>=3):
        print("GAME OVER!\nYOU LOSE :(")
        window.destroy()
    text_area = tk.Text(master=window,height=7,width=30,bg="light grey")
    text_area.grid(column=1,row=2)
    answer = "사용자가 낸 결과: {uc} \n컴퓨터가 낸 결과: {cc} \n==총 승부 결과== \n    승: {u} \n    패: {c} \n    무 :{t}".format(t=TIE,uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)
    text_area.insert(tk.END,answer)
     
    
    


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='바위'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='보'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
   
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='가위'
    COMP_CHOICE=random_computer_choice() 
    result(USER_CHOICE,COMP_CHOICE)
def EXIT():
    window.destroy()

 
photo1 = tk.PhotoImage(file='rock.png')
photo2 = tk.PhotoImage(file='paper.png')
photo3 = tk.PhotoImage(file='scissor.png')

button1 = tk.Button(image=photo1,height=130,width=130,command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(image=photo2,height=130,width=130,command=paper)
button2.grid(column=1,row=1)
button3 = tk.Button(image=photo3,height=130,width=130,command=scissor)
button3.grid(column=2,row=1)
button4=tk.Button(text='EXIT',width=10,bg='grey',command=EXIT)
button4.grid(row=4, column=0,columnspan=2,sticky='NE')
window.mainloop()


