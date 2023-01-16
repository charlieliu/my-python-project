from ecosystem.__main__ import *
from ecosystem.creature import *
from ecosystem.kingdom import *
from ecosystem.phylum import *
from ecosystem.className import *
from ecosystem.order import *
from ecosystem.family import *
from ecosystem.genus import *

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