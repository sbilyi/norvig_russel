from agent import Agent
from point import Point
from environment import Environment
from vacuum import VacuumWorld

if __name__ == '__main__' :
    vacummWorld = VacuumWorld()
    vacuumCleaner = Agent(0, 0, vacummWorld)

    for i in range(1, 12):
        print('{:3d}. '.format(i), end='')
        vacummWorld.draw()
        vacuumCleaner.perform()

    for action in vacuumCleaner.history:
        print(action.toString())