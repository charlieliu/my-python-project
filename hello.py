import random

class thing:
    def __init__(self, weight=0, species='nothing'):
        self.weight = float(weight)
        self.name = 'nothing'
        self.kingdom = 'nothing'
        self.species = species
        self.id = 0
class area:
    def __init__(self, name = 'area'):
        self.members = []
        self.name = name
        self.lastMemberId = 0
    def updateIndex(self):
        for idx, member in enumerate(self.members):
            member.idx = idx
    def exist(self):
        for item in self.members:
            print('[', self.name, '] exist:', item.species, 'idx:', item.idx, 'id:', item.id)
class farm(area):
    def __init__(self):
        super().__init__('farm')
        self.habitat = {'coop':[],'soil':[],'pool':[]}
    def enter(self, item):
        self.lastMemberId += 1
        item.id = self.lastMemberId
        item.farmID = self.lastMemberId
        self.members.append(item)
        print('[', self.name, '] new member:', item.species, 'id:', item.id, 'gender:', item.gender)
        self.updateIndex()
    def leave(self, idx):
        item = self.members[idx]
        del self.members[idx]
        self.updateIndex()
        print('[', self.name, '] leave member:', item.species, 'id:', item.id, 'gender:', item.gender)
    def feed(self):
        for member in self.members:
            if member.species == 'animal':
                member.weight += 0.1 * member.weight
                print('[', self.name, '] exist:', item.species, 'id:', item.id, 'gender:', item.gender)
class forest(area):
    def __init__(self):
        super().__init__('forest')
        self.habitat = {'surface':[],'soil':[],'lake':[]}
    def enter(self, item):
        self.lastMemberId += 1
        item.id = self.lastMemberId
        item.forestID = self.lastMemberId
        self.members.append(item)
        random.shuffle(self.members)
        self.updateIndex()
    def leave(self, idx):
        item = self.members[idx]
        del self.members[idx]
        self.updateIndex()
        print('[', self.name, '] leave member:', item.species, 'id:', item.id, 'gender:', item.gender)
    def find(self):
        probability = random.randint(0, 100)
        if probability < 78:
            item = random.choice(self.members)
        else:
            item = thing()
        print('[', self.name, '] find:', item.species, 'id:', item.id, 'has', len(self.members), 'members')
        return item
class creature:
    def __init__(self, weight=0, species='creature'):
        self.mouth = 0
        self.water = float(0)
        self.species = species
        self.weight = float(weight)
        self.id = 0
        # print(self.species, 'Weight:', self.weight)
    def drink(self, water):
        self.water += float(water)
class plant(creature):
    def __init__(self, weight=0, species='plant'):
        super().__init__(weight, species) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.mouth = 0
        self.eye = 0
        self.kingdom = 'plant'
        self.gender = ''
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
            print(self.species, 'need sleep')
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
class insect(animal):
    def __init__(self, weight=0):
        super().__init__(weight, 'insect') # 使用 super() 繼承 father __init__ 裡所有屬性
        self.wing = 4
        self.leg = 2
        self.food = ['vegetable']
class duck(bird):
    def __init__(self, weight=0):
        super().__init__(weight, 'duck') # 使用 super() 繼承 father __init__ 裡所有屬性
        self.wing = 2
        self.leg = 2
        self.food = ['vegetable','worm','insect']
class human(animal):
    def __init__(self, weight=0, name='', height=0, gender=''):
        super().__init__(weight, 'human')
        self.name = name
        self.height = height
        self.eye = 2
        self.max_working_hour = float(8)
        self.gender = gender
        self.food = ['vegetable','duck','chicken']
    def BMI(self):
        return self.weight / ((self.height/100)**2)
    def work(self):
        self.working_hour += 1
    def cook(self, ingredients):
        self.sleepiness(0.1 * ingredients.weight)
        return ingredients
    def hunt(self, forest):
        prey = {'food':[],'others':[]}
        working_hour = 0.1
        while (self.working_hour + working_hour) < self.max_working_hour:
            item = forest.find()
            for i in self.food:
                print('species', item.species, 'check:', i, 'result:', i == item.species)
            print('in list:', item.species in self.food)
            if item.species in self.food:
                forest.leave(item.idx)
                prey['food'].append(item)
                print('food:', item.species, 'kingdom:', item.kingdom)
            elif item.kingdom == 'animal':
                forest.leave(item.idx)
                prey['others'].append(item)
                print('others:', item.species, 'kingdom:', item.kingdom)
            self.sleepiness(working_hour)
        print('working_hour:', self.working_hour, '/', self.max_working_hour)
        print('charlie food:', len(prey['food']), 'others:', len(prey['others']))
        return prey


forest = forest()
for i in range(1000):
    item = plant(0.1, 'tree')
    forest.enter(item)
for i in range(100):
    weight = random.uniform(0.01, 0.1)
    item = worm(weight)
    forest.enter(item)
for i in range(100):
    weight = random.random()
    item = insect(weight)
    forest.enter(item)
for i in range(100):
    weight = random.uniform(0.1, 3)
    item = duck(weight)
    forest.enter(item)
# forest.exist()
print('==============================================================')
farm = farm()
for i in range(100):
    item = plant(0.1, 'vegetable')
    farm.enter(item)
for i in range(10):
    weight = random.uniform(0.9, 1.1)
    item = bird(weight, 'chicken')
    item.food = ['vegetable','worm','insect']
    farm.enter(item)
# farm.exist()
print('==============================================================')

charlie = human(78, 'chalrie', 172, 'male')
print(charlie.name, charlie.BMI())
meals = []
meals_weight = 0
prey = charlie.hunt(forest)
print('charlie find food:', len(prey['food']), 'others:', len(prey['others']))
while prey['food']:
    ingredients = prey['food'].pop()
    meal = charlie.cook(ingredients)
    if meals_weight < 1:
        meals_weight += meal.weight
        meals.append(meal)
        print('charlie cook:', meal.species, 'has meals:', len(meals))
while prey['food']:
    item = prey['food'].pop()
    farm.enter(item)
while prey['others']:
    item = prey['others'].pop()
    farm.enter(item)
while meals:
    item = meals.pop()
    charlie.eat(item)
    # print('charlie eat:', item.species, item.weight, item.id)