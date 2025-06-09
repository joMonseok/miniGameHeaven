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
    screen.print(40,20,"Player 1: [A] / Player 2: [L]")
    screen.print(40,21,"Press the keys quickly to defeat your opponent!")
    screen.print(45,24, str)
    screen.refresh()

def onPress_key():
    global position
    key = screen.getKey()
    
    if key == 'a':
        position = position-1
        if position <= 0:
            screen.clear()
            screen.print(40,21,"🎉 Player 1 Wins!")
            screen.refresh()
            return False
    elif key == 'l':
        position = position+1
        if position >= WIDTH - 1:
            screen.clear()
            screen.print(40,21,"🎉 Player 2 Wins!")
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
    "                                                                                                 "   
]
def tug_of_war():
    global position, game_over
    position = CENTER
    game_over = False
    screen.clear()
    y=20
    for mainScreenLine in mainScreenLines:
        screen.print(20,y,mainScreenLine)
        y=y+1
    y=y+2
    screen.print(27,y,"Press Any Key to Start the Game")
    screen.refresh()
    start = ''
    key=screen.getKey()
    gameIng=True
    if start == '':
        screen.clearScreen()
        screen.print(27,12, "╔════════════════════════════════════════════════════════════════════╗\n")
        screen.print(27,13, "║                         🕹️  How to play guide                       ║\n")
        screen.print(27,14, "╠════════════════════════════════════════════════════════════════════╣\n")
        screen.print(27,15, "║   🔹 It\'s a two-player keyboard combo game.                        ║\n")
        screen.print(27,16, "║                                                                    ║\n")
        screen.print(27,17, "║   🔸 Player 1 : [ A ] Keep hitting the keys!                       ║\n")
        screen.print(27,18, "║   🔸 Player 2 : [ L ] Keep hitting the keys!                       ║\n")
        screen.print(27,19, "║                                                                    ║\n")
        screen.print(27,20,"║   ⏱️ The person who pulls the rope all the way to the end wins!    ║\n")
        screen.print(27,21,"║                                                                    ║\n")
        screen.print(27,22,"║   🚀 When you are ready, press any key to start the game.          ║\n")
        screen.print(27,23,"╚════════════════════════════════════════════════════════════════════╝\n")
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
