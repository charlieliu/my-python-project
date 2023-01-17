import sys
import pygame

pygame.init()

# 設定視窗
width, height = 640, 480                            # 遊戲畫面寬和高
screen = pygame.display.set_mode((width, height))   # 依設定顯示視窗
pygame.display.set_caption("Sean's game")           # 設定程式標題

'''
建立畫布 background
顏色由 3 個 0 到 255 整數組成 (R,G,B)
(0,0,0)         為黑色
(255,0,0)       為紅色
(0,255,0)       為綠色
(0,0,255)       為藍色
(255,255,0)     為黃色
(0,255,255)     為青綠色
(255,0,255)     為桃紅色
(255,255,255)   為白色
'''
background = pygame.Surface(screen.get_size())  # get_size()取得視窗尺寸
background = background.convert()               # convert()建立副本，加快畫布在視窗顯示速度
background.fill((255,255,255))                  # 白色

# 繪製幾何圖形 - 線寬0為實心
pygame.draw.rect(background, (0,0,255),[70, 70, 500, 60], 4)            # 矩形(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
pygame.draw.rect(background, (255,0,255),[70, 150, 500, 60], 0)
pygame.draw.circle(background, (255,0,0),(100,300), 50, 4)              # 圓形(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
pygame.draw.circle(background, (255,255,0),(100,300), 20, 0)
pygame.draw.ellipse(background, (0,255,0),[200,250, 150, 80], 4)        # 橢圓形(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 線寬)
pygame.draw.ellipse(background, (0,255,255),[265,250, 20, 80], 0)
pygame.draw.arc(background, (0,0,255),[400, 250, 70, 150] ,5 ,1.5 , 4)  # 圓弧形(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 起始角, 結束角, 線寬)
pygame.draw.line(background, (0,0,255),(550,250), (550, 400), 4)        # 直線(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)

# 繪製文字
font = pygame.font.SysFont("simhei", 24)
text = font.render("Hello", True, (255,0,0), (255,255,0))               # 繪製(文字, 平滑值, 文字顏色, 背景顏色)
background.blit(text, (320,240))

# 顯示
screen.blit(background, (0,0))
pygame.display.update()

# 關閉程式的程式碼
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit() 


