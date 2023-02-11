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
from ecosystem.order import *
class family(order): 
    def __init__(self, weight=0, kingdom='', phylum = '', className = '', order = '', family = ''):
        super().__init__(weight, kingdom, phylum, className, order) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.family = family                                        # 科
        # self.info()
# 貓科 https://zh.wikipedia.org/wiki/%E7%8C%AB%E7%A7%91
class Felidae(Carnivora):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.family = 'Felidae'     # 貓科
        self.scientific_name = ''   # 學名
        # self.info()
class Anatidae(Anseriformes): # 雁鴨科
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.family = 'Anatidae'    # 雁鴨科
        # self.info()