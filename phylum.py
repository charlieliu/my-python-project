from kingdom import *
# 脊索動物門 https://zh.wikipedia.org/wiki/%E8%84%8A%E6%A4%8E%E5%8A%A8%E7%89%A9
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