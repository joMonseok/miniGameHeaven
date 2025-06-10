import screen
from copy import deepcopy
import curses

map1 =[
        ['┌','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┬','─','┐'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['├','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┼','─','┤'],
        ['└','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┴','─','┘']
    ]
#화면 그리기용
map2 = [[0 for _ in range(29)] for _ in range(29)]#가중치 저장용
black=1#검정돌
white=2#하얀돌
dol = black


cursor_x, cursor_y = 1, 1# 커서 위치
dolx, doly = 5, 5# 실제 맵에 연결 될 커서
gameIng = True#플레이 중 체크
winDolChk=0# 어떤 돌이 이겼는지 비교용

PC_PLAY = 0#1인 플레이 모드
TWO_PLAY=1#2인 플레이 모드
mode = 0



class pc:
    map=[]

    # 방어 (defense)
    defenseLevelOne = -1             # 한 칸만 있을 때
    defenseLevelTwo_oneBlock = -5    # 양쪽이 막힌 두 칸
    defenseLevelTwo = -10            # 열린 두 칸(양방)
    defenseLevelTwo_center = -12
    defenseLevelThree_oneBlock = -50 # 양쪽이 막힌 세 칸
    defenseLevelThree = -100         # 열린 세 칸(양방)
    defenseLevelThree_center = -120
    defenseLevelFour_oneBlock = -300 # 막힌 4(즉시 막아야함)
    defenseLevelFour = -500         # 열린 4(즉사, 반드시 막아야함)

    # 공격 (attack)
    attackLevelOne = -1
    attackLevelTwo_oneBlock = -3
    attackLevelTwo = -8
    attackLevelTwo_center = -10
    attackLevelThree_oneBlock = -30
    attackLevelThree = -70
    attackLevelThree_center = -90
    attackLevelFour_oneBlock = -700
    attackLevelFour = -800           # 열린4, 즉시승리 가능
    
    dolMin=0#가장 가중치가 변화된 값을 체크하기 위한 변수
    setDolX=0
    setDolY=0
    dol = white
    rival = black
    

    def __init__(self,mapchk):
        self.map=deepcopy(mapchk)

    def setMyDol(self, dol):#pc용 돌 설정(검흰)
        self.dol=dol
        if dol==black:
            self.rival=white
        elif dol==white:
            self.rival=black

    def weightChk(self,mapchk):#가중치 측정
        global winDolChk
        directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),  # 오른쪽, 왼쪽, 아래, 위
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # 우하단, 좌하단, 우상단, 좌상단
        ]

        self.map = deepcopy(mapchk)
        for y in range(5,24,1):
            for x in range(5,24,1):
                for dy,dx in directions:
                    if self.map[y][x]==self.rival:
                        if self.map[y][x]==self.rival and self.map[y+dy][x+dx]==self.rival:
                            if self.map[y+dy*2][x+dx*2]==self.rival:
                                if self.map[y+dy*3][x+dx*3]==self.rival:
                                    #four
                                    if self.map[y+dy*4][x+dx*4]>0:
                                        if self.map[y-dy][x-dx]<0:
                                            self.map[y-dy][x-dx]+=self.defenseLevelFour_oneBlock
                                    elif self.map[y-dy][x-dx]>0:
                                        if self.map[y+dy*4][x+dx*4]<0:
                                            self.map[y+dy*4][x+dx*4]+=self.defenseLevelFour_oneBlock
                                    else:
                                        self.map[y+dy*4][x+dx*4]+=self.defenseLevelFour
                                        self.map[y-dy][x-dx]+=self.defenseLevelFour
                                    
                                else:
                                    #three
                                    if self.map[y+dy*3][x+dx*3]>0:
                                        if self.map[y-dy][x-dx]<0:
                                            self.map[y-dy][x-dx]+=self.defenseLevelThree_oneBlock
                                    elif self.map[y-dy][x-dx]>0:
                                        if self.map[y+dy*3][x+dx*3]<0:
                                            self.map[y+dy*3][x+dx*3]+=self.defenseLevelThree_oneBlock
                                    else:
                                        self.map[y+dy*3][x+dx*3]+=self.defenseLevelThree
                                        self.map[y-dy][x-dx]+=self.defenseLevelThree
                            else:
                                #two
                                if self.map[y+dy*2][x+dx*2]>0:
                                    if self.map[y-dy][x-dx]<0:
                                        self.map[y-dy][x-dx]+=self.defenseLevelTwo_oneBlock
                                elif self.map[y-dy][x-dx]>0:
                                    if self.map[y+dy*2][x+dx*2]<0:
                                        self.map[y+dy*2][x+dx*2]+=self.defenseLevelTwo_oneBlock
                                else:
                                    self.map[y+dy*2][x+dx*2]+=self.defenseLevelTwo
                                    self.map[y-dy][x-dx]+=self.defenseLevelTwo
                        else:
                            #one
                                if self.map[y+dy][x+dx]<1:
                                    self.map[y+dy][x+dx]+=self.defenseLevelOne
                        if self.map[y+dy][x+dx]==self.rival and self.map[y+dy*2][x+dx*2]<1 and self.map[y+dy*3][x+dx*3]==self.rival:
                            self.map[y+dy*2][x+dx*2] += self.defenseLevelThree_center
                        elif  self.map[y+dy][x+dx]<1 and self.map[y+dy*2][x+dx*2]==self.rival and self.map[y+dy*3][x+dx*3]==self.rival:
                            self.map[y+dy][x+dx] += self.defenseLevelThree_center
                        elif self.map[y+dy][x+dx]<1 and self.map[y+dy*2][x+dx*2]==self.rival:
                            self.map[y+dy][x+dx] += self.defenseLevelTwo_center
                    
                    elif self.map[y][x]==self.dol:
                        if self.map[y][x]==self.dol and self.map[y+dy][x+dx]==self.dol:
                            if self.map[y+dy*2][x+dx*2]==self.dol:
                                if self.map[y+dy*3][x+dx*3]==self.dol:
                                    #four
                                    if self.map[y+dy*4][x+dx*4]>0:
                                        if self.map[y-dy][x-dx]<0:
                                            self.map[y-dy][x-dx]+=self.attackLevelFour_oneBlock
                                    elif self.map[y-dy][x-dx]>0:
                                        if self.map[y+dy*4][x+dx*4]<0:
                                            self.map[y+dy*4][x+dx*4]+=self.attackLevelFour_oneBlock
                                    else:
                                        self.map[y+dy*4][x+dx*4]+=self.attackLevelFour
                                        self.map[y-dy][x-dx]+=self.attackLevelFour
                                    
                                else:
                                    #three
                                    if self.map[y+dy*3][x+dx*3]>0:
                                        if self.map[y-dy][x-dx]<0:
                                            self.map[y-dy][x-dx]+=self.attackLevelThree_oneBlock
                                    elif self.map[y-dy][x-dx]>0:
                                        if self.map[y+dy*3][x+dx*3]<0:
                                            self.map[y+dy*3][x+dx*3]+=self.attackLevelThree_oneBlock
                                    else:
                                        self.map[y+dy*3][x+dx*3]+=self.attackLevelThree
                                        self.map[y-dy][x-dx]+=self.attackLevelThree
                            else:
                                #two
                                if self.map[y+dy*2][x+dx*2]>0:
                                    if self.map[y-dy][x-dx]<0:
                                        self.map[y-dy][x-dx]+=self.attackLevelTwo_oneBlock
                                elif self.map[y-dy][x-dx]>0:
                                    if self.map[y+dy*2][x+dx*2]<0:
                                        self.map[y+dy*2][x+dx*2]+=self.attackLevelTwo_oneBlock
                                else:
                                    self.map[y+dy*2][x+dx*2]+=self.attackLevelTwo
                                    self.map[y-dy][x-dx]+=self.attackLevelTwo
                        else:
                            #one
                                if self.map[y+dy][x+dx]<1:
                                    self.map[y+dy][x+dx]+=self.attackLevelOne
                        if self.map[y+dy][x+dx]==self.dol and self.map[y+dy*2][x+dx*2]<1 and self.map[y+dy*3][x+dx*3]==self.dol:
                            self.map[y+dy*2][x+dx*2] += self.attackLevelThree_center
                        elif  self.map[y+dy][x+dx]<1 and self.map[y+dy*2][x+dx*2]==self.dol and self.map[y+dy*3][x+dx*3]==self.dol:
                            self.map[y+dy][x+dx] += self.attackLevelThree_center
                        elif self.map[y+dy][x+dx]<1 and self.map[y+dy*2][x+dx*2]==self.dol:
                            self.map[y+dy][x+dx] += self.attackLevelTwo_center
        
        for y in range(0,29,1):
            for x in range(0,29,1):
                if self.map[y][x]<self.dolMin:
                    self.dolMin = self.map[y][x]
                    self.setDolX=x
                    self.setDolY=y
        self.dolMin=0
    
    def setDol(self):#커서에 돌 두기
        global map2
        map2[self.setDolY][self.setDolX] = self.dol                   
    
    def showMap(self):#맵 그리기(디버깅용)
        for i in range(0,29,1):
            for j in range(0,29,1):
                print(self.map[i][j],end=' ')
            print("\r")

                    

ai = pc(map2)



def on_press():#키 입력
    global cursor_x, cursor_y, doly, dolx, dol, gameIng, winDolChk
    key = screen.getRowKey()  # 키 입력 대기 (1byte 입력받기)
    # 전역 변수 사용
    if key == 'w':  # W: 위로 이동
        cursor_y = max(1, cursor_y - 1)  # 위쪽 경계값 제한
        doly = max(5, doly - 1)
    elif key == 's':  # S: 아래로 이동
        cursor_y = min(19, cursor_y + 1)  # 아래쪽 경계값 제한
        doly = min(23, doly + 1) 
    elif key == 'a':  # A: 왼쪽으로 이동
        cursor_x = max(1, cursor_x - 2)  # 왼쪽 경계값 제한
        dolx = max(5, dolx - 1) 
    elif key == 'd':  # D: 오른쪽으로 이동
        cursor_x = min(37, cursor_x + 2)  # 오른쪽 경계값 제한
        dolx = min(23, dolx + 1) 
    elif key == '\n': # 돌 두기
        if map2[doly][dolx]==0:#돌이 비워져 있으면 돌 두기
            map2[doly][dolx] = dol
            if winChk(dolx,doly,dol):#이겼는지 체크
                gameIng=False
                winDolChk = dol
                return
            elif mode == TWO_PLAY:#2인 플레이면 돌만 바꾸어서 코드 진행
                if dol==black:
                    dol=white
                else:
                    dol=black
            elif mode == PC_PLAY:#1인 플레이면 pc가 플레이
                ai.weightChk(map2)
                ai.setDol()
                if winChk(ai.setDolX,ai.setDolY,ai.dol):
                    gameIng=False
                    winDolChk = ai.dol


#이겼는지 확인
def winChk(x,y,dol):
    #각 방향 돌 몇개있는지 체크용
    right=0
    left=0
    up=0
    down=0
    riup=0
    rido=0
    leup=0
    ledo=0

    #재귀함수로 체크
    right = chkDol(x+1,y,1,0,dol,right)
    left = chkDol(x-1,y,-1,0,dol,left)
    up = chkDol(x,y-1,0,-1,dol,up)
    down = chkDol(x,y+1,0,1,dol,down)
    riup = chkDol(x+1,y-1,1,-1,dol,riup)
    rido = chkDol(x+1,y+1,1,1,dol,rido)
    leup = chkDol(x-1,y-1,-1,-1,dol,leup)
    ledo = chkDol(x-1,y+1,-1,1,dol,ledo)
    
    #각 방향 양쪽으로 더해서 5 이상이면 승리로 체크
    if right + left + 1 > 4:
        return True
    elif up + down + 1 >4:
        return True 
    elif riup + ledo + 1 >4:
        return True
    elif rido + leup + 1 >4:
        return True
    return False
#연결된 돌 찾는 함수
def chkDol(x,y,plusX,plusY,dol,wei):
    if map2[y][x]==dol:
        wei = chkDol(x+plusX,y+plusY,plusX,plusY,dol,wei+1)
    return wei
#오목 판 그리기
drawMapY=0
def drawMap(div=2,loc=1):
    longest = 37
    h, w = screen.getmaxyx()  # 현재 터미널의 높이와 너비를 가져옴
    n_lines = 19
    n_cols = longest
    start_y = (h//div) * loc - (n_lines // 2)
    start_x = (w - n_cols) // 2
    y=11
    for i in range(0,19,1):
        j2=0
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        for j in range(0,37,1):
            startStr = ""
            str = ""
            lastStr = ""
            color = 0
            if i==cursor_y-1 and j==cursor_x-1:
                color=1
            if j%2==0:
                if map2[i+5][j2+5]!=0:
                    if map2[i+5][j2+5]==black:
                        str='○'
                    elif map2[i+5][j2+5]==white:
                        str='●'
                else:
                    str=map1[i][j]
                j2=j2+1
            else:
                str = map1[i][j]
            startStr= ""+startStr+str+lastStr
            screen.printColor(start_x+j,i+start_y,startStr,color)
            y=y+1

setPlayModeIng = True
setDolIng=True
#메뉴 키 입력
def on_press_menu():
    global cursor_y, dol, setDolIng,setPlayModeIng
    key = screen.getRowKey()  # 키 입력 대기 (1byte 입력받기)
    # 전역 변수 사용
    if key == 'w':  # W: 위로 이동
        cursor_y = 1
    elif key == 's':  # S: 아래로 이동
        cursor_y = 2
    elif key == '\n':
        if mode == PC_PLAY:
            if cursor_y==1:
                dol = black
                ai.setMyDol(white)
            elif cursor_y==2:
                dol = white
                ai.setMyDol(black)
        else:
            dol = black
        setDolIng=False
        setPlayModeIng=False
        
drawMainMenuLines = [
    "╔═══════════════════════════════════════════════════════════════════════════╗",
    "║                                                                           ║",
    "║               ██████╗ ███╗   ███╗ ██████╗  ██████╗ ██╗  ██╗               ║",
    "║              ██╔═══██╗████╗ ████║██╔═══██╗██╔═══██╗██║ ██╔╝               ║",
    "║              ██║   ██║██╔████╔██║██║   ██║██║   ██║█████╔╝                ║",
    "║              ██║   ██║██║╚██╔╝██║██║   ██║██║   ██║██╔═██╗                ║",
    "║              ╚██████╔╝██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║  ██╗               ║",
    "║               ╚═════╝ ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝               ║",
    "║                                                                           ║",
    "║                                                                           ║",
    "║                                                                           ║",
    "║                                                                           ║",
    "║                     move : wasd   │   select : enter                      ║",
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
    "╚═══════════════════════════════════════════════════════════════════════════╝"
]
#기본 화면
def drawMenu():
    screen.draw_centered_menu(drawMainMenuLines)

whiteWinStr = [
    "    ██     ██ ██    ██ ██████ ████████ ██████",
    "    ██     ██ ██    ██   ██      ██    ██    ",
    "    ██  █  ██ ████████   ██      ██    ██████",
    "    ██ ███ ██ ██    ██   ██      ██    ██    ",
    "     ███ ███  ██    ██ ██████    ██    ██████",
    "                                             ",
    "                ██████ ██ ██ ████            "
]
blackWinStr = [
    "    ██████  ██      █████   ██████  ██   ██",
    "    ██   ██ ██     ██   ██ ██       ██  ██ ",
    "    ██████  ██     ███████ ██       █████  ",
    "    ██   ██ ██     ██   ██ ██       ██  ██ ",
    "    ██████  ██████ ██   ██  ██████  ██   ██",
    "                                           ",
    "                ██████ ██ ██ ████          "
]

setDolMenuStr = [
    "1. Black Dol",
    "2. White Dol"
]
setPlayModeMenuStr = [
    "1. one Person Play",
    "2. two Person Play"
]

def drawDolMenu():
    screen.draw_centered_menuCommand(setDolMenuStr,5,3, cursor_y-1)

def drawPlayModeMenu():
    screen.draw_centered_menuCommand(setPlayModeMenuStr,5,3, cursor_y-1)

#사용할 돌 선택
def drawSetDolMenu():
    global setDolIng
    screen.clearScreen()
    setDolIng=True
    drawMenu()
    while setDolIng:
        drawDolMenu()
        on_press_menu()
    screen.clearScreen()

#1인모드 2인보드 선택
def drawSetPlayModeMenu():
    global cursor_y, setPlayModeIng,mode
    screen.clearScreen()
    setPlayModeIng=True
    drawMenu()
    while setPlayModeIng:
        drawPlayModeMenu()
        on_press_menu()
    mode = cursor_y-1
    cursor_y=1
    screen.clearScreen()


def main():
    global gameIng, dolx, doly, cursor_x, cursor_y, dol, drawMapY
    
    cursor_x, cursor_y = 1, 1
    dolx, doly = 5, 5
    for i in range(0,29,1):#맵 초기화
        for j in range(0,29,1):
            map2[i][j]=0
    for i in range(0,29,1):#맵초기화
        for j in range(0,5,1):
            map2[i][j]=3
            map2[j][i]=3
            map2[i][24+j]=3
            map2[24+j][i]=3

    #모드 및 돌 선택
    drawSetPlayModeMenu()
    if mode == PC_PLAY:
        drawSetDolMenu()  
        if(dol==white):
            map2[14][14]=black
    else:
        dol = black

    #오목 시작
    drawMap()
    while gameIng:
        on_press()
        drawMap()
        screen.refresh()
        #ai.showMap()
    screen.clearScreen()
    drawMapY=14
    drawMap(5,3)
    if winDolChk==white:
        screen.draw_centered_menuCommand(whiteWinStr, 20,3)
    else:
        screen.draw_centered_menuCommand(blackWinStr, 20,3)
    screen.refresh()
    on_press()
    gameIng = True
    drawMapY=0
    screen.clearScreen()
