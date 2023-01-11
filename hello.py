import random

class thing:
    def __init__(self, weight=0, species='nothing'):
        self.weight = float(weight)
        self.species = species
        self.id = 0
class forest:
    def __init__(self):
        self.habitat = []
    def enter(self, item):
        self.habitat.append(item)
        print('enter:', item.species, 'id:', item.id, 'gender:', item.gender)
    def leave(self):
        pass
    def exist(self):
        # species = []
        # for item in self.habitat:
        #     if species[item.species]:
        #         species[item.species] += 1
        #     else:
        #         species[item.species] = 1
        # for item in species:
        #     print('exist:', item)
        print('exist:', len(self.habitat), type(self.habitat))
    def find(self):
        probability = random.randint(0, 100)
        if probability < 50:
            item = random.choice(self.habitat)
            print('find:', item.species, 'id:', item.id)
            return item
        else:
            return thing()
class creature:
    def __init__(self, weight=0, species='creature'):
        self.mouth = 0
        self.water = float(0)
        self.species = species
        self.weight = float(weight)
        self.id = 0
        print(self.species, 'Weight:', self.weight)
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
            print(self.species, 'eat:', food.weight, 'weight:', self.weight)
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
        self.prey = []
        self.gender = gender
        self.food = ['vegetable','dock','chicken']
    def BMI(self):
        return self.weight / ((self.height/100)**2)
    def work(self):
        self.working_hour += 1
    def cook(self):
        meals = []
        while self.prey:
            self.working_hour += 1
            food = self.prey.pop()
            meals.append(food)
            self.sleepiness(0.1 * food.weight)
            print(self.name, 'cook:', food.species)
            print(self.name, 'has meals:', len(meals))
        return meals
    def hunt(self, forest):
        while self.working_hour <= self.max_working_hour:
            print('working_hour:', self.working_hour)
            print('max_working_hour:', self.max_working_hour)
            self.sleepiness(1)
            item = forest.find()
            print('charlie find:', item.species, 'id:', item.id)
            if item.species in self.food:
                self.prey.append(item)

forest = forest()
print('==============================================================')
for i in range(1, 1001):
    item = plant(0.1, 'vegetable')
    item.id = i
    forest.enter(item)
print('==============================================================')
for i in range(1001, 1101):
    weight = random.random()
    item = worm(weight)
    item.id = i
    forest.enter(item)
print('==============================================================')
for i in range(1101, 1201):
    item = insect(0.1)
    item.id = i
    forest.enter(item)
print('==============================================================')
for i in range(1201, 1211):
    item = duck(10)
    item.id = i
    forest.enter(item)
print('==============================================================')
for i in range(1201, 1211):
    item = bird(2, 'chicken')
    item.id = i
    item.food = ['vegetable','worm','insect']
    forest.enter(item)
print('==============================================================')

forest.exist()

charlie = human(78, 'chalrie', 172, 'male')
print(charlie.name, charlie.BMI())
charlie.hunt(forest)
meals = charlie.cook()
while meals:
    item = meals.pop()
    charlie.eat(item)
    print('charlie eat:', item.species, item.weight, item.id)