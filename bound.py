# https://ithelp.ithome.com.tw/articles/10209606
import random, pygame, random, math

lastMemberId = 0
def getMemberId():
    global lastMemberId
    lastMemberId += 1
    return lastMemberId

pygame.init()

# 設定視窗背景
width, height = 640, 480                            # 遊戲畫面寬和高
screen = pygame.display.set_mode((width, height))   # 依設定顯示視窗
pygame.display.set_caption("Tom and Jerry")         # 設定程式標題
background = pygame.Surface(screen.get_size())      # get_size()取得視窗尺寸
background = background.convert()                   # convert()建立副本，加快畫布在視窗顯示速度
background.fill((255,255,255))                      # 白色

# 建立球體
class circle(pygame.sprite.Sprite):
    id = 0
    x = 0          # 球x坐標
    y = 0          # 球y坐標
    direction = 0  # 球移動方向
    radian = 0
    dx = 0         # x位移量
    dy = 0         # y位移量
    speed = 0      # 球移動速度
    def __init__(self, sp, radium, color, name):
        pygame.sprite.Sprite.__init__(self)
        self.id = getMemberId()
        self.speed = sp
        self.x = random.randint(radium, width-radium)
        self.y = random.randint(radium, height-radium)
        self.radium = radium
        self.image = pygame.Surface([radium*2, radium*2])   # 繪製球體
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()                   # 取得球體區域
        self.rect.center = (self.x, self.y)                 # 初始位置
        self.direction = random.randint(40,70)              # 移動角度
        self.radian = math.radians(self.direction)
        self.dx = self.speed * math.cos(self.radian)        # 球水平運動速度
        self.dy = -self.speed * math.sin(self.radian)       # 球垂直運動速度
        self.name = name
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        screen.blit(self.image, self.rect.topleft)
    # 改變水平位置
    def reboundX(self):
        self.dx *= -1
    # 改變垂直位置
    def reboundY(self):
        self.dy *= -1
    # 球體移動
    def move(self):
        left    = self.rect.left + self.dx
        right   = self.rect.right + self.dx
        top     = self.rect.top + self.dy
        bottom  = self.rect.top + self.dy
        if(left <= 1 or right >= width):   # 到達左右邊界
            self.reboundX()
        if(top <= 1 or bottom >= height):  # 到達上下邊界
            self.reboundY()
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect.topleft)
    # 碰撞事件
    def bound(self, item):
        x = abs(self.x - item.x)
        y = abs(self.y - item.y)
        distance = math.sqrt(x * x + y * y)
        radium = self.radium + item.radium
        if distance > radium:
            return # 無碰撞ß
        print('rebound', x, y, distance, radium)
        bound = False 
        if (self.dx * item.dx) <= 0:
            self.reboundX()
            item.reboundX()
            bound = True
        if (self.dy * item.dy) <= 0:
            self.reboundY()
            item.reboundX()
            bound = True
        if bound == True:
            self.move()
            item.move()
    def update(self):
        self.move()

class area:
    members = []
    balls = pygame.sprite.Group()
    def __init__(self):
        density = 160 * 120                         # 障礙物密度
        obstacles = round(width * height / density) # 障礙物個數
        self.addObstacles(obstacles)
    # 新增障礙物
    def addObstacles(self, obstacles):
        for i in range(obstacles):
            item = circle(0, 10, (0,255,20), 'Tree_'+str(i))
            self.add(item)
    def add(self, member):
        self.members.append(member)
        self.balls.add(member)
    def update(self):
        screen.blit(background, (0,0)) #清除繪圖視窗
        for member in self.members:
            member.update()
        self.checkBound()
    def checkBound(self):
        for item1 in self.members:
            for item2 in self.members:
                if item1 != item2:
                    item1.bound(item2)

# 建立全部角色群組
farm = area()
Tom = circle(10, 10, (255,0,0), 'Tom')
farm.add(Tom)
Jerry = circle(20, 10, (0,0,255), 'Jerry')
farm.add(Jerry)

# 建立時間元件
clock = pygame.time.Clock()

# 關閉程式的程式碼
running = True
while running:
    clock.tick(30) # 每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    farm.update()
    pygame.display.update()
pygame.quit()