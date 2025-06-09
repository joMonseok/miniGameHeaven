import os
import platform
import threading
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
    screen.print(1,2,"Player 1: [A] / Player 2: [L]")
    screen.print(1,3,"Press the keys quickly to defeat your opponent!")
    screen.print(0,5, str)
    screen.refresh()


# 플레이어 입력 감지
def player_listener(player_key, direction):
    global position, game_over
    while not game_over:
        key = screen.getKey()
        if key == player_key:
            position += direction
            draw()
            if position <= 0:
                print()
                print("\n🎉 Player 1 Wins!")
                game_over = True
            elif position >= WIDTH - 1:
                print()
                print("\n🎉 Player 2 Wins!")
                game_over = True

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
    y=2
    for mainScreenLine in mainScreenLines:
        screen.print(0,y,mainScreenLine)
        y=y+1
    y=y+2
    screen.print(27,y,"Press Any Key to Start the Game")
    screen.refresh()
    start = ''
    key=screen.getKey()
    if start == '':
        screen.clearScreen()
        screen.print(1,2, "╔════════════════════════════════════════════════════════════════════╗\n")
        screen.print(1,3, "║                         🕹️  How to play guide                      ║\n")
        screen.print(1,4, "╠════════════════════════════════════════════════════════════════════╣\n")
        screen.print(1,5, "║   🔹 It\'s a two-player keyboard combo game.                        ║\n")
        screen.print(1,6, "║                                                                    ║\n")
        screen.print(1,7, "║   🔸 Player 1 : [ A ] Keep hitting the keys!                       ║\n")
        screen.print(1,8, "║   🔸 Player 2 : [ L ] Keep hitting the keys!                       ║\n")
        screen.print(1,9, "║                                                                    ║\n")
        screen.print(1,10,"║   ⏱️ The person who pulls the rope all the way to the end wins!    ║\n")
        screen.print(1,11,"║                                                                    ║\n")
        screen.print(1,12,"║   🚀 When you are ready, press any key to start the game.          ║\n")
        screen.print(1,13,"╚════════════════════════════════════════════════════════════════════╝\n")
        screen.refresh()

        screen.getKey()

        screen.clearScreen()
        draw()

        t1 = threading.Thread(target=player_listener, args=('a', -1))
        t2 = threading.Thread(target=player_listener, args=('l', 1))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    screen.clearScreen()
    screen.print(1,3,"\nGAME OVER!")
    screen.refresh()
    time.sleep(5)  # 5초 대기


if __name__ == "__main__":
    tug_of_war()


def main():
    
    tug_of_war()
