import random
import atexit
import sys
import os
import tkinter as tk

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def goodbye():
    text.insert(tk.END,'정답입니다. 축하합니다!!\n')
    
def game():
    global tryIdx
    if tryIdx >=11:
        text.insert(tk.END,'***GAME OVER***\n')
        sys.exit()

    isAnswer=False
    guessNum=int(display.get())
    text.insert(tk.END,guessNum)
    if guessNum>answerNum :
        text.insert (tk.END,'\n정답보다 큰 숫자입니다.\n')
    elif guessNum<answerNum :
        text.insert(tk.END,'\n정답보다 작은 숫자입니다.\n')
    else :
        isAnswer=True
        
    if isAnswer:
        text.insert(tk.END,'\n정답입니다. 축하합니다!!\n')
        text.insert(tk.END,'***GAME OVER***\n')
        sys.exit()
    elif tryIdx == MAX_TRY:
        text.insert(tk.END,'\n[실패]도전' + str(MAX_TRY) + '회 동안 정답을 맞추지 못했습니다.\n')
        text.insert(tk.END,'정답은 ' + str(answerNum) + "입니다.\n")
        
    tryIdx += 1
    Q=str(tryIdx) + "번째 시도) 숫자를 입력하세요\n"
    text.insert(tk.END,Q)

def click (text):
    if text == '입력':
        game()
    elif text == '삭제':
        display.delete(0,tk.END)
    else:
        display.insert(tk.END, text)

window = tk.Tk()
window.title("숫자 맞추기 게임")

display = tk.Entry(window, width=35,bg='white')
display.grid(row=0, column=0, columnspan=1)

tk.Button(window, text="Restart", command=restart_program).grid(row=3,column=0,sticky='N')

button_frame=tk.Frame(window)
button_frame.grid(row=2,column=0)

button_list = [
 '7',  '8',  '9',
 '4',  '5',  '6',
 '1',  '2',  '3',
'입력','0','삭제']

row_index = 1
col_index = 0

for btn_text in button_list:
    def cmd(t=btn_text):
        click(t)
    tk.Button(button_frame, text= btn_text,height=1,width=10,command=cmd).grid(row=row_index,column=col_index)
    col_index += 1
    if col_index > 2:
        row_index += 1
        col_index = 0

MAX_RANDOM=100
MAX_TRY=10
tryIdx=1

answerNum=random.randint(1, MAX_RANDOM)

text = tk.Text(master=window,height=100,width=100,bg="white")
text.grid(column=0,row=4)
text.insert(tk.END,"1부터 " + str(MAX_RANDOM) + "까지의 숫자중에서 하나의 숫자를 맞추는 게임입니다.\n숫자를 입력하면 큰값인지, 적은값인지, 정답인지가 화면에 표시가 됩니다. \n총 " + str(MAX_TRY) + "회 의 기회가 주어집니다.\n")
Q=str(tryIdx) + "번째 시도) 숫자를 입력하세요\n"
text.insert(tk.END,Q)

window.mainloop()
