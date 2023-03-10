from ecosystem.species import *

class duck(Anas):
    def __init__(self, weight=0):
        super().__init__(weight)                        # 使用 super() 繼承 father __init__ 裡所有屬性
        self.mouth = 1                                  # Numeric Types:    int
        self.wing = 2                                   # Numeric Types:    int
        self.leg = 2                                    # Numeric Types:    int
        self.food = ['vegetable','worm','insect']       # Sequence Types:	list
        self.activity_range = {'land','lake','pool'}    # Set Types:        et
        # self.info()

# 綠頭鴨 (學名：Anas platyrhynchos) https://zh.wikipedia.org/zh-tw/%E7%BB%BF%E5%A4%B4%E9%B8%AD
platyrhynchos = duck(0.1)
platyrhynchos.genus = 'Anas'
platyrhynchos.species = 'platyrhynchos'
platyrhynchos.setScientificName()
platyrhynchos.info()

# 疣鼻棲鴨 荷西時期引進台灣（學名：Cairina moschata）https://zh.wikipedia.org/zh-tw/%E7%96%A3%E9%BC%BB%E6%A3%B2%E9%B4%A8
moschata = moschata(0.2)
moschata.info()
