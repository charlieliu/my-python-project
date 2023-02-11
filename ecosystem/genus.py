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
from ecosystem.family import *
class genus(family): 
    def __init__(self, weight=0, kingdom='', phylum = '', className = '', order = '', family = '', genus = ''):
        super().__init__(weight, kingdom, phylum, className, order, family) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = genus                                                  # 屬
        # self.info()
# 貓屬 https://zh.wikipedia.org/wiki/%E8%B2%93%E5%B1%AC
class Felis(Felidae):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = 'Felis'                # 貓屬
        self.setScientificName()            # 學名
        # self.info()
# 豹屬 https://zh.wikipedia.org/wiki/%E8%B1%B9%E5%B1%9E
class Panthera(Felis):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = 'Panthera'             # 豹屬
        self.setScientificName()            # 學名
        # self.info()
# 家鴨（學名：Anas platyrhynchos domesticus） https://zh.wikipedia.org/zh-tw/%E5%AE%B6%E9%B8%AD
class Anas(Anatidae):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = 'Anas'                 # 鴨屬
        self.setScientificName()            # 學名
        # self.info()
# 疣鼻棲鴨 荷西時期引進台灣（學名：Cairina moschata）https://zh.wikipedia.org/zh-tw/%E7%96%A3%E9%BC%BB%E6%A3%B2%E9%B4%A8   
class Cairina(Anatidae):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = 'Cairina'              # 鴨屬
        self.setScientificName()            # 學名
        # self.info()