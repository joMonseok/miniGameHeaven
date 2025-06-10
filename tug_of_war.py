import os
import platform
import screen
import time

# 게임 설정
WIDTH = 21
CENTER = WIDTH // 2
position = CENTER
game_over = False


# 화면 지우기
def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")


# 줄 그리기
def draw():
    bar = ['-'] * WIDTH
    bar[position] = '|'
    str = ''.join(bar)
    drawStr=[
        "Player 1: [A] / Player 2: [L]",
        "Press the keys quickly to defeat your opponent!",
        "       "+str
    ]
    screen.draw_centered_menu(drawStr)
    screen.refresh()

def onPress_key():
    global position
    key = screen.getKey()
    
    if key == 'a':
        position = position-1
        if position <= 0:
            screen.clear()
            screen.draw_centered_str("🎉 Player 1 Wins!")
            screen.refresh()
            return False
    elif key == 'l':
        position = position+1
        if position >= WIDTH - 1:
            screen.clear()
            screen.draw_centered_str("🎉 Player 2 Wins!")
            screen.refresh()
            return False
    draw()
    return True
    


mainScreenLines = [
    " ________  __    __   ______          ______   ________        __       __   ______   _______  ",
    "/        |/  |  /  | /      \        /      \ /        |      /  |  _  /  | /      \ /       \ ",
    "$$$$$$$$/ $$ |  $$ |/$$$$$$  |      /$$$$$$  |$$$$$$$$/       $$ | / \ $$ |/$$$$$$  |$$$$$$$  |",
    "   $$ |   $$ |  $$ |$$ | _$$/       $$ |  $$ |$$ |__          $$ |/$  \$$ |$$ |__$$ |$$ |__$$ |",
    "   $$ |   $$ |  $$ |$$ |/    |      $$ |  $$ |$$    |         $$ /$$$  $$ |$$    $$ |$$    $$< ",
    "   $$ |   $$ |  $$ |$$ |$$$$ |      $$ |  $$ |$$$$$/          $$ $$/$$ $$ |$$$$$$$$ |$$$$$$$  |",
    "   $$ |   $$ \__$$ |$$ \__$$ |      $$ \__$$ |$$ |            $$$$/  $$$$ |$$ |  $$ |$$ |  $$ |",
    "   $$ |   $$    $$/ $$    $$/       $$    $$/ $$ |            $$$/    $$$ |$$ |  $$ |$$ |  $$ |",
    "   $$/     $$$$$$/   $$$$$$/         $$$$$$/  $$/             $$/      $$/ $$/   $$/ $$/   $$/ ",
    "                                                                                               " ,  
    "                                                                                               "  , 
    "                                 Press Any Key to Start the Game                               "
]

guideStr = [
    "╔════════════════════════════════════════════════════════════════════╗",
    "║                         🕹️  How to play guide                       ║",
    "╠════════════════════════════════════════════════════════════════════╣",
    "║   🔹 It\'s a two-player keyboard combo game.                        ║",
    "║                                                                    ║",
    "║   🔸 Player 1 : [ A ] Keep hitting the keys!                       ║",
    "║   🔸 Player 2 : [ L ] Keep hitting the keys!                       ║",
    "║                                                                    ║",
    "║   ⏱️ The person who pulls the rope all the way to the end wins!    ║",
    "║                                                                    ║",
    "║   🚀 When you are ready, press any key to start the game.          ║",
    "╚════════════════════════════════════════════════════════════════════╝"
]

def tug_of_war():
    global position, game_over
    position = CENTER
    game_over = False
    screen.clear()
    screen.draw_centered_menu(mainScreenLines)
    screen.refresh()
    start = ''
    key=screen.getKey()
    gameIng=True
    if start == '':
        screen.clearScreen()
        screen.draw_centered_menu(guideStr)
        screen.refresh()

        screen.getKey()

        screen.clearScreen()
        draw()

        while gameIng:
            gameIng = onPress_key()


    time.sleep(5)  # 5초 대기


if __name__ == "__main__":
    tug_of_war()


def main():
    
    tug_of_war()
