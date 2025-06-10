import mainScreen
import screen
import sys
import os
import time
import threading

MIN_ROWS = 35
MIN_COLS = 90

def check_terminal_size(stdscr):
    while True:
        rows, cols = stdscr.getmaxyx()
        if rows < MIN_ROWS or cols < MIN_COLS:
            stdscr.clear()
            stdscr.addstr(0, 0, f" Terminal size is too small! Currently: {rows}x{cols}")
            stdscr.addstr(1, 0, "Minimum size: Please send a window with at least") 
            stdscr.addstr(2, 0, f"{MIN_ROWS} rows x {MIN_COLS} columns.")
            stdscr.addstr(3, 0, "Adjust the app and don't press any more keys.")
            stdscr.refresh()
            stdscr.getch()
        elif rows < MIN_ROWS+5 and cols < MIN_COLS+5:
            stdscr.clear()
            stdscr.refresh()
            return
        else:
            stdscr.clear()
            stdscr.addstr(0, 0, f" Terminal size is too small! Currently: {rows}x{cols}")
            stdscr.addstr(1, 0, "Minimum size: Please send a window with at least") 
            stdscr.addstr(2, 0, f"{MIN_ROWS} rows x {MIN_COLS} columns.")
            stdscr.addstr(3, 0, "Adjust the app and don't press any more keys.")
            stdscr.refresh()
            stdscr.getch()
        time.sleep(0.01)

#코드 진입(windoe mac 구별별)
def main():
#윈도우에서 curses 모듈이 없으면 설치
    try:
        import curses
    except ImportError:
        if sys.platform == "win32":
            os.system("pip install windows-curses")
            import curses
        else:
            raise
    
    curses.wrapper(game)

def game(stdscr):
    import curses
    check_terminal_size(stdscr)
    screen.setStdscr(stdscr)
    curses.curs_set(0)   # 커서 숨김 
    curses.start_color()
    mainScreen.main()

main()