from order import *
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