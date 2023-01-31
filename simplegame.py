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
    attack = 1
    luck = 1
    ranged = 1
    defence = 1
    magic = 1
    role = 1
    def __init__(self, name, color=(0,0,0), radium=10):
        pygame.sprite.Sprite.__init__(self)
        self.id = getMemberId()
        self.name = name
        self.attack = random.randint(6,10)
        self.luck = random.randint(1,10)
        self.ranged = random.randint(1,10)
        self.defence = random.randint(1,5)
        self.magic = random.randint(1,10)
        self.radium = radium
        self.color = color
        self.x = random.randrange(1, int(math.floor(width/self.radium)), 2) * self.radium
        self.y = random.randrange(1, int(math.floor(height/self.radium)), 2) * self.radium
    def drawShape(self):
        self.image = pygame.Surface([self.radium*2, self.radium*2])     # 繪製球體
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()                               # 取得球體區域
        self.rect.center = (self.x, self.y)                             # 初始位置
        pygame.draw.circle(self.image, self.color, (self.radium,self.radium), self.radium, 0)
        screen.blit(self.image, self.rect.topleft)
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        # 到達左右邊界
        if self.rect.left <= self.radium and dx < 0:
            self.x = self.radium
            print(self.name, 'left', self.rect.left, self.radium)
        elif self.rect.right >= width and dx > 0:
            self.x = (width - self.radium)
            print(self.name, 'right', self.rect.right, width)
        else:
            self.x += (dx * self.radium * 2)
        # 到達上下邊界
        if self.rect.top <= self.radium and dy < 0:
            self.y = self.radium
            print(self.name, 'top', self.rect.top, self.radium)
        elif self.rect.bottom >= height and dy > 0:
            self.y = (height - self.radium)
            print(self.name, 'bottom', self.rect.top, height)
        else:
            self.y += (dy * self.radium * 2)
        self.rect.center = (self.x, self.y)
    def update(self):
        self.drawShape()
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
        if self.role == item.role:
            self.rebound()
            item.rebound()
            return False
        print('Before self', 'name:', self.name, 'health:', self.health, 'defence:', self.defence, 'attack:', self.attack)
        print('Before item', 'name:', item.name, 'health:', item.health, 'defence:', item.defence, 'attack:', item.attack)
        if (item.attack - self.defence) > 0:
            self.health -= (item.attack - self.defence)
        if self.health <= 0:
            self.health = 0
        if (self.attack - item.defence) > 0:
            item.health -= (self.attack - item.defence)
        if item.health <= 0:
            item.health = 0
        print('After self', 'name:', self.name, 'health:', self.health, 'defence:', self.defence, 'attack:', self.attack)
        print('After item', 'name:', item.name, 'health:', item.health, 'defence:', item.defence, 'attack:', item.attack)
        self.drawShape()
        item.drawShape()
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
        self.health = 20
        self.role = 0
    def drawShape(self):
        self.image = pygame.Surface([self.radium*2, self.radium*2])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()                   # 取得球體區域
        self.rect.center = (self.x, self.y)                 # 初始位置
        shapes = int(math.ceil(self.health/10)) + 3
        points = self.getPoints(shapes)
        print('drawShape shapes:', shapes, 'points:', points)
        pygame.draw.polygon(self.image, self.color, points, 0)
        screen.blit(self.image, self.rect.topleft)
    def getPoints(self, shapes):
        list = []
        angle = 360 / shapes
        cross = 0
        x, y = 0, 0
        max_x = float(0)
        min_x = float(0)
        max_y = float(0)
        min_y = float(0)
        for i in range(shapes):
            cross += angle
            x += math.cos(math.radians(cross))
            y += math.sin(math.radians(cross))
            if float(x) > max_x: max_x = float(x)
            if float(x) < min_x: min_x = float(x)
            if float(y) > max_y: max_y = float(y)
            if float(y) < min_y: min_y = float(y)
            list.append((x, y))
        print('getPoints min_x:', min_x, 'min_y:', min_y)
        alfa = self.radium * 2 / (max_x - min_x)
        points = []
        for (x, y) in list:
            x = (x - min_x) * alfa
            y = (y - min_y) * alfa
            points.append((x, y))
        print('getPoints shapes:', shapes, 'points:', points)
        return points
        
class Enemy(Chess):
    def __init__(self):
        super().__init__('ememy', (255,0,0))
        self.name = 'ememy_' + str(self.id)
        self.drawShape()
    def update(self):
        self.move(random.randint(-1, 1), random.randint(-1, 1))
        self.drawShape()
        
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
                print('exist.item1', item1.id)
                continue
            else:
                for item2 in self.members:
                    if item2.id in activity:
                        # print('exist.item2', item2.id)
                        continue
                    elif item1 != item2 and item1.bound(item2):
                        activity.append(item1.id)
                        activity.append(item2.id)
                        item1.rebound()
                        item2.rebound()
                    if item1.health <= 0:
                        self.members.remove(item1)
                    if item2.health <= 0:
                        self.members.remove(item2)
        pygame.display.update()        

maze = area()

Player = Hero('Tom')
maze.add(Player)

for i in range(10):
    ememy = Enemy()
    ememy.update()
    maze.add(ememy)

clock = pygame.time.Clock()
maze.update()

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
                maze.update()
            elif event.key == K_DOWN:
                Player.move(0, 1)
                maze.update()
            elif event.key == K_LEFT:
                Player.move(-1, 0)
                maze.update()
            elif event.key == K_RIGHT:
                Player.move(1, 0)
                maze.update()
            elif event.key == K_SPACE:
                print('HP:', Player.getHealth())
            else:
                print('event.key:', event.key)
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
pygame.quit()