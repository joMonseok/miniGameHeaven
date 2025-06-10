import screen
import os
import time
import random
import platform

# 게임 상태
gameIng = True
game_over = False
score = 0

# ASCII 아트 타이틀
TITLE_ART = [
    "██████╗ ██╗███╗   ██╗ ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗",
    "██╔══██╗██║████╗  ██║██╔═══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝",
    "██║  ██║██║██╔██╗ ██║██║   ██║    ██║  ███╗███████║██╔████╔██║█████╗  ",
    "██║  ██║██║██║╚██╗██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ",
    "██████╔╝██║██║ ╚████║╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗",
    "╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"
]

# 공룡 캐릭터 상태
GROUND_Y = 15
dino_x = 5
dino_y = GROUND_Y
is_jumping = False
jump_velocity = 0
GRAVITY = 0.2
JUMP_FORCE = -1.2

# 장애물 관련
obstacles = []
OBSTACLE_TYPES = ['🌵', '🌵🌵']

# 캐릭터와 게임 요소
DINO = '⊇'
GROUND = '═'
EMPTY = ' '

# 플랫폼별 키 입력 모듈
key_input_module = None
old_settings = None

if platform.system() == "Windows":
    import msvcrt
    key_input_module = msvcrt
else:
    # macOS/Linux용 비동기 키 입력을 위한 모듈
    import sys
    import select
    import termios
    import tty

def setup_terminal():
    """macOS/Linux에서 비동기 키 입력을 위한 터미널 설정"""
    global old_settings
    if platform.system() != "Windows":
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin.fileno())

def restore_terminal():
    screen.clearScreen()

def show_title_screen():
    screen.clearScreen()
    
    # 화면 중앙에 타이틀 표시
    screen.draw_centered_menu(TITLE_ART)
    screen.draw_centered_str("Press any key to start...", div=5, loc=3)
    # 시작 안내 메시지
    screen.refresh()

    time.sleep(2)  # 2초 대기
    screen.clearScreen()

def reset_game():
    global gameIng, game_over, score, dino_y, is_jumping, jump_velocity, obstacles
    gameIng = True
    game_over = False
    score = 0
    dino_y = GROUND_Y
    is_jumping = False
    jump_velocity = 0
    obstacles = []

def check_input(key):
    global is_jumping, gameIng, jump_velocity
    
    if key == ' ' and not is_jumping:  # 스페이스바로 점프
        is_jumping = True
        jump_velocity = JUMP_FORCE
    elif key == 'q':  # q로 게임 종료
        screen.reset()
        gameIng = False

def update_game():
    global dino_y, is_jumping, jump_velocity, score, game_over

    # 점프 물리 처리
    if is_jumping:
        # 중력 적용
        jump_velocity += GRAVITY
        
        # 새로운 위치 계산
        new_y = dino_y + jump_velocity
        
        # 바닥 충돌 체크
        if new_y >= GROUND_Y:
            dino_y = GROUND_Y
            is_jumping = False
            jump_velocity = 0
        else:
            dino_y = new_y

    # 장애물 생성
    if random.randint(1, 20) == 1 and len(obstacles) < 3:
        obstacle_type = random.choice(OBSTACLE_TYPES)
        obstacles.append({'x': 80, 'type': obstacle_type})

    # 장애물 이동
    for obstacle in obstacles[:]:
        obstacle['x'] -= 1
        if obstacle['x'] < 0:
            obstacles.remove(obstacle)
            score += 1

    # 충돌 체크
    for obstacle in obstacles:
        if (obstacle['x'] <= dino_x + 1 and 
            obstacle['x'] + len(obstacle['type']) >= dino_x and 
            dino_y + 1 >= GROUND_Y):
            game_over = True
            return

def draw_game():
    
    # 게임 화면 초기화
    game_display = [[EMPTY for _ in range(82)] for _ in range(20)]
    
    # 공룡 그리기
    dino_y_rounded = round(dino_y)  # 실수값을 반올림하여 그리기
    game_display[dino_y_rounded][dino_x] = DINO
    
    # 장애물 그리기
    for obstacle in obstacles:
        x = obstacle['x']
        for i, char in enumerate(obstacle['type']):
            if 0 <= x + i < 82:
                game_display[GROUND_Y][x + i] = char
    
    # 바닥 그리기
    for x in range(82):
        game_display[GROUND_Y + 1][x] = GROUND
    
    # 점수 표시
    score_text = f'score: {score}'
    for i, char in enumerate(score_text):
        game_display[1][70 + i] = char
    
    # 조작법 표시
    controls_text = "spacebar: jump  Q: quit"
    for i, char in enumerate(controls_text):
        game_display[1][2 + i] = char
    
    # 화면 출력
    # y=0
    # for row in game_display:
    #     str= ''.join(row)
    #     screen.print(20, y+10, str)
    #     y=y+1
    #     #print(''.join(row), '\r')
    string_display = [''.join(row) for row in game_display]
    screen.draw_centered_menu(string_display)
    screen.refresh()
    
        
def main():
    global gameIng, game_over
    oneResetChk=True
    try:
        #setup_terminal()  # 터미널 설정
        show_title_screen()  # 타이틀 화면 표시
        reset_game()
        
        screen.getStdscr().nodelay(True) # True로 키 입력 비동기 처리 
        screen.getStdscr().timeout(50)  # 입력 대기 시간 설정 (ms)
        
        while gameIng:
            if not game_over:
                try:
                    key = screen.getKey()
                    check_input(key)  # 키 입력 확인
                except:
                    pass # 입력이 없을 경우 넘어감 

                update_game()  # 게임 상태 업데이트
                draw_game()    # 화면 그리기
            else:
                screen.clear()
                str = [
                    "Game Over!",
                    f"Score: {score}",
                    "Press Q to return to menu..."
                ]
                screen.draw_centered_menu(str)
                screen.refresh()
                try:
                    key = screen.getKey()
                    check_input(key)  # 게임 오버 상태에서 Q 키 입력 대기
                except:
                    pass # 입력이 없을 경우 넘어감 
        
        screen.clearScreen()
        
    finally:
        restore_terminal()  # 터미널 설정 복원

if __name__ == "__main__":
    main() 