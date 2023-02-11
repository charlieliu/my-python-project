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
from ecosystem.phylum import *
class className(phylum): 
    def __init__(self, weight=0, kingdom='', phylum = '', className = ''):
        super().__init__(weight, kingdom, phylum)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = className                  # 綱
        # self.info()
# 哺乳類 哺乳綱 https://zh.wikipedia.org/wiki/%E5%93%BA%E4%B9%B3%E5%8A%A8%E7%89%A9
class Mammalia(Chordata):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = 'Mammalia' # 哺乳綱
        self.mouth = 1              # Numeric Types: int
        self.eye = 2                # Numeric Types: int
        # self.info()
# 鳥類 鳥綱
class Aves(Chordata): 
    def __init__(self, weight=0):
        super().__init__(weight)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = 'Aves'             # 鳥綱
        self.mouth = 1                      # Numeric Types: int
        self.eye = 2                        # Numeric Types: int
        self.wing = 2                       # Numeric Types: int
        # self.info()
# 昆蟲綱
class insect(Arthropoda): 
    def __init__(self, weight=0):
        super().__init__(weight)                # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = 'Insecta'              # 昆蟲綱
        self.wing = 4                           # Numeric Types:    int
        self.leg = 6                            # Numeric Types:    int
        self.food = ['vegetable','grass']       # Sequence Types:	list
        self.activity_range = {'soil','land'}   # Set Types:        et
        # self.info()