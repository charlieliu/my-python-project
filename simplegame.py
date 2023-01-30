# https://www.pygame.org/docs/ref/key.html
# https://realpython.com/pygame-a-primer/#basic-game-design
# https://medium.com/python-pandemonium/python-rpg-game-part-1-2468ed8f58ea
# https://ithelp.ithome.com.tw/articles/10209660
import random, pygame, random, math
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

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

class Chess(pygame.sprite.Sprite):
    id = 0
    x = 0
    y = 0
    dx = 0
    dy = 0
    radium = 10
    name = ''
    health = 10
    attack = 10
    luck = 10
    ranged = 10
    defence = 10
    magic = 10
    def __init__(self, name, color=(0,0,0), radium=10):
        pygame.sprite.Sprite.__init__(self)
        self.id = getMemberId()
        self.name = name
        self.radium = radium
        self.x = random.randint(self.radium, width-self.radium)
        self.y = random.randint(self.radium, height-self.radium)
        self.image = pygame.Surface([radium*2, radium*2])   # 繪製球體
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()                   # 取得球體區域
        self.rect.center = (self.x, self.y)                 # 初始位置
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        screen.blit(self.image, self.rect.topleft)
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        left    = self.rect.left + (dx * self.radium)
        right   = self.rect.right + (dx * self.radium)
        top     = self.rect.top + (dy * self.radium)
        bottom  = self.rect.top + (dy * self.radium)
        # 到達左右邊界
        if left <= self.radium:
            self.x = self.radium
        elif right >= width:
            self.x = (width - self.radium)
        else:
            self.x += (dx * self.radium)
        # 到達上下邊界
        if top <= 1:
            self.y = self.radium
        elif bottom >= height:
            self.y += (height - self.radium)
        else:
            self.y += (dy * self.radium)
        self.rect.center = (self.x, self.y)
    def update(self):
        screen.blit(self.image, self.rect.topleft)
    def rebound(self):
        self.dx *= -1
        self.dy *= -1
        self.move(self.dx, self.dy)
    # 碰撞事件
    def bound(self, item):
        x = abs(self.x - item.x)
        y = abs(self.y - item.y)
        distance = math.sqrt(x * x + y * y)
        radium = self.radium + item.radium
        if distance > radium:
            return False # 無碰撞
        print('Before self', 'name:', self.name, 'health:', self.health, 'defence:', self.defence, 'attack:', self.attack)
        print('Before item', 'name:', item.name, 'health:', item.health, 'defence:', item.defence, 'attack:', item.attack)
        if (item.attack - self.defence) > 0:
            self.health -= (item.attack - self.defence)
        if self.health <= 0:
            self.health = 0
            self.image.fill((0,0,0))
        if (self.attack - item.defence) > 0:
            item.health -= (self.attack - item.defence)
        if item.health <= 0:
            item.health = 0
            item.image.fill((0,0,0))
        print('After self', 'name:', self.name, 'health:', self.health, 'defence:', self.defence, 'attack:', self.attack)
        print('After item', 'name:', item.name, 'health:', item.health, 'defence:', item.defence, 'attack:', item.attack)
        return True
    # we're gonna get setters and getters
    # These are getters, where we can check the health or attack of the character
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getLuck(self):
        return self.luck
    def getRanged(self):
        return self.ranged
    def getDefence(self):
        return self.defence
    def getMagic(self):
        return self.magic
    def getName(self):
        return self.name
    # setters is what we can use to change a variable
    # for example if we want to set a new attack value
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setLuck(self, newLuck):
        self.luck = newLuck
    def setRanged(self, newRanged):
        self.ranged = newRanged
    def setDefence(self, newDefence):
        self.defence = newDefence
    def setMagic(self, newMagic):
        self.magic = newMagic
    
    
class Hero(Chess):
    def __init__(self, name):
        super().__init__(name, (0,0,255)) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.health = 100
        self.attack = random.randint(1,100)
        self.luck = random.randint(1,100)
        self.ranged = random.randint(1,100)
        self.defence = random.randint(1,100)
        self.magic = random.randint(1,100)
        
class Enemy(Chess):
    def __init__(self):
        super().__init__('ememy', (255,0,0))
        self.name = 'ememy_' + str(self.id)
        
class area:
    members = []
    balls = pygame.sprite.Group()
    def __init__(self):
        pass
    def add(self, member):
        self.members.append(member)
        self.balls.add(member)
    def update(self):
        screen.blit(background, (0,0)) # 清除繪圖視窗
        for member in self.members:
            member.update()
        pygame.display.update()
        self.checkBound()
    def checkBound(self):
        activity = []
        for item1 in self.members:
            if item1.id in activity:
                print('exist', item1.id)
            else:
                for item2 in self.members:
                    if item2.id in activity:
                        print('exist', item2.id)
                    elif item1 != item2 and item1.bound(item2):
                        activity.append(item1.id)
                        activity.append(item2.id)
                        item1.rebound()
                        item2.rebound()
        pygame.display.update()

maze = area()

Player = Hero('Tom')
maze.add(Player)

ememies = pygame.sprite.Group()
for i in range(10):
    ememy = Enemy()
    ememy.update()
    ememies.add(ememy)
    maze.add(ememy)

ememies.draw(screen)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                Player.move(0, -1)
            elif event.key == K_DOWN:
                Player.move(0, 1)
            elif event.key == K_LEFT:
                Player.move(-1, 0)
            elif event.key == K_RIGHT:
                Player.move(1, 0)
            elif event.key == K_SPACE:
                print('HP:', Player.getHealth())
            else:
                print('event.key:', event.key)
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    maze.update()
pygame.quit()