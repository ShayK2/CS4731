import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavmeshnavigator import *
			
			
			
			
nav = RandomNavMeshNavigator()
	
			
world = GameWorld(SEED, (1000, 1000), (1000, 1000))
agent = Agent(AGENT, (200, 100), 0, SPEED, world)
world.initializeTerrain([[(5, 160), (870, 260), (5, 320)],
                         [(5, 475), (265, 575), (5, 595)],
                         [(5, 800), (640, 870), (5, 960)],
                         [(974, 320), (220, 440), (560, 560), (380, 650), (974, 650)]])
world.setPlayerAgent(agent)
agent.setNavigator(nav)
nav.setWorld(world)
world.initializeRandomResources(NUMRESOURCES)
world.debugging = True
world.run()
