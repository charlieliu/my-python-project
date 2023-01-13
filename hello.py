import random

lastMemberId = 0
def getMemberId():
    global lastMemberId
    lastMemberId += 1
    return lastMemberId
'''
https://www.w3schools.com/python/python_datatypes.asp
Text Type:      str
Numeric Types:  int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:   dict
Set Types:      et, frozenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview
None Type:      NoneType
'''
class thing:
    def __init__(self, weight=0, name='nothing'):
        self.id = getMemberId()     # Numeric Types: int
        self.forestID = 0           # Numeric Types: int
        self.farmID = 0             # Numeric Types: int
        self.name = name            # Text Type:     str
        self.weight = float(weight) # Numeric Types: float
        # print(self.__dict__)
    def info(self):
        print(self.__dict__)
    def setName(self, name):
        self.name = name
class reward(thing):
    def __init__(self, weight=0, name='nothing'):
        super().__init__(weight, name)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.list = []       # Sequence Types:	list
    def add(self, item):
        self.list.append(item)
        self.weight += float(item.weight)
    def remove(self):
        if len(self.list) > 0:
            item = self.list.pop()
            self.weight -= float(item.weight)
        else:
            item = thing()
        return item

class creature(thing):
    def __init__(self, weight=0, species='creature'):
        super().__init__(weight, '')   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = 'creature'   # Text Type: str
        self.phylum = ''            # Text Type: tr
        self.division = ''          # Text Type: str
        self.className = ''         # Text Type: str
        self.order = ''             # Text Type: str
        self.family = ''            # Text Type: str
        self.genus = ''             # Text Type: str
        self.species = species      # Text Type: str
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
        self.gender = ''            # Text Type:        str
        self.water = float(0)       # Numeric Types:    float
        self.activity_range = set() # Set Types:        et
        # self.info()
    def drink(self, water):
        self.water += float(water)
class plant(creature):
    def __init__(self, weight=0, species='plant'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = 'Plantae'            # 植物界
        self.activity_range = {'land'}      # Set Types:    et
        self.chloroplast = True             # Boolean Type: bool
    '''
    光合作用也稱光能合成 photosynthesis
    是植物、藻類和藍菌等生產者利用光能把一氧化二氫、二氧化碳或硫化氫等無機物轉變成可以儲存化學能的有機物（比如碳水化合物）的生物過程。
    光合作用可分為產氧光合作用和不產氧光合作用兩類，並會因為不同環境改變反應速率。
    '''
    def photosynthesis(self):
        hour = 0    # used time
        amount = 0  # amount of water
        while self.chloroplast == True and self.water > 0:
            hour += 1
            if self.water > (0.1 * self.weight):
                amount += 0.1 * self.weight
            else:
                amount += self.water
        if amount > 0:
            self.weight += amount * 1.5
            self.water -= amount
        print(self.species, 'used time:', hour, 'water:', amount)
class animal(creature):
    def __init__(self, weight=0, species='animal'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.kingdom = 'Metazoan'           # 動物門
        self.working_hour = float(0)        # Numeric Types:    float
        self.max_working_hour = float(12)   # Numeric Types:    float
        self.mouth = 0                      # Numeric Types:    int
        self.eye = 0                        # Numeric Types:    int
        self.leg = 0                        # Numeric Types:    int
        self.wing = 0                       # Numeric Types:    int
        self.food = []                      # Sequence Types:	list
        if random.randint(0, 2) == 0:       # get random from 0 to 1
            self.gender = 'female'
        else:
            self.gender = 'male'
        # self.info()
    def run(self):
        if self.leg >= 2:
            print(self.species, 'run')
    def walk(self):
        if self.leg > 0:
            print(self.species, 'walk')
    def fly(self):
        if self.wing > 0:
            print('fly')
    def sleep(self, hour=0):
        if self.working_hour >= float(hour):
            self.working_hour -= float(hour)
        else:
            self.working_hour = 0
        print(self.species, 'sleep:', hour)
    def look(self, forest):
        if self.eye > 0:
            item = forest.find()
            print(self.species, 'see:', item.species)
        else:
            item = thing()
            print(self.species, 'Does not have eye')
        return item
    def eat(self, food):
        if self.mouth < 1:
            print(self.species, 'No mouth:', self.mouth)
            return
        weight = float(food.weight)
        if weight < 0:
            print(self.species, 'No food:', weight)
            return
        self.weight += weight
        print(self.species, 'eat:', food.species, 'weight:', weight, '/', self.weight)
        self.sleepiness(weight)
    def sleepiness(self, hour):
        self.working_hour += float(hour)
        if self.working_hour >= self.max_working_hour:
            print(self.species, 'need sleep', self.working_hour, '/', self.max_working_hour)
    def hunt(self, forest):
        while self.working_hour > self.max_working_hour:
            item = forest.find()
            if item.species in self.food:
                self.eat(item)
class Chordata(animal): # 脊索動物門
    def __init__(self, weight=0, species='Chordata'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = 'Chordata'            # 脊索動物門
        # self.info()
class Aves(Chordata): # 鳥類 鳥綱
    def __init__(self, weight=0, species='Aves'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = 'Aves'             # 鳥綱
        self.mouth = 1                      # Numeric Types: int
        self.eye = 2                        # Numeric Types: int
        self.wing = 2                       # Numeric Types: int
        # self.info()
class Anseriformes(Aves): # 雁形目
    def __init__(self, weight=0, species='Anseriformes'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.order = 'Anseriformes'         # 雁形目
        # self.info()
class Anatidae(Anseriformes): # 雁鴨科
    def __init__(self, weight=0, species='Anatidae'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.family = 'Anatidae'            # 雁鴨科
        # self.info()
class Anas(Anatidae): # 鴨屬
    def __init__(self, weight=0, species='Anas'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.genus = 'Anas'                 # 鴨屬
        # self.info()
class duck(Anas):
    def __init__(self, weight=0, species='duck'):
        super().__init__(weight, species)               # 使用 super() 繼承 father __init__ 裡所有屬性
        self.mouth = 1                                  # Numeric Types:    int
        self.wing = 2                                   # Numeric Types:    int
        self.leg = 2                                    # Numeric Types:    int
        self.food = ['vegetable','worm','insect']       # Sequence Types:	list
        self.activity_range = {'land','lake','pool'}    # Set Types:        et
        # self.info()
class Mammalia(Chordata): # 哺乳類 哺乳綱
    def __init__(self, weight=0, species='Mammalia'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = 'Mammalia'         # 哺乳綱
        self.mouth = 1                      # Numeric Types: int
        self.eye = 2                        # Numeric Types: int
class cow(Mammalia):
    def __init__(self, weight=0):
        super().__init__(weight, 'cow')     # 使用 super() 繼承 father __init__ 裡所有屬性
        self.leg = 4                        # Numeric Types: int
        self.food = ['vegetable','grass']   # list
        self.activity_range = {'land'}      # set
class human(Mammalia):
    def __init__(self, weight=0, name='', height=0, gender=''):
        super().__init__(weight, 'sapiens')             # 智人種
        self.order = 'Primates'                         # 靈長目
        self.family = 'Hominidae'                       # 人科
        self.genus = 'Homo'                             # 人屬
        self.leg = 2                                    # Numeric Types:    int
        self.name = name
        self.max_working_hour = float(8)
        self.gender = gender                            # Text Type: str
        self.food = ['vegetable','duck','chicken']      # Sequence Types:	list
        self.activity_range = {'land','lake','pool'}    # Set Types:        et
        self.height = height
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
class Arthropoda(animal): # 節肢動物門
    def __init__(self, weight=0, species='insect'):
        super().__init__(weight, species)   # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = 'Arthropoda'          # 節肢動物門
        self.mouth = 1                          # Numeric Types:    int
class insect(Arthropoda): # 昆蟲綱
    def __init__(self, weight=0):
        super().__init__(weight, 'insect')      # 使用 super() 繼承 father __init__ 裡所有屬性
        self.className = 'Insecta'              # 昆蟲綱
        self.wing = 4                           # Numeric Types:    int
        self.leg = 6                            # Numeric Types:    int
        self.food = ['vegetable','grass']       # Sequence Types:	list
        self.activity_range = {'soil','land'}   # Set Types:        et
class worm(animal): # 蚯蚓
    def __init__(self, weight=0):
        super().__init__(weight, 'worm')    # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = 'Annelida'            # 環節動物門
        self.className = 'Clitellata'       # 環帶綱
        self.mouth = 1                      # Numeric Types:    int
        self.food = ['vegetable','grass']   # Sequence Types:	list
        self.activity_range = {'soil'}      # Set Types:        et
class area:
    def __init__(self, name = 'area'):
        self.name = name
        self.lastMemberId = 0
        self.members = []
        self.habitat = {}
        self.activity_range = set()
        print('[area] habitat', type(self.activity_range), 'habitat', type(self.habitat))
    def addTree(self, amount):
        for i in range(amount):
            item = plant(0.1, 'tree')
            self.enter(item)
    def addWorm(self, amount):
        for i in range(amount):
            weight = random.uniform(0.01, 0.1)
            item = worm(weight)
            self.enter(item)
    def addInsect(self, amount):
        for i in range(amount):
            weight = random.random()
            item = insect(weight)
            self.enter(item)
    def addDuck(self, amount):
        for i in range(amount):
            weight = random.uniform(0.1, 3)
            item = duck(weight)
            self.enter(item)
    def updateIndex(self):
        for idx, member in enumerate(self.members):
            member.idx = int(idx)
        for location in self.habitat:
            for loc_idx, member in enumerate(self.habitat[location]):
                member.loc_idx = int(loc_idx)
                member.location = location
    def addVegetable(self, amount):
        for i in range(amount):
            item = plant(0.1, 'vegetable')
            self.enter(item)
    def addGrass(self, amount):
        for i in range(amount):
            item = plant(0.1, 'grass')
            self.enter(item)
    def addCow(self, amount):
        weight = random.uniform(5, 10)
        for i in range(amount):
            item = cow(weight)
            self.enter(item)
    def leave(self, member):
        del self.members[member.idx]
        del self.habitat[member.location][member.loc_idx]
        self.updateIndex()
    def exist(self):
        for item in self.members:
            print('[', self.name, '] exist:', item.species, 'idx:', item.idx, 'id:', item.id, '-', item.forestID, '-', item.farmID, 'location:', item.location, 'loc_idx:', item.loc_idx)
    def grow(self, kingdoms, hour=1):
        list = []
        for member in self.members:
            if member.kingdom in kingdoms:
                list.append(member)
        for item in list:
            weight = item.weight * random.random() * hour / len(list)
            item.weight += weight
            self.members[item.idx].weight = item.weight
            self.habitat[item.location][item.loc_idx].weight = item.weight
            # print('[', self.name, '] grow:', item.species, 'id:', item.id, '-', item.forestID, '-', item.farmID, 'weight:', weight, '/', item.weight)
    def pickLocation(self, member):
        # print('[', self.name, '] self', type(self.activity_range), 'member', type(member.activity_range))
        range = self.activity_range.intersection(member.activity_range)
        if len(range) == 0:
            return ''
        if len(range) == 1:
            # return next(iter(range))
            return range.pop()
        return random.sample(range, 1)[0]
    def find(self):
        if len(self.members) > 1:
            item = random.choice(self.members)
        elif len(self.members) == 1:
            item = self.members[0]
        else:
            item = thing()
        print('[', self.name, '] find:', item.species, 'id:', item.id, '-', item.forestID, '-', item.farmID)
        return item
        
class forest(area):
    def __init__(self):
        super().__init__('forest')
        self.activity_range = {'land','soil','lake'}
        for location in self.activity_range:
            self.habitat[location] = []
        print('[forest] habitat', type(self.activity_range), 'habitat', type(self.habitat))
    def enter(self, member):
        location = self.pickLocation(member)
        if location == '':
            return member
        self.lastMemberId += 1
        member.forestID = self.lastMemberId
        member.location = location
        self.members.append(member)
        self.habitat[location].append(member)
        random.shuffle(self.members)
        random.shuffle(self.habitat[location])
        self.updateIndex()
    def find(self):
        if random.randint(0, 100) < 78: # 78% get creature in the forest
            if len(self.members) > 1:
                item = random.choice(self.members)
            elif len(self.members) == 1:
                item = self.members[0]
            else:
                item = thing()
        else:
            item = thing()
        print('[', self.name, '] find:', item.species, 'id:', item.id, '-', item.forestID, '-', item.farmID)
        return item
class farm(area):
    def __init__(self):
        super().__init__('farm')
        self.habitat = {'land':[],'soil':[],'pool':[]}
        for location in self.habitat:
            self.activity_range.add(location)
        print('[farm] habitat', type(self.activity_range), 'habitat', type(self.habitat))
    def enter(self, member):
        location = self.pickLocation(member)
        if location == '':
            return member
        self.lastMemberId += 1
        member.farmID = self.lastMemberId
        member.location = location
        self.members.append(member)
        self.habitat[location].append(member)
        self.updateIndex()
    def feed(self, hour=1):
        self.grow(['animal'], hour)
    def farming(self, hour=1):
        self.grow(['plant'], hour)
    def harvest(self):
        pass

# item = duck()
# item.info()

# # 綠頭鴨 (學名：Anas platyrhynchos) https://zh.wikipedia.org/zh-tw/%E7%BB%BF%E5%A4%B4%E9%B8%AD
# platyrhynchos = duck(0.1, 'Anas platyrhynchos')
# platyrhynchos.info()

# # 疣鼻棲鴨 荷西時期引進台灣（學名：Cairina moschata）https://zh.wikipedia.org/zh-tw/%E7%96%A3%E9%BC%BB%E6%A3%B2%E9%B4%A8
# moschata = duck(0.2, 'Cairina moschata')
# moschata.info()

# farm = farm()
# farm.addVegetable(10)
# farm.addGrass(10)
# farm.addCow(1)
# for i in range(10):
#     weight = random.uniform(0.9, 1.1)
#     item = Aves(weight, 'chicken')
#     item.food = ['vegetable','worm','insect']
#     item.activity_range = {'land'}
#     item.info()
#     farm.enter(item)

# forest = forest()
# forest.addTree(100)
# forest.addWorm(100)
# forest.addInsect(50)
# forest.addDuck(10)
# forest.addGrass(1000)

# charlie = human(78, 'chalrie', 172, 'male')
# charlie.info()
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
