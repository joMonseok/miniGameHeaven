import screen
import Gomoku
import dino_game
import acid_rain_game
import tug_of_war
import sys

# import dino_game
cursor_y = 0
max=4
gameIng = True
menu = [
    "1. tug of war",
    "2. gomoku",
    "3. dino game",
    "4. acid rain game",
    "5. exit"
]

def on_press():
    global cursor_y, gameIng, max
    key = screen.getRowKey()  # 키 입력 대기 (1byte 입력받기)
    
    # 전역 변수 사용
    if key == 'w':  # W: 위로 이동
        cursor_y = cursor_y-1  # 위쪽 경계값 제한
        if cursor_y<0:
            cursor_y=0
    elif key == 's':  # S: 아래로 이동
        cursor_y = cursor_y+1  # 아래쪽 경계값 제한
        if cursor_y>max:
            cursor_y=max
    elif key == '\n': 
        gameIng = False
        

mainScreenLines = [
    "╔═══════════════════════════════════════════════════════════════════════════╗",
    "║                                                                           ║",
    "║      ███╗   ███╗██╗███╗   ██╗██╗ ██████╗  █████╗ ███╗   ███╗███████╗      ║",
    "║      ████╗ ████║██║████╗  ██║██║██╔════╝ ██╔══██╗████╗ ████║██╔════╝      ║",
    "║      ██╔████╔██║██║██╔██╗ ██║██║██║  ███║███████║██╔████╔██║█████╗        ║",
    "║      ██║╚██╔╝██║██║██║╚██╗██║██║██║   ██║██╔══██║██║╚██╔╝██║██╔══╝        ║",
    "║      ██║ ╚═╝ ██║██║██║ ╚████║██║╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗      ║",
    "║      ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝      ║",
    "║                                                                           ║",
    "║            ██╗  ██╗███████╗ █████╗ ██╗   ██╗███████╗███╗   ██╗            ║",
    "║            ██║  ██║██╔════╝██╔══██╗██║   ██║██╔════╝████╗  ██║            ║",
    "║            ███████║█████╗  ███████║ ██╗ ██╔╝█████╗  ██╔██╗ ██║            ║",
    "║            ██╔══██║██╔══╝  ██╔══██║ ██║ ██║ ██╔══╝  ██║╚██╗██║            ║",
    "║            ██║  ██║███████╗██║  ██║  ████╔╝ ███████╗██║ ╚████║            ║",
    "║            ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝            ║",
    "║                                                                           ║",
    "║                                                                           ║",
    "║                                                                           ║",
    "║                     move : wasd       select : enter                      ║",
    "║                                                                           ║",
    "║     ┌──────────────────────────────────────────────────────────────┐      ║",
    "║     │                                                              │      ║",
    "║     │                                                              │      ║",
    "║     │                                                              │      ║",
    "║     │                                                              │      ║",
    "║     │                                                              │      ║",
    "║     │                                                              │      ║",
    "║     │                                                              │      ║",
    "║     │                                                              │      ║",
    "║     └──────────────────────────────────────────────────────────────┘      ║",
    "║                                                                           ║",
    "╚═══════════════════════════════════════════════════════════════════════════╝",
]

def mainScreen():
    screen.draw_centered_menu(mainScreenLines)

def showMenu():
    screen.draw_centered_menuCommand(menu,20,15,cursor_y)

    
    #screen.move_cursor_to(0, 0)



def main():
    global gameIng

    ii=0
    screen.clear()
    while True:
        while gameIng:
            mainScreen()
            showMenu()
            screen.refresh()
            on_press()
            
            #screen.clearScreen()
        screen.clearScreen()

        if cursor_y == 0:
            tug_of_war.main()
        elif cursor_y == 1:
            Gomoku.main()
        elif cursor_y == 2:
            dino_game.main()
        elif cursor_y == 3:
            acid_rain_game.main()
            
        elif cursor_y == max:
            exit()
        screen.clearScreen()
        screen.flush_input()
        gameIng=True

#curses.wrapper(main)