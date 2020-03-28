class Environment: 
    def __init__(self, width, height) :
        self.__init__(width, height, [])

    def __init__(self, width, height, agents) :
        self.width = width
        self.height = height
        self.agents = agents
        self.build()
    
    def build(self):
        self.matrix = [['*'] * self.width for i in range(self.height)]
        for agent in self.agents:
            self.matrix[agent.getXPosition()][agent.getYPosition()] = 'X' 
    
    def draw(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print('')

    
class Agent: 
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def getXPosition(self):
        return self.x
    
    def getYPosition(self):
        return self.y

if __name__ == '__main__' :
    smallField = Environment(10, 10, [Agent(5,8)])
    smallField.draw()