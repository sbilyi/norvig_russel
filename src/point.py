class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, point):
        if (self.getX() != point.getX() or self.getY() != point.getY()):
            return False
        else: 
            return True

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def toString(self):
        return "[{}:{}]".format(self.x, self.y)