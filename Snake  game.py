import pygame
import random

pygame.init()
pygame.mixer.init()

screen_width=900
screen_height=900
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("snake game")
carImg=pygame.image.load("C:\\Users\\VENKATESH JACKIE\\OneDrive\\Desktop\\a.png")
overImg=pygame.image.load("C:\\Users\\VENKATESH JACKIE\\OneDrive\Desktop\\s.gif")
welcome=pygame.image.load("C:\\Users\\VENKATESH JACKIE\\OneDrive\\Desktop\\w.jpg")

green=(0,50,35)
start_on=True

def start_game():
    pygame.mixer.music.load('')
    pygame.mixer.music.play(50)

    exit_game=False
    game_over=False
    FPS=60
    snake_width=20
    snake_x=100
    snake_y=100
    snake_mv='r'
    food_pos=(random.randint(1,860), random.randint(70,860))
    head=[[snake_x,snake_y]]
    snake_len=1
    clock=pygame.time.Clock()
    font=pygame.font.SysFont("Snake Chan",29)
    font2=pygame.font.Sysfont("Snake Chan",45)
    return exit_game,game_over,snake_x,snake_y,snake_width,FPS,snake_mv,food_pos,head,snake_len,clock,font,font2
exit_game,game_over,snake_x,snake_y,snake_width,FPS,snake_mv,food_pos,head,snake_len,clock,font,font2=start_game()

def plot_snake(gameWindow,head,snake_width):
    pygame.draw.circle(gameWindow,green,[head[-1][0] + snake_width//2, head[-1][1] + snake_width//2], snake_width//2 + 1)
    if snake_len//3 < snake_width//2:
        for i in range(0,len(head)//3):
            pygame.draw.circle(gameWindow, green, [head[i][0] + snake_width // 2, head[i][1] + snake_width // 2],snake_width // 2 + i - snake_len//3)
        for i in head[len(head)//3:-1]:
            pygame.draw.circle(gameWindow, green, [i[0] + snake_width // 2, i[1] + snake_width//2],snake_width//2)
    else:
        for i in range(0,snake_width//2):
            pygame.draw.circle(gameWindow, green, [head[i][0] + snake_width // 2, head[i][1] + snake_width // 2],
                               snake_width // 2 + i - snake_len // 3)
            for i in head[len(head) // 3:-1]:
                pygame.draw.circle(gameWindow, green, [i[0] + snake_width // 2, i[1] + snake_width // 2],
                                   snake_width // 2)

def put_text(text,color,x,y,font):
    text_screen= font.render(text,True,color)
    gameWindow.blit(text_screen, [x,y])
sound1=pygame.mixer.sound('')
with open("high_score.txt",'r') as f:
    high_score+int(f.read())
while not exit_game:
    while start_on:
        gameWindow.blit(welcome,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.type==pygame.K_RETURN:
                    start_on=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT and snake_mv != 'l':
                snake_mv='r'
            elif event.key==pygame.K_LEFT and snake_mv != 'r':
                snake_mv='l'
            elif event.key==pygame.K_UP and snake_mv != 'd':
                snake_mv='u'
            elif event.key==pygame.K_DOWN and snake_mv != 'u':
                snake_mv='d'

    if snake_mv == 'r':
        snake_x += 4
    elif  snake_mv == 'l':
        snake_x += 4
    elif  snake_mv == 'u':
        snake_x += 4
    elif  snake_mv == 'd':
        snake_x += 4

    if snake_x in range(food_pos[0],food_pos[0]+40) and snake_y in range(food_pos[1],food_pos[1]+40):


