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
        super().__init__(weight, name)  # 使用 super() 繼承 father __init__ 裡所有屬性
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