import pygame
from random import*

from pygame.constants import GL_BUFFER_SIZE
#레벨에 맞게 설정
def setup(level):

    #얼마동안 숫자를 보여줄지
    global display_time
    display_time = 5 - (curr_level * 0.1)
    display_time = max(display_time, 1)

    #얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    #실제 화면에 grid형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)

def shuffle_grid(number_count):
    rows = 5
    colums = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for col in range(colums)] for row in range(rows)]

    number = 1 #시작숫자 1부터 number_count 까지
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(colums)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            #현재 grid cell 위치 기준으로 x,y위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            #숫자 버튼 만들기
            button = pygame.Rect(0,0,button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

    #print(grid)

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색으로 동그라미를 그리는데 중심좌표는 start_butten.center이고 
    #반지름은 60, 선 두께는 5

    msg = game_font.render(f"{curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)

    screen.blit(msg, msg_rect)

def display_gmae_screen():
    global hidden, start_ticks

    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # ms > sec
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(number_buttons, start = 1):
        if hidden:
            #사격형 그리기
            pygame.draw.rect(screen, WHITE, rect)
        else:
            #실제 숫자 텍스트
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)

#pos에 해당하는 버튼 
def check_buttons(pos):
    global start, start_ticks

    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):  #start_button안에 들어가있냐
        start = True
        start_ticks = pygame.time.get_ticks() #타이머시작

def check_number_buttons(pos):
    global hidden, start, curr_level

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                #print("Correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                game_over()
            break
    #모든숫자를 맞춰서 길이가 0일때
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

def game_over():
    global running
    running = False

    msg = game_font.render(f"Your level is {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)

#초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) #폰트 정의
#시작버트
start_button = pygame.Rect(0 , 0, 120, 120) #사격형
start_button.center = (120, screen_height - 120)

#색깔
BLACK = (0,0,0) #RGB순서
WHITE = (255, 255, 255)
GRAY = (50,50,50)

number_buttons = [] #플레이어가 눌러야 하는 버튼들
curr_level = 1 #현재레벨
display_time = None #숫자를 보여주는 시간
start_ticks = None #시간계산 (현재 시간 정보를 저장)

#게임시작여부
start = False
hidden = False

#게임시작 전에 게임설정 함수 수행
setup(curr_level)

#게임 루프
running = True #게임이 실행중인가
while running:
    click_pos = None

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가?
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: #사용자가 클릭했을때
            click_pos = pygame.mouse.get_pos() #좌표를 가지고옴
            #print(click_pos)
        elif event.type == pygame.K_ESCAPE:
            running = False
    #화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    if start:
        display_gmae_screen() #게임화면 표시
    else:
        display_start_screen() #시작화면 표시
    #사용자가 클릭한 좌표값이 있다면
    if click_pos:
        check_buttons(click_pos)
    #화면 업데이트
    pygame.display.update()

#ms 단위
pygame.time.delay(2000)

#게임종료
pygame.quit()