'''
現代生物分類依次採用
界 kingdom
門 phylum 動物學 / division 植物學
綱 class
目 order
科 family
屬 genus
種 species
'''
import random
from ecosystem.creature import *
class kingdom(creature):
    def __init__(self, weight=0, kingdom=''):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = kingdom      # 界
        # self.info()
# 植物界
class plant(creature):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = 'Plantae'            # 植物界
        self.activity_range = {'land'}      # Set Types: et
        self.chloroplast = True             # 有沒有葉綠體 Boolean Type: bool
        # self.info()
    '''
    光合作用也稱光能合成 photosynthesis
    是植物、藻類和藍菌等生產者利用光能把一氧化二氫、二氧化碳或硫化氫等無機物轉變成可以儲存化學能的有機物（比如碳水化合物）的生物過程。
    光合作用可分為產氧光合作用和不產氧光合作用兩類，並會因為不同環境改變反應速率。
    '''
    def photosynthesis(self):
        hour = 0                            # 花費時間
        amount = 0                          # 消耗水份
        while self.chloroplast == True and self.water > 0:
            hour += 1
            if self.water > (0.1 * self.weight):
                amount += 0.1 * self.weight
            else:
                amount += self.water
        if amount > 0:
            self.weight += amount * 1.5
            self.water -= amount
        print(self.species, 'used time:', hour, 'water:', amount)
# 動物界
class animal(creature):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = 'Metazoan'           # 動物界
        self.activity_range = set()         # Set Types: et
        self.working_hour = float(0)        # Numeric Types: float
        self.max_working_hour = float(12)   # Numeric Types: float
        self.mouth = 0                      # Numeric Types: int
        self.eye = 0                        # Numeric Types: int
        self.leg = 0                        # Numeric Types: int
        self.wing = 0                       # Numeric Types: int
        self.food = []                      # Sequence Types: list
        if random.randint(0, 2) == 0:       # get random from 0 to 1
            self.gender = 'female'
        else:
            self.gender = 'male'
        self.urine = float(0)               # 尿液 Numeric Types: float
        self.stool = float(0)               # 糞便 Numeric Types: float
        self.exchange_rate = 0.37           # 換肉率 Numeric Types: float
        # self.info()
        '''
        https://www.loverabbit.org/article_detail/153
        蛋白質保留率(Protein retention)
        肉雞 37%
        鮭魚 28%
        肉豬 21%
        水產動物平均 19%
        兔肉 17-19%。
        肉牛 13%
        '''
    def canEaten(self, food):
        if self.mouth < 1:
            print(self.species, 'No mouth for drink:', self.mouth)
            return 0
        amount = float(food.weight)
        if amount < 0:
            print(self.species, 'No drink:', amount)
            return 0
        return amount
    def drink(self, food):
        amount = self.canEaten(food)
        self.water += amount
        self.weight += amount
        self.urine += amount * self.exchange_rate
        self.sleepiness(amount)
    def eat(self, food):
        amount = self.canEaten(food)
        self.weight += amount
        self.stool += amount * self.exchange_rate
        self.sleepiness(amount)
    def pee(self):
        if self.urine <= 0:
            return 0;
        amount = self.urine
        self.water -= amount
        self.weight -= amount
        self.sleepiness(amount)
        return amount
    def poop(self):
        if self.stool < 0:
            return 0
        amount = self.stool
        self.weight -= float(amount)
        self.stool -= amount
        self.sleepiness(amount)
        return amount
    def sleepiness(self, hour):
        self.working_hour += float(hour)
        if self.working_hour >= self.max_working_hour:
            print(self.species, 'need sleep', self.working_hour, '/', self.max_working_hour)
    def hunt(self, forest):
        while self.working_hour > self.max_working_hour:
            item = forest.find()
            if item.species in self.food:
                self.eat(item)
    def run(self):
        if self.leg >= 2:
            print(self.species, 'run')
    def walk(self):
        if self.leg > 0:
            print(self.species, 'walk')
    def fly(self):
        if self.wing > 0:
            print('fly')
    def sleep(self, hour=0):
        if self.working_hour >= float(hour):
            self.working_hour -= float(hour)
        else:
            self.working_hour = 0
        print(self.species, 'sleep:', hour)
    def look(self, forest):
        if self.eye > 0:
            item = forest.find()
            print(self.species, 'see:', item.species)
        else:
            item = thing()
            print(self.species, 'Does not have eye')
        return item