import random
lastMemberId = 0
def getMemberId():
    global lastMemberId
    lastMemberId += 1
    return lastMemberId
class thing:
    def __init__(self, weight=0, species='nothing'):
        self.id = getMemberId()
        self.forestID = 0
        self.farmID = 0
        self.weight = float(weight)
        self.name = 'nothing'
        self.kingdom = 'nothing'
        self.species = species
        self.activity_range = {}
class reward(thing):
    def __init__(self, weight=0, species='reward'):
        super().__init__(weight, species) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.list = []
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
        super().__init__(weight, species) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.mouth = 0
        self.water = float(0)
    def drink(self, water):
        self.water += float(water)
class plant(creature):
    def __init__(self, weight=0, species='plant'):
        super().__init__(weight, species) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.mouth = 0
        self.eye = 0
        self.kingdom = 'plant'
        self.gender = ''
        self.activity_range = {'land'}
    def photosynthesis(self):
        seconds = 0
        while self.water > 0:
            seconds += 1
            if self.water > (0.1 * self.weight):
                amount = 0.1 * self.weight
            else:
                amount = self.water
            self.weight += amount
            self.water -= amount
        print(self.species, seconds, 'water:', self.water, 'weight:', self.weight)
class animal(creature):
    def __init__(self, weight=0, species='animal'):
        super().__init__(weight, species) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.mouth = 1
        self.eye = 0
        self.working_hour = float(0)
        self.max_working_hour = float(12)
        self.leg = 0
        self.wing = 0
        self.food = []
        self.kingdom = 'animal'
        self.activity_range = {}
        probability = random.randint(0, 100)
        if probability < 50:
            self.gender = 'female'
        else:
            self.gender = 'male'
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
        if self.working_hour >= hour:
            self.working_hour -= hour
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
        elif food.weight < 0:
            print(self.species, 'No food:', food.weight)
        else:
            self.weight += food.weight
            print(self.species, 'eat:', food.species, food.weight, 'weight:', self.weight)
            self.working_hour += 1
            self.sleepiness(food.weight)
    def sleepiness(self, hour):
        self.working_hour += float(hour)
        if self.working_hour >= self.max_working_hour:
            print(self.species, 'need sleep', self.working_hour, '/', self.max_working_hour)
    def hunt(self, forest):
        while self.working_hour > self.max_working_hour:
            item = forest.find()
            if item.species in self.food:
                self.eat(item)
class bird(animal):
    def __init__(self, weight=0, species='bird'):
        super().__init__(weight, species) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.eye = 2
        self.wing = 2
class worm(animal):
    def __init__(self, weight=0):
        super().__init__(weight, 'worm') # 使用 super() 繼承 father __init__ 裡所有屬性
        self.food = ['vegetable']
        self.activity_range = {'soil'}
class insect(animal):
    def __init__(self, weight=0):
        super().__init__(weight, 'insect') # 使用 super() 繼承 father __init__ 裡所有屬性
        self.wing = 4
        self.leg = 2
        self.food = ['vegetable']
        self.activity_range = {'soil','land'}
class duck(bird):
    def __init__(self, weight=0):
        super().__init__(weight, 'duck') # 使用 super() 繼承 father __init__ 裡所有屬性
        self.wing = 2
        self.leg = 2
        self.food = ['vegetable','worm','insect']
        self.activity_range = {'land','lake','pool'}
class cow(animal):
    def __init__(self, weight=0):
        super().__init__(weight, 'cow') # 使用 super() 繼承 father __init__ 裡所有屬性
        self.leg = 0
        self.food = ['vegetable','grass']
        self.activity_range = {'land'}
class human(animal):
    def __init__(self, weight=0, name='', height=0, gender=''):
        super().__init__(weight, 'human')
        self.name = name
        self.height = height
        self.eye = 2
        self.max_working_hour = float(8)
        self.gender = gender
        self.food = ['vegetable','duck','chicken']
        self.activity_range = {'land','lake','pool'}
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
        print('farming', self.working_hour, '/', self.max_working_hour)
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
        print('hunt', self.working_hour, '/', self.max_working_hour)
        return prey
class area:
    def __init__(self, name = 'area'):
        self.name = name
        self.lastMemberId = 0
        self.members = []
        self.habitat = {}
        self.activity_range = set()
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
            print('[', self.name, '] grow:', item.species, 'id:', item.id, '-', item.forestID, '-', item.farmID, 'weight:', weight, '/', item.weight)
class forest(area):
    def __init__(self):
        super().__init__('forest')
        self.activity_range = {'land','soil','lake'}
        for location in self.activity_range:
            self.habitat[location] = []
    def enter(self, member):
        range = self.activity_range.intersection(member.activity_range)
        if len(range) == 0:
            print('[', self.name, '] 交集:', len(range), member.species)
            return member
        location = random.sample(range, 1)
        self.lastMemberId += 1
        member.forestID = self.lastMemberId
        member.location = location[0]
        self.members.append(member)
        self.habitat[location[0]].append(member)
        random.shuffle(self.members)
        random.shuffle(self.habitat[location[0]])
        self.updateIndex()
    def find(self):
        probability = random.randint(0, 100)
        if probability < 78 and len(self.members) > 0:
            item = random.choice(self.members)
            print('[', self.name, '] find:', item.species, 'id:', item.id, '-', item.forestID, '-', item.farmID)
        else:
            item = thing()
        return item
class farm(area):
    def __init__(self):
        super().__init__('farm')
        self.habitat = {'land':[],'soil':[],'pool':[]}
        for location in self.habitat:
            self.activity_range.add(location)
    def enter(self, member):
        range = self.activity_range.intersection(member.activity_range)
        if len(range) == 0:
            print('[', self.name, '] 交集:', len(range), member.species)
            return member
        elif len(range) == 1:
            location = next(iter(range))
        else:
            location = random.sample(range, 1)
            location = location[0]
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




farm = farm()
farm.addVegetable(10)
farm.addGrass(10)
farm.addCow(1)
for i in range(10):
    weight = random.uniform(0.9, 1.1)
    item = bird(weight, 'chicken')
    item.food = ['vegetable','worm','insect']
    item.activity_range = {'land'}
    farm.enter(item)
    
forest = forest()
forest.addTree(100)
forest.addWorm(100)
forest.addInsect(50)
forest.addDuck(10)
forest.addGrass(1000)

charlie = human(78, 'chalrie', 172, 'male')
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
    print('charlie prey:', item.species, 'id:', item.id, '-', item.forestID, '-', item.farmID)
    if item.species in charlie.food and meals.weight < 1:
        meal = charlie.cook(item)
        meals.add(meal)
    elif item.kingdom == 'animal' or item.species == 'grass':
        farm.enter(item)
    else:
        break
while len(meals.list):
    item = meals.remove()
    charlie.eat(item)
    # print('charlie eat:', item.species, item.weight, item.id)
# forest.exist()
# print('==============================================================')
# farm.exist()
# print('==============================================================')
charlie.farming(farm)