from ecosystem.__main__ import *
from ecosystem.creature import *
from ecosystem.kingdom import *
from ecosystem.phylum import *

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
class insect(Arthropoda): # 昆蟲綱
    def __init__(self, weight=0):
        super().__init__(weight)                # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = 'Insecta'              # 昆蟲綱
        self.wing = 4                           # Numeric Types:    int
        self.leg = 6                            # Numeric Types:    int
        self.food = ['vegetable','grass']       # Sequence Types:	list
        self.activity_range = {'soil','land'}   # Set Types:        et
        # self.info()