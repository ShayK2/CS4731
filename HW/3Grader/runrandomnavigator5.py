import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavmeshnavigator import *
			
			
			
			
nav = RandomNavMeshNavigator()
	
			
world = GameWorld(SEED, (1000,1000), (1000,1000))
agent = Agent(AGENT, (500, 500), 0, SPEED, world)
world.setPlayerAgent(agent)
polygons = [[(900.0, 150.0), (900.0, 390.0), (850.0, 390.0), (780.0, 295.0), (720.0, 295.0), (650.0, 390.0), (600.0, 390.0), (600.0, 150.0)], [(910.0, 850.0), (910.0, 610.0), (860.0, 610.0), (790.0, 705.0), (730.0, 705.0), (660.0, 610.0), (610.0, 610.0), (610.0, 850.0)], [(435.0, 100.0), (435.0, 340.0), (167.0, 340.0), (167.0, 100.0)], [(415.0, 900.0), (415.0, 660.0), (187.0, 660.0), (187.0, 900.0)]]
world.initializeTerrain(polygons, (255, 0, 0), 2)
world.setPlayerAgent(agent)
agent.setNavigator(nav)
nav.setWorld(world)
world.initializeRandomResources(NUMRESOURCES)
world.debugging = True
world.run()
