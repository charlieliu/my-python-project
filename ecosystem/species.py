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
from ecosystem.genus import *
class species(genus): 
    def __init__(self, weight=0, kingdom='', phylum = '', className = '', order = '', family = '', genus = '', species = ''):
        super().__init__(weight, kingdom, phylum, className, order, family, genus)  # 使用 super() 繼承 father __init__ 裡所有屬性
        self.species = species                                                      # 種
        # self.info()

# 家貓（學名：Felis catus 或 Felis silvestris catus） https://zh.wikipedia.org/wiki/%E7%8C%AB
class catus(Felis):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.species = 'catus'      # 貓
        self.setScientificName()    # 學名
        # self.info()
# 老虎（學名：Panthera tigris）https://zh.wikipedia.org/wiki/%E8%99%8E
class tigris(Panthera):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.species = 'tigris'     # 虎
        self.setScientificName()    # 學名
        # self.info()
# 綠頭鴨 (學名：Anas platyrhynchos) https://zh.wikipedia.org/zh-tw/%E7%BB%BF%E5%A4%B4%E9%B8%AD
class platyrhynchos(Anas):
    def __init__(self, weight=0):
        super().__init__(weight)        # 使用 super() 繼承 father __init__ 裡所有屬性
        self.species = 'platyrhynchos'  # 鴨
        self.setScientificName()        # 學名
        # self.info()
# 疣鼻棲鴨 荷西時期引進台灣（學名：Cairina moschata）https://zh.wikipedia.org/zh-tw/%E7%96%A3%E9%BC%BB%E6%A3%B2%E9%B4%A8
class moschata(Cairina):
    def __init__(self, weight=0):
        super().__init__(weight)        # 使用 super() 繼承 father __init__ 裡所有屬性
        self.species = 'moschata'       # 鴨
        self.setScientificName()        # 學名
        # self.info()