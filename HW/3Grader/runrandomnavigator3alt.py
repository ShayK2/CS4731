# The version of runrandomnavigator3.py that is in the autograder.
# Slightly different than the student-provided runrandomnavigator3.py.

import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavmeshnavigator import *
			
			
			
			
nav = RandomNavMeshNavigator()
	
			
world = GameWorld(SEED, (1000,1000), (1000,1000))
agent = Agent(AGENT, (200, 100), 0, SPEED, world)
world.setPlayerAgent(agent)
polygons = [[(126, 160), (870, 260), (126, 320)],
                        [(38, 475), (265, 575), (38, 595)],
                        [(92, 800), (640, 870), (92, 960)],
                        [(974, 320), (220, 440), (560, 560), (380, 650), (974, 650)]]
world.initializeTerrain(polygons, (255, 0, 0), 2)
world.setPlayerAgent(agent)
agent.setNavigator(nav)
nav.setWorld(world)
world.initializeRandomResources(NUMRESOURCES)
world.debugging = True
world.run()
