class creature:
    def __init__(self, weight=0, name='creature'):
        self.mouth = 0
        self.water = float(0)
        self.name = name
        self.weight = float(weight)
        print(self.name, 'Weight:', self.weight)
    def drink(self, water):
        self.water += float(water)
        
class plant(creature):
    def __init__(self, weight=0, name='plant'):
        super().__init__(weight, name) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.mouth = 0
        self.eye = 0
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
        print(self.name, seconds, 'water:', self.water, 'weight:', self.weight)

class animal(creature):
    def __init__(self, weight=0, name='animal'):
        super().__init__(weight, name) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.mouth = 1
        self.eye = 0
    def sleep(self):
        print(self.name, 'sleep')
    def see(self):
        if self.eye > 0:
            print(self.name, 'eye:', self.eye)
        else:
            print(self.name, 'Does not have eye')
    def eat(self, food):
        if self.mouth < 1:
            print(self.name, 'No mouth:', self.mouth)
        elif food.weight < 0:
            print(self.name, 'No food:', food.weight)
        else:
            self.weight += food.weight
            print(self.name, 'food:', food.weight)
            print(self.name, 'weight:', self.weight)
        
class bird(animal):
    def __init__(self, weight=0, name='bird'):
        super().__init__(weight, name) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.eye = 2
        self.wing = 2
        pass
        
class worm(animal):
    def __init__(self, weight=0, name='worm'):
        super().__init__(weight, name) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.eye = 0
        pass
    
class wing:
    def __init__(self):
        pass
    def fly(self):
        print(self.name, 'fly')
    
class insect(animal, wing):
    def __init__(self, weight=0, name='worm'):
        super().__init__(weight, name) # 使用 super() 繼承 father __init__ 裡所有屬性
        self.eye = 0
        
class duck(bird, wing):
    def __init__(self, weight=0, name='duck'):
        super().__init__(weight, name) # 使用 super() 繼承 father __init__ 裡所有屬性

class human(animal):
    def __init__(self, weight=0, name='human', height=0):
        super().__init__(weight, name)
        self.working_hour = 0
        self.height = height
    def BMI(self):
        return self.weight / ((self.height/100)**2)
    def work(self):
        self.working_hour += 1
        print(self.name, 'working:', self.working_hour)

print('==============================================================')
insect = insect(0.1)
print('==============================================================')
duck = duck(10)
duck.see()
duck.eat(insect)
duck.fly()
print('==============================================================')
vegetable = plant(0.1)
vegetable.drink(0.5)
vegetable.photosynthesis()
print('==============================================================')
worm = worm(0.2)
worm.see()
worm.eat(vegetable)
print('==============================================================')
chicken = bird(2, 'chicken')
chicken.sleep()
chicken.eat(worm)
# chicken.fly()
print('==============================================================')
charlie = human(78, 'chalrie', 172)
print(charlie.name, charlie.BMI())