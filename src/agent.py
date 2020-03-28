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

class DirtinessDetector:
    def __init__(self, environment):
        self.environment = environment

    def isDirty(self, position):
        return self.environment.contains(position)

    def isAvailable(self, position):
        return self.environment.isAvailable(position)

class Agent: 
    def __init__(self, x, y, environment):
        self.position = Point(x, y)
        self.history = []
        self.environment = environment
        self.environment.register(self)
        self.dirtinessDetector = DirtinessDetector(self.environment)
        
    def getPosition(self):
        return self.position
    
    def perform(self):
        position = self.position
        if self.dirtinessDetector.isDirty(self.getPosition()):
            self.environment.suck(self.position)
            self.history.append(Entry(position, 'Dirty','Suck'))
        else :
            direction = self.move()
            self.history.append(Entry(position, 'Clean', direction))
        print('')


    def move(self):
        position = Point(self.getPosition().getX(), self.getPosition().getY() - 1)
        result = 'None'
        if self.dirtinessDetector.isAvailable(position):
            self.position = position
            result = 'Left'
        else:
            position = Point(self.getPosition().getX(), self.getPosition().getY() + 1)
            if self.dirtinessDetector.isAvailable(position):
                self.position = position
            result = 'Right'
            # else:
                # raise Exception('There is nowhere to move')
        self.environment.build()
        return result