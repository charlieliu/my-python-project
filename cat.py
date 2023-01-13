import random

lastMemberId = 0
def getMemberId():
    global lastMemberId
    lastMemberId += 1
    return lastMemberId
'''
https://www.w3schools.com/python/python_datatypes.asp
Text Type:      str
Numeric Types:  int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:   dict
Set Types:      et, frozenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview
None Type:      NoneType
'''
class thing:
    def __init__(self, weight=0, name='nothing'):
        self.id = getMemberId()     # Numeric Types: int
        self.forestID = 0           # Numeric Types: int
        self.farmID = 0             # Numeric Types: int
        self.name = name            # Text Type:     str
        self.weight = float(weight) # Numeric Types: float
        # print(self.__dict__)
    def info(self):
        print(self.__dict__)
    def setName(self, name):
        self.name = name
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
class creature(thing):
    def __init__(self, weight=0):
        super().__init__(weight, '')   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = ''           # Text Type: str
        self.phylum = ''            # Text Type: tr
        self.division = ''          # Text Type: str
        self.className = ''         # Text Type: str
        self.order = ''             # Text Type: str
        self.family = ''            # Text Type: str
        self.genus = ''             # Text Type: str
        self.species = ''           # Text Type: str
        self.gender = ''            # Text Type: str
        self.water = float(0)       # Numeric Types: float
        self.protein = float(0)     # Numeric Types: float
        # self.info()
    def setWeight(self, weight):
        self.weight = float(weight)
# 動物界
class animal(creature):
    def __init__(self, weight=0):
        super().__init__(weight)        # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = 'Metazoan'       # 動物界
        self.urine = float(0)           # 尿液 Numeric Types: float
        self.stool = float(0)           # 糞便 Numeric Types: float
        self.exchange_rate = 0.37       # 換肉率 Numeric Types: float
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
    def drink(self, amount):
        amount = float(amount)
        self.water += amount
        self.weight += amount
        self.urine += amount * self.exchange_rate
    def eat(self, amount):
        amount = float(amount)
        self.weight += amount
        self.stool += amount * self.exchange_rate
    def pee(self, amount):
        amount = float(amount)
        if amount > self.urine:
            amount = self.urine
        self.water -= amount
        self.weight -= amount
    def poop(self, amount):
        amount = float(amount)
        if amount > self.stool:
            amount = self.stool
        self.weight -= float(amount)
        self.stool -= amount
# 脊索動物門 https://zh.wikipedia.org/wiki/%E8%84%8A%E6%A4%8E%E5%8A%A8%E7%89%A9
class Chordata(animal): 
    def __init__(self, weight=0):
        super().__init__(weight)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = 'Chordata'   # 脊索動物門
        # self.info()
# 哺乳類 哺乳綱 https://zh.wikipedia.org/wiki/%E5%93%BA%E4%B9%B3%E5%8A%A8%E7%89%A9
class Mammalia(Chordata):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = 'Mammalia' # 哺乳綱
        self.mouth = 1              # Numeric Types: int
        self.eye = 2                # Numeric Types: int
        # self.info()
# 食肉目 https://zh.wikipedia.org/wiki/%E9%A3%9F%E8%82%89%E7%9B%AE
class Carnivora(Mammalia): 
    def __init__(self, weight=0, ):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.order = 'Carnivora'    # 食肉目
        self.leg = 4                # Numeric Types:    int
        # self.info()
# 貓科 https://zh.wikipedia.org/wiki/%E7%8C%AB%E7%A7%91
class Felidae(Carnivora):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.family = 'Felidae'     # 貓科
        self.scientific_name = ''   # 學名
        # self.info()
# 貓屬 https://zh.wikipedia.org/wiki/%E8%B2%93%E5%B1%AC
class Felis(Felidae):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = 'Felis'                # 貓屬
        self.scientific_name = self.genus   # 學名
        # self.info()
# 家貓（學名：Felis catus 或 Felis silvestris catus） https://zh.wikipedia.org/wiki/%E7%8C%AB
class catus(Felis):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.species = 'catus'      # 貓
        self.scientific_name = self.genus + ' ' + self.species
        # self.info()
# 布偶貓 https://zh.wikipedia.org/wiki/%E5%B8%83%E5%81%B6%E8%B2%93
class Ragdoll(catus):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.variety = 'Ragdoll'    # 品種
        # self.info()
# 豹屬 https://zh.wikipedia.org/wiki/%E8%B1%B9%E5%B1%9E
class Panthera(Felis):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = 'Panthera'             # 豹屬
        self.scientific_name = self.genus   # 學名
        # self.info()
# 老虎（學名：Panthera tigris）https://zh.wikipedia.org/wiki/%E8%99%8E
class tigris(Panthera):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.species = 'tigris'     # 虎
        self.scientific_name = self.genus + ' ' + self.species
        # self.info()

kitty = Ragdoll(4.5)
kitty.setName('kitty')
kitty.info()

cookie = Ragdoll(5.1)
cookie.setName('cookie')
cookie.info()

tiger = tigris()
tiger.info()