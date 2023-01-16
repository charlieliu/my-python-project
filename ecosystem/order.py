from ecosystem.__main__ import *
from ecosystem.creature import *
from ecosystem.kingdom import *
from ecosystem.phylum import *
from ecosystem.className import *
class order(className): 
    def __init__(self, weight=0, kingdom='', phylum = '', className = '', order = ''):
        super().__init__(weight, kingdom, phylum, className)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.order = order                                      # 目
        # self.info()
# 食肉目 https://zh.wikipedia.org/wiki/%E9%A3%9F%E8%82%89%E7%9B%AE
class Carnivora(Mammalia): 
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.order = 'Carnivora'    # 食肉目
        self.leg = 4                # Numeric Types: int
        # self.info()
# 雁形目
class Anseriformes(Aves):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.order = 'Anseriformes' # 雁形目
        # self.info()