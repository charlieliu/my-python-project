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
from ecosystem.kingdom import *
class phylum(kingdom): 
    def __init__(self, weight=0, kingdom='', phylum = ''):
        super().__init__(weight, kingdom)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = phylum                # 門
        # self.info()
class Chordata(animal): 
    def __init__(self, weight=0):
        super().__init__(weight)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = 'Chordata'   # 脊索動物門
        # self.info()
class Arthropoda(animal): # 節肢動物門
    def __init__(self, weight=0):
        super().__init__(weight)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = 'Arthropoda' # 節肢動物門
        self.mouth = 1             # Numeric Types:    int
        # self.info()