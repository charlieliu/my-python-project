from ecosystem.__main__ import *
from ecosystem.creature import *
from ecosystem.kingdom import *

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