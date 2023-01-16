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
class cow(Mammalia):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.leg = 4                        # Numeric Types: int
        self.species = 'cow'
        self.setScientificName()
        self.food = ['vegetable','grass']   # list
        self.activity_range = {'land'}      # set
        # self.info()
class human(Mammalia):
    def __init__(self, weight=0, name='', height=0, gender=''):
        super().__init__(weight)                        # 使用 super() 繼承 father __init__ 裡所有屬性
        self.order = 'Primates'                         # 靈長目
        self.family = 'Hominidae'                       # 人科
        self.genus = 'Homo'                             # 人屬
        self.species = 'sapiens'                        # 智人種
        self.setScientificName()
        self.leg = 2                                    # Numeric Types:    int
        self.name = name
        self.max_working_hour = float(8)
        self.gender = gender                            # Text Type: str
        self.food = ['vegetable','duck','chicken']      # Sequence Types:	list
        self.activity_range = {'land','lake','pool'}    # Set Types:        et
        self.height = height                            # 身高
        # self.info()
    def BMI(self):
        return self.weight / ((self.height/100)**2)
    def farming(self, farm, max_hour=0.1):
        unit_hour = 0.2
        keep_hour = 0
        working_hour = (self.working_hour + unit_hour)
        while working_hour < self.max_working_hour and keep_hour < max_hour:
            farm.farming(0.1)
            farm.feed(0.1)
            self.sleepiness(unit_hour)
            keep_hour += working_hour
            working_hour += working_hour
        # print('farming', self.working_hour, '/', self.max_working_hour)
    def cook(self, ingredients):
        self.sleepiness(0.1 * ingredients.weight)
        return ingredients
    def hunt(self, forest, max_hour=0.1, list=[]):
        prey = reward()
        unit_hour = 0.1
        keep_hour = 0
        working_hour = (self.working_hour + unit_hour)
        while working_hour < self.max_working_hour and keep_hour < max_hour:
            item = forest.find()
            if item.species in list:
                prey.add(item)
                forest.leave(item)
                self.sleepiness(unit_hour)
                keep_hour += working_hour
                working_hour += working_hour
        # print('hunt', self.working_hour, '/', self.max_working_hour)
        return prey
class worm(animal): # 蚯蚓
    def __init__(self, weight=0):
        super().__init__(weight, 'worm')    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = 'Annelida'            # 環節動物門
        self.className = 'Clitellata'       # 環帶綱
        self.mouth = 1                      # Numeric Types:    int
        self.food = ['vegetable','grass']   # Sequence Types:	list
        self.activity_range = {'soil'}      # Set Types:        et

def addTree(area, amount):
    for i in range(amount+1):
        item = plant(0.1, 'tree')
        area.enter(item)
def addWorm(area, amount):
    for i in range(amount+1):
        weight = random.uniform(0.01, 0.1)
        item = worm(weight)
        area.enter(item)
def addInsect(area, amount):
    for i in range(amount+1):
        weight = random.random()
        area = insect(weight)
        area.enter(item)
def addDuck(area, amount):
    for i in range(amount+1):
        weight = random.uniform(0.1, 3)
        item = duck(weight)
        area.enter(item)
def addVegetable(area, amount):
    for i in range(amount+1):
        item = plant(0.1)
        item.species = 'vegetable'
        item.setScientificName()
        area.enter(item)
def addGrass(area, amount):
    for i in range(amount+1):
        item = plant(0.1)
        item.species = 'grass'
        area.enter(item)
def addCow(area, amount):
    weight = random.uniform(5, 10)
    for i in range(amount+1):
        item = cow(weight)
        area.enter(item)
# 綠頭鴨 (學名：Anas platyrhynchos) https://zh.wikipedia.org/zh-tw/%E7%BB%BF%E5%A4%B4%E9%B8%AD
platyrhynchos = duck(0.1)
platyrhynchos.genus = 'Anas'
platyrhynchos.species = 'platyrhynchos'
platyrhynchos.setScientificName()
platyrhynchos.info()

# 疣鼻棲鴨 荷西時期引進台灣（學名：Cairina moschata）https://zh.wikipedia.org/zh-tw/%E7%96%A3%E9%BC%BB%E6%A3%B2%E9%B4%A8
moschata = moschata(0.2)
moschata.info()

farm = farm()
addVegetable(farm, 1)
addGrass(farm, 1)
addCow(farm, 1)
for i in range(2):
    weight = random.uniform(0.9, 1.1)
    item = Aves(weight)
    item.species = 'chicken'
    item.setScientificName()
    item.food = ['vegetable','worm','insect']
    item.activity_range = {'land'}
    item.info()
    farm.enter(item)

# forest = forest()
# forest.addTree(100)
# forest.addWorm(100)
# forest.addInsect(50)
# forest.addDuck(10)
# forest.addGrass(1000)

charlie = human(78, 'chalrie', 172, 'male')
charlie.info()
#print(charlie.name, charlie.BMI())

# meals = reward()
# list = []
# for item in charlie.food:
#     list.append(item)
# list.append('worm')
# list.append('grass')
# prey = charlie.hunt(forest, 2, list)
# while prey.weight:
#     item = prey.remove()
#     # print('charlie prey:', item.species, 'id:', item.id, '-', item.forestID, '-', item.farmID)
#     if item.species in charlie.food and meals.weight < 1:
#         meal = charlie.cook(item)
#         meals.add(meal)
#     elif item.kingdom == 'animal' or item.species == 'grass':
#         farm.enter(item)
#     else:
#         break
# while len(meals.list):
#     item = meals.remove()
#     charlie.eat(item)
#     # print('charlie eat:', item.species, item.weight, item.id)
# # forest.exist()
# # print('==============================================================')
# # farm.exist()
# # print('==============================================================')
# charlie.farming(farm)
