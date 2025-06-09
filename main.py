import mainScreen
import screen
import sys
import os


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
    screen.setStdscr(stdscr)
    curses.curs_set(0)   # 커서 숨김 
    curses.start_color()
    mainScreen.main()

main()