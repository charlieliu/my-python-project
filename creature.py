from main import *
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
class creature(thing):
    def __init__(self, weight=0):
        super().__init__(weight, '')   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = ''           # Text Type: str
        self.phylum = ''            # Text Type: tr
        self.division = ''          # Text Type: str
        self.className = ''         # Text Type: str
        self.order = ''             # Text Type: str
        self.family = ''            # Text Type: str
        self.genus = ''             # Text Type: str
        self.species = ''           # Text Type: str
        self.gender = ''            # Text Type: str
        self.water = float(0)       # Numeric Types: float
        self.protein = float(0)     # Numeric Types: float
        self.activity_range = set() # Set Types: et
        # self.info()
    def setWeight(self, weight):
        self.weight = float(weight)
    def setScientificName(self):
        self.scientific_name = self.genus + ' ' + self.species