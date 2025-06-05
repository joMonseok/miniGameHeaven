import os
import platform
import sys
import threading


# 플랫폼별 키 입력 처리
if os.name == 'nt':
    import msvcrt

    def get_key():
        return msvcrt.getch().decode('utf-8').lower()

else:
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

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
    print('\r' + ''.join(bar), end='', flush=True)


# 플레이어 입력 감지
def player_listener(player_key, direction):
    global position, game_over
    while not game_over:
        key = get_key()
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


def tug_of_war():
    global position, game_over
    clear()
    print("\r")
    print("\r")
    print(" ________  __    __   ______          ______   ________        __       __   ______   _______  \r")
    print("/        |/  |  /  | /      \        /      \ /        |      /  |  _  /  | /      \ /       \ \r")
    print("$$$$$$$$/ $$ |  $$ |/$$$$$$  |      /$$$$$$  |$$$$$$$$/       $$ | / \ $$ |/$$$$$$  |$$$$$$$  |\r")
    print("   $$ |   $$ |  $$ |$$ | _$$/       $$ |  $$ |$$ |__          $$ |/$  \$$ |$$ |__$$ |$$ |__$$ |\r")
    print("   $$ |   $$ |  $$ |$$ |/    |      $$ |  $$ |$$    |         $$ /$$$  $$ |$$    $$ |$$    $$< \r")
    print("   $$ |   $$ |  $$ |$$ |$$$$ |      $$ |  $$ |$$$$$/          $$ $$/$$ $$ |$$$$$$$$ |$$$$$$$  |\r")
    print("   $$ |   $$ \__$$ |$$ \__$$ |      $$ \__$$ |$$ |            $$$$/  $$$$ |$$ |  $$ |$$ |  $$ |\r")
    print("   $$ |   $$    $$/ $$    $$/       $$    $$/ $$ |            $$$/    $$$ |$$ |  $$ |$$ |  $$ |\r")
    print("   $$/     $$$$$$/   $$$$$$/         $$$$$$/  $$/             $$/      $$/ $$/   $$/ $$/   $$/ \r")
    print("                                                                                                 \r")                                                                                   
    print("    \r")
    print("" + " " * 27 + "Press Any Key to Start the Game")
    start = ''
    key=get_key()
    if start == '':
        clear()

        print("╔════════════════════════════════════════════════════════╗\r")
        print("║                    🕹️  게임 방법 안내                   ║\r")
        print("╠════════════════════════════════════════════════════════╣\r")
        print("║   🔹 2인용 키보드 연타 게임입니다.                     ║\r")
        print("║                                                        ║\r")
        print("║   🔸 Player 1 : [ A ] 키를 연타하세요!                 ║\r")
        print("║   🔸 Player 2 : [ L ] 키를 연타하세요!                 ║\r")
        print("║                                                        ║\r")
        print("║   ⏱️ 줄을 끝까지 당겨오는 사람이 승리합니다!            ║\r")
        print("║                                                        ║\r")
        print("║   🚀 준비되었다면 아무 키를 눌러 게임을 시작하세요. ║\r")
        print("╚════════════════════════════════════════════════════════╝\r")
        
        get_key()
        clear()

        print("Player 1: [A]키 / Player 2: [L]키\r\n")
        print("빠르게 키를 눌러 상대편을 이겨보세요!\r\n")

        draw()

        t1 = threading.Thread(target=player_listener, args=('a', -1))
        t2 = threading.Thread(target=player_listener, args=('l', 1))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    print("\n게임 종료!")


if __name__ == "__main__":
    tug_of_war()


def main():
    
    tug_of_war()
