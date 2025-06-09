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
    "║            ██╗  ██╗███████╗ █████╗ ███╗   ██╗███████╗███╗   ██╗           ║",
    "║            ██║  ██║██╔════╝██╔══██╗████╗  ██║██╔════╝████╗  ██║           ║",
    "║            ███████║█████╗  ███████║██╔██╗ ██║█████╗  ██╔██╗ ██║           ║",
    "║            ██╔══██║██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██║╚██╗██║           ║",
    "║            ██║  ██║███████╗██║  ██║██║ ╚████║███████╗██║ ╚████║           ║",
    "║            ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝           ║",
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
    #screen.move_cursor_to(0, 0)
    y=10
    for line in mainScreenLines:     # lines: 한 줄씩 분리된 문자열 리스트
        screen.print(25, y, line)
        y += 1

def showMenu():
    x=57
    y=33
    #screen.move_cursor_to(x, y)
    i=0
    for item in menu:
        #screen.move_cursor_to(x, y+i)
        if(cursor_y == i):
            str = "-->"+menu[i]
            screen.print(x,y+i,str)
        else:
            screen.print(x,y+i,menu[i])
        i=i+1

    
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