import mainScreen
import screen
import sys
import os
import time

MIN_ROWS = 50
MIN_COLS = 130

def set_windows_size(rows, cols):
    # 윈도우(cmd)에서 창 크기 변경
    try:
        os.system(f'mode con: cols={cols} lines={rows}')
    except Exception as e:
        pass  # 실패해도 무시

def check_terminal_size(stdscr):
    while True:
        rows, cols = stdscr.getmaxyx()
        if rows < MIN_ROWS or cols < MIN_COLS:
            stdscr.clear()
            stdscr.addstr(0, 0, f" Terminal size is too small! Currently: {rows}x{cols}")
            stdscr.addstr(1, 0, f"Minimum size: Please send a window with at least {MIN_ROWS} rows x {MIN_COLS} columns.")
            stdscr.addstr(3, 0, "Adjust the app and don't press any more keys.")
            stdscr.refresh()
            stdscr.getch()
        elif rows < MIN_ROWS+5 and cols < MIN_COLS+5:
            stdscr.clear()
            stdscr.refresh()
            return
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
            set_windows_size(MIN_ROWS,MIN_COLS)
        else:
            raise
    curses.wrapper(game)

def game(stdscr):
    import curses
    if sys.platform != "win32":
        check_terminal_size(stdscr)
    screen.setStdscr(stdscr)
    curses.curs_set(0)   # 커서 숨김 
    curses.start_color()
    mainScreen.main()

main()