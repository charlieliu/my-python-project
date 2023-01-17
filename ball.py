# https://ithelp.ithome.com.tw/articles/10209606
import pygame, random, math

pygame.init()

# 設定視窗背景
width, height = 640, 480                            # 遊戲畫面寬和高
screen = pygame.display.set_mode((width, height))   # 依設定顯示視窗
pygame.display.set_caption("Sean's game")           # 設定程式標題
background = pygame.Surface(screen.get_size())      # get_size()取得視窗尺寸
background = background.convert()                   # convert()建立副本，加快畫布在視窗顯示速度
background.fill((255,255,255))                      # 白色

# 建立藍球
ball = pygame.Surface((70,70))
ball.fill((255,255,255))
pygame.draw.circle(ball, (255,75,0), (35,35), 35, 0)            # 圓形(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
pygame.draw.line(ball, (0,0,0), (35,0), (35,70), 4)             # 直線(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)
pygame.draw.arc(ball, (0,0,0),[0,5,30,60], 5, 1.5, 4)           # 圓弧形(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 起始角, 結束角, 線寬)
pygame.draw.arc(ball, (0,0,0),[45,10,30,60], 1.7, 4, 4)         # 圓弧形(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 起始角, 結束角, 線寬)
rect = ball.get_rect()
rect.center = (random.randint(100,540),random.randint(100,380)) # 球隨機起始位置
x, y = rect.topleft                                             # 球左上角坐標
direction = random.randint(20,70)                               # 起始角度
radian = math.radians(direction )                               # 轉為弳度
dx = 5 * math.cos(radian)                                       # 球水平運動速度
dy = -5 * math.sin(radian)                                      # 球垂直運動速度

# 建立時間元件
clock = pygame.time.Clock()

# 關閉程式的程式碼
running = True
while running:
    clock.tick(30)                                              # 每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += dx                                                     # 改變水平位置
    y += dy                                                     # 改變垂直位置
    rect.center = (x,y)
    if(rect.left <= 0 or rect.right >= screen.get_width()):     # 到達左右邊界
        dx *= -1                                                # 水平速度變號
    elif(rect.top <= 1 or rect.bottom >= screen.get_height()-1):# 到達上下邊界
        dy *= -1                                                # 垂直速度變號
    screen.blit(background, (0,0))
    screen.blit(ball, rect.topleft) 
    pygame.display.update()    
pygame.quit()
