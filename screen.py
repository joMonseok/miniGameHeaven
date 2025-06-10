import os
import curses
import time

stdscr=0

def draw_centered_menu(lines):
    h, w = stdscr.getmaxyx()
    n_lines = len(lines)
    n_cols = len(lines[0])
    start_y = round((h - n_lines) / 2)
    start_x = round((w - n_cols) / 2)
    for line in lines:
        stdscr.addstr(start_y,start_x,line)
        start_y=start_y+1

def draw_centered_menuCommand(lines,div=2,loc=1,cursor_y=-1):
    longest = len(max(lines, key=len))
    h, w = stdscr.getmaxyx()
    n_lines = len(lines)
    n_cols = longest
    start_y = round((h/div) *loc - (n_lines // 2))
    start_x = (w - n_cols) // 2
    idx=0
    for line in lines:
        x=(longest-len(line))//2
        if cursor_y!=-1 and idx == cursor_y:
            stdscr.addstr(start_y,start_x-4,"--> "+(" "*x)+line)
        else:
            stdscr.addstr(start_y,start_x-4,"   "+(" "*x)+line+"    ")
        idx+=1
        start_y=start_y+1
def draw_centered_str(str,div=2,loc=1):
    longest = len(str)
    h, w = stdscr.getmaxyx()
    n_cols = longest
    start_y = round((h/div) *loc)
    start_x = (w - n_cols) // 2
    stdscr.addstr(start_y,start_x,str)


def setStdscr(_stdscr):
    global stdscr
    stdscr = _stdscr

def setAsyInputMode(time):
    stdscr.nodelay(True) # True로 키 입력 비동기 처리 
    stdscr.timeout(time)  # 입력 대기 시간 설정 (ms)

def getStdscr():
    global stdscr
    return stdscr

def getmaxyx():
    global stdscr
    return stdscr.getmaxyx()

def reset():
    
    stdscr.clear()
    stdscr.nodelay(False)
    stdscr.timeout(-1)
    curses.endwin()
    curses.initscr()

#화면 지우기
def clearScreen():
    #os.system('cls' if os.name == 'nt' else 'clear')
    stdscr.clear()

#커서 이동
def move_cursor_to(x, y):
    print(f"\033[{y};{x}H", end="")  # ANSI 코드 출력

def flush_input():
    stdscr.nodelay(True)
    try:
        while stdscr.getch() != -1:
            pass
    finally:
        stdscr.nodelay(False)

def print(str):
    stdscr.addstr(str)
def print(y,x,str):
    stdscr.addstr(x,y,str)
def printColor(y,x,str,color):
    stdscr.addstr(x,y,str,curses.color_pair(color))

def refresh():
    stdscr.refresh()

def clear():
    stdscr.clear()

#키 입력 받기(하나만 enterX)
def getKey():
    key=stdscr.getch()
    return chr(key)
def getRowKey():
    return stdscr.getkey()
