from agent import Agent
from point import Point

class Environment: 
    def __init__(self, width, height, agents = []):
        self.width = width
        self.height = height
        self.agents = agents
        self.build()
    
    def build(self):
        self.matrix = [['*'] * self.width for i in range(self.height)]
        for agent in self.agents:
            self.matrix[agent.getPosition().getX()][agent.getPosition().getY()] = 'X' 
    
    def draw(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
    
    def isAvailable(self, position):
        if position.getX() < 0 or position.getX() >= len(self.matrix):
            return False
        if position.getY() < 0 or position.getY() >= len(self.matrix[position.getX()]):
            return False
        return self.matrix[position.getX()][position.getY()] == '*'        


class VacuumWorld(Environment): 
    def __init__(self, cleaner):
        Environment.__init__(self, 2, 1, [cleaner])
        self.dirties = [Point(0,0), Point(0,1)]

    def getDirties(self):
        return self.dirties

    def suck(self, point):
        if self.contains(point):
            self.dirties = [dirtyPoint for dirtyPoint in self.dirties if not dirtyPoint.equals(point)]
            return True 
        else: 
            return False

    def contains(self, point):
        return [dirtyPoint for dirtyPoint in self.dirties if dirtyPoint.equals(point)]

    def draw(self):
        Environment.draw(self)
        print('| ', end='')
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.contains(Point(i, j)):
                    print('8', end=' ')
                else:
                    print('_', end=' ')

class DirtinessDetector:
    def isDirty(self, position):
        return self.env.contains(position)

    def setEnv(self, env):
        self.env = env
    
    def isAvailable(self, position):
        return self.env.isAvailable(position)

if __name__ == '__main__' :
    dirtinessDetector = DirtinessDetector()
    vacuumCleaner = Agent(0,0, [dirtinessDetector])
    smallField = VacuumWorld(vacuumCleaner)
    dirtinessDetector.setEnv(smallField)
    vacuumCleaner.setEnv(smallField)
    
    for i in range(1, 12):
        smallField.draw()
        vacuumCleaner.perform()

    for action in vacuumCleaner.history:
        print(action.toString())