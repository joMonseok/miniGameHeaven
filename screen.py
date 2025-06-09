import os
import curses

stdscr=0

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
