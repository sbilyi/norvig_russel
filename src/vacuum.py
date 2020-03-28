from environment import Environment
from point import Point

class VacuumWorld(Environment): 
    def __init__(self):
        Environment.__init__(self, 2, 1)
        self.dirties = [Point(0,0), Point(0,1)]

    def register(self, agent):
        self.agents.append(agent)
        
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

