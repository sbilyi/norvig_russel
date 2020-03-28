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
