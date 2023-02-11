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