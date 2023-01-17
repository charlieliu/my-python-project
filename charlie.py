from ecosystem.species import *
class reward(thing):
    def __init__(self, weight=0):
        super().__init__(weight)  # 使用 super() 繼承 father __init__ 裡所有屬性
        self.list = []                  # Sequence Types:	list
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
class area:
    def __init__(self, name = 'area'):
        self.name = name
        self.lastMemberId = 0
        self.members = []
        self.habitat = {}
        self.activity_range = set()
        print('[area] habitat', type(self.activity_range), 'habitat', type(self.habitat))
    def updateIndex(self):
        for idx, member in enumerate(self.members):
            member.idx = int(idx)
        for location in self.habitat:
            for loc_idx, member in enumerate(self.habitat[location]):
                member.loc_idx = int(loc_idx)
                member.location = location
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
        species = ''
        if hasattr(item, 'species'):
            species = item.species
        print('[', self.name, '] find:', species, 'id:', item.id, '-', item.forestID, '-', item.farmID)
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
        species = ''
        if hasattr(item, 'species'):
            species = item.species
        print('[', self.name, '] find:', species, 'id:', item.id, '-', item.forestID, '-', item.farmID)
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
class cow(Mammalia):
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.leg = 4                        # Numeric Types: int
        self.species = 'cow'
        self.setScientificName()
        self.food = ['vegetable','grass']   # list
        self.activity_range = {'land'}      # set
        # self.info()

class worm(animal): # 蚯蚓
    def __init__(self, weight=0):
        super().__init__(weight)            # 使用 super() 繼承 father __init__ 裡所有屬性
        self.phylum = 'Annelida'            # 環節動物門
        self.className = 'Clitellata'       # 環帶綱
        self.species = 'worm'
        self.setScientificName()
        self.mouth = 1                      # Numeric Types:    int
        self.food = ['vegetable','grass']   # Sequence Types:	list
        self.activity_range = {'soil'}      # Set Types:        et
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
            species = ''
            if hasattr(item, 'species'):
                species = item.species
            if species in list:
                prey.add(item)
                forest.leave(item)
                self.sleepiness(unit_hour)
                keep_hour += working_hour
                working_hour += working_hour
        # print('hunt', self.working_hour, '/', self.max_working_hour)
        return prey
def addTree(area, amount):
    for i in range(amount+1):
        item = plant(0.1)
        item.species = 'tree'
        item.setScientificName()
        area.enter(item)
def addWorm(area, amount):
    for i in range(amount+1):
        weight = random.uniform(0.01, 0.1)
        item = worm(weight)
        area.enter(item)
def addInsect(area, amount):
    for i in range(amount+1):
        weight = random.random()
        item = insect(weight)
        item.species = 'insect'
        item.setScientificName()
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
        item.setScientificName()
        area.enter(item)
def addCow(area, amount):
    weight = random.uniform(5, 10)
    for i in range(amount+1):
        item = cow(weight)
        area.enter(item)

farm = farm()
addVegetable(farm, 1)
addGrass(farm, 1)
addCow(farm, 1)

forest = forest()
addTree(forest, 100)
addWorm(forest, 100)
addInsect(forest, 50)
addGrass(forest, 1000)

charlie = human(78, 'chalrie', 172, 'male')
charlie.info()
print(charlie.name, charlie.BMI())

meals = reward()
list = []
for item in charlie.food:
    list.append(item)
list.append('worm')
list.append('grass')
prey = charlie.hunt(forest, 2, list)
while prey.weight:
    item = prey.remove()
    # print('charlie prey:', item.species, 'id:', item.id, '-', item.forestID, '-', item.farmID)
    species = ''
    if hasattr(item, 'species'):
        species = item.species
    kingdom = ''
    if hasattr(item, 'kingdom'):
        kingdom = item.kingdom
    if species in charlie.food and meals.weight < 1:
        meal = charlie.cook(item)
        meals.add(meal)
    elif kingdom == 'animal' or species == 'grass':
        farm.enter(item)
    else:
        break
while len(meals.list):
    item = meals.remove()
    charlie.eat(item)
    # print('charlie eat:', item.species, item.weight, item.id)
forest.exist()
print('==============================================================')
farm.exist()
print('==============================================================')
charlie.farming(farm)