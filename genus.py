from family import *
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
# 鴨屬
class Anas(Anatidae):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = 'Anas'                 # 鴨屬
        self.setScientificName()            # 學名
        # self.info()