from ecosystem.species import *

# 布偶貓 https://zh.wikipedia.org/wiki/%E5%B8%83%E5%81%B6%E8%B2%93
class Ragdoll(catus):
    def __init__(self, weight=0):
        super().__init__(weight)    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.variety = 'Ragdoll'    # 品種
        # self.info()

kitty = Ragdoll(4.5)
kitty.setName('kitty')
kitty.info()

cookie = Ragdoll(5.1)
cookie.setName('cookie')
cookie.info()

tiger = tigris()
tiger.info()