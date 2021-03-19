#########################################################################################
# MC (Memory Cancel) : 메모리에 있는 값을 지울때 사용

# MR (Memory Recall) : 메모리에 있는 값을 읽어올때 사용

# MS (Memory Save) : 메모리에 값을 저장할때 사용 - 이 버튼이 없는 경우 M+ 버튼을 이용

# M+ (Memory Add) : 메모리에 값을 더할때 사용

# M- (Memory Subtract) : 메모리에 값을 뺄때 사용

# CE : 가장 최근에 입력된 값 지우기

# %(100으로 나누어 실수로 표현)

# √(제곱근 계산)

# OFF(프로그램 종료)

# ON/C(계산결과 지우고 디스플레이에 0 나타남)
#########################################################################################
import sys
import math
import tkinter as tk

# 윈도우 생성
window = tk.Tk()
window.title("My Calculator")

# memory clip board 생성
clip_frame = tk.Frame(window)
clip_frame.grid(row=0, column=0, columnspan=2, sticky='E')
clip_entry = tk.Entry(clip_frame, width=20, bg="light grey")
clip_entry.grid(row=0, column=1)
clip_entry.insert(tk.END, 0)

# 디스플레이 생성
display = tk.Entry(window, width=35, bg='white')
display.grid(row=1, column=0, columnspan=1)
# 버튼 함수 생성


def click(text):

    if text == "=":
        try:
            # 결과 값을 계산
            result = str(eval(display.get()))
            # 메인 디스플레이를 지우고
            display.delete(0, tk.END)
            # 결과 값을 추가합니다.
            display.insert(tk.END, result)
        except:
            display.insert(tk.END, "=>*ERROR*")
    elif text == "CE":
        # 현재 display_entry 글자 수를 구해서
        display_len = len(display.get())
        # 마지막 글자만 지운다
        display.delete(display_len-1, tk.END)
    elif text == "ON/C":
        display.delete(0, tk.END)
        zero = float('0')
        display.insert(tk.END, zero)
    elif text == "√":
        result = str(math.sqrt(float(display.get())))
        # 메인 디스플레이를 지우고
        display.delete(0, tk.END)
        # 결과 값을 추가합니다.
        display.insert(tk.END, result)
    elif text == 'OFF':
        window.destroy()

    else:
        # 그 외의 버튼을 누르면 그 버튼의 Text 값을 Entry에 출력
        display.insert(tk.END, text)


# Memory 버튼 생성
def funcClick(key):
    display.configure(state=tk.NORMAL)
    # M+ 키를 누른 경우
    if key == 'M+':
        x = float(clip_entry.get())
        y = float(display.get())
        result = (x + y)
        # 클립보드1의 내용을 삭제
        clip_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 1로 복사
        clip_entry.insert(tk.END, result)
        display.delete(0, tk.END)
    # MR 키를 누른 경우
    elif key == 'MR':
        # 클립보드1의 내용을 display에 추가
        display.insert(tk.END, clip_entry.get())
    elif key == 'MC':
        # 클립보드1의 내용 삭제
        clip_entry.delete(0, tk.END)
    elif key == 'M-':
        x = float(clip_entry.get())
        y = float(display.get())
        result = (x - y)
        # 클립보드1의 내용을 삭제
        clip_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 1로 복사
        clip_entry.insert(tk.END, result)
        display.delete(0, tk.END)
    elif key == '%':
        p = float(display.get())
        result = p/100
        # 메인 디스플레이를 지우고
        display.delete(0, tk.END)
        # 결과 값을 추가합니다.
        display.insert(tk.END, str(result))


# 버튼 프레임 생성
button_frame = tk.Frame(window)
button_frame.grid(row=2, column=0)

# 버튼생성
MBTN_list = ['MC',  'MR',  'M-',  'M+',  '%']

button_list = [
    '√',  '7',  '8',  '9',  '/ ',
    'OFF',  '4',  '5',  '6',  '* ',
    'CE',  '1',  '2',  '3',  '-',
    'ON/C', '0', '.', '=', '+']

row_index = 1
col_index = 0
for mbtn_text in MBTN_list:
    def mem_cmd(t=mbtn_text):
        funcClick(t)
    tk.Button(button_frame, text=mbtn_text, width=5, command=mem_cmd).grid(
        row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0

for btn_text in button_list:
    def cmd(t=btn_text):
        click(t)
    tk.Button(button_frame, text=btn_text, width=5, command=cmd).grid(
        row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
