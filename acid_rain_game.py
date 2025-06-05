import random
import time
import threading
import os
import sys

#윈도우에서 curses 모듈이 없으면 설치
try:
    import curses
except ImportError:
    if sys.platform == "win32":
        os.system("pip install windows-curses")
        import curses
    else:
        raise

# 떨어질 단어 리스트 
WORDS = ["break", "elif", "continue", "python", "True", "False", "None", "and", "as"
         , "class", "def", "else", "for", "from", "global", "import", "not", "or"
         , "print", "in", "while", "except", "pass", "exec", "assert", "finally"
         , "raise", "if", "return", "del", "try", "is", "with"]
TICK_RATE = 0.7  # 단어가 떨어지는 속도 (초)
MAX_LIVES = 5    # 목숨 개수 

# 단어 객체 클래스 
class Word:
    def __init__(self, text, x):
        self.text = text # 단어 내용 
        self.x = x # 가로 
        self.y = 0 # 세로 (초기에는 맨 위) 

# 게임 화면 그리기 
def draw_game(stdscr, falling_words, typed_word, score, lives):
    stdscr.clear()  # 화면 초기화 
    height, width = stdscr.getmaxyx() # 현재 터미널 크기 가져오기 

    # 떨어지는 단어 출력 
    for word in falling_words:
        if 0 <= word.y < height:
            stdscr.addstr(word.y, word.x, word.text)

    # 입력창, 점수, 목숨 정보 출력
    stdscr.addstr(height - 3, 0, f"-----------------------------------")
    stdscr.addstr(height - 2, 0, f"Your Input: {typed_word}")
    stdscr.addstr(height - 1, 0, f"Score: {score}  Lives: {lives}")
    stdscr.refresh()

# 게임의 메인 함수 
def game(stdscr):
    curses.curs_set(0)   # 커서 숨김 
    stdscr.nodelay(True) # True로 키 입력 비동기 처리 
    stdscr.timeout(100)  # 입력 대기 시간 설정 (ms)

    falling_words = []   # 화면에 떨어지고 있는 단어 리스트 
    typed_word = ""      # 사용자가 입력한 단어 
    score = 0            # 점수 
    lives = MAX_LIVES    # 목숨 

    last_spawn_time = time.time() # 마지막 단어 생성 시간 

    while True:
        now = time.time()
        if now - last_spawn_time > TICK_RATE:
            # 새 단어 생성 
            text = random.choice(WORDS)
            x = random.randint(0, max(0, curses.COLS - len(text))) # 랜덤 
            falling_words.append(Word(text, x))
            last_spawn_time = now

            # 모든 단어들 한 칸씩 아래로 내려주기  
            for word in falling_words:
                word.y += 1

            # 화면 아래에 닿은 단어 제거 후 목숨 감소 
            for word in falling_words:
                if word.y >= curses.LINES - 3:
                    lives -= 1
                    falling_words.remove(word)

        # 사용자 입력 처리 부분  
        try:
            key = stdscr.getkey()
            if key == '\n': # 엔터 클릭 시 
                matched = False
                for word in falling_words:
                    if word.text == typed_word:
                        falling_words.remove(word)
                        score += 1
                        matched = True
                        break
                typed_word = "" # 입력 초기화 
            elif key in ('KEY_BACKSPACE', '\b', '\x7f'): # 백스페이스 처리 
                typed_word = typed_word[:-1]
            elif len(key) == 1 and key.isprintable(): # 일반 문자 입력 
                typed_word += key
        except:
            pass # 입력이 없을 경우 넘어감 

        draw_game(stdscr, falling_words, typed_word, score, lives) # 화면 갱신 

        if lives <= 0:
            # 게임 종료 처리 
            stdscr.clear()
            stdscr.nodelay(False)
            stdscr.timeout(-1)
            # 게임 종료 후 화면 그리기 
            height, width = stdscr.getmaxyx()
            stdscr.addstr(height // 2, width // 2 - 5, "Game Over!")
            stdscr.addstr(height // 2 + 1, width // 2 - 10, f"Your Score: {score}")
            stdscr.addstr(height // 2 + 2, width // 2 - 10, "Press ESC key to exit.")

            stdscr.refresh()

            # ESC 키 입력까지 대기 
            while True:
                key = stdscr.getch()
                if key == 27: # ESC 키
                    curses.endwin()
                    curses.initscr()
                    return


def main():
    curses.wrapper(game)
def main(std):
    game(std)