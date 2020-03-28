from point import Point
  
class Entry:
    def __init__(self, position, state, action):
        self.position = position
        self.state = state
        self.action = action 

    def draw(self):
        print('[' + self.position.getX() + ":" + self.position.getY() + ", " + self.state + ']=' + self.action)    
    
    def toString(self):
        return "[ {}:{}, {}]={}".format(self.position.getX(), self.position.getY(), self.state, self.action) 
    
class SenseHistory:
    def __init__(self):
        self.data = []
    def save(self, sesnor, act):
        print('x')

class Agent: 
    def __init__(self, x, y, sensors=[]):
        self.position = Point(x, y)
        self.sensors = sensors
        self.history = []

    def setEnv(self, env):
        self.env = env

    def getPosition(self):
        return self.position
    
    def perform(self):
        position = self.position
        if self.sensors[0].isDirty(self.getPosition()):
            self.env.suck(self.position)
            self.history.append(Entry(position, 'Dirty','Suck'))
        else :
            direction = self.move()
            self.history.append(Entry(position, 'Clean', direction))
        print('')


    def move(self):
        position = Point(self.getPosition().getX(), self.getPosition().getY() - 1)
        if self.sensors[0].isAvailable(position):
            self.position = position
            return 'Left'
        else:
            position = Point(self.getPosition().getX(), self.getPosition().getY() + 1)
            if self.sensors[0].isAvailable(position):
                self.position = position
            return 'Right'
            # else:
                # raise Exception('There is nowhere to move')
        self.env.build()