import mainScreen
import platform
import screen
import sys
import os
import ctypes


#코드 진입(windoe mac 구별별)
def main():

    if platform.system()=="win32":
        import msvcrt
        import ctypes
        hConsole = ctypes.windll.kernel32.GetStdHandle(-11)
        class CONSOLE_CURSOR_INFO(ctypes.Structure):
            _fields_ = [("dwSize", ctypes.c_uint32),
                        ("bVisible", ctypes.c_bool)]
        cursor_info = CONSOLE_CURSOR_INFO()
        ctypes.windll.kernel32.GetConsoleCursorInfo(hConsole, ctypes.byref(cursor_info))
        cursor_info.bVisible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(hConsole, ctypes.byref(cursor_info))

        screen.setStdscr(msvcrt)
        screen.setPlatform(1)
        mainScreen.main()
    else:

        try:
            import curses
        except ImportError:
                os.system("pip install curses")
                import curses
        screen.setPlatform(2)
        curses.wrapper(mac)

def mac(stdscr):
    screen.setStdscr(stdscr)
    mainScreen.main()

main()