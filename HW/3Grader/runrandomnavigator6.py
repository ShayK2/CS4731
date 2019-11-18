import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavmeshnavigator import *
			
			
			
			
nav = RandomNavMeshNavigator()
	
			
world = GameWorld(SEED, (1000,1000), (1000,1000))
agent = Agent(AGENT, (200, 200), 0, SPEED, world)
world.setPlayerAgent(agent)
polygons = [[(580.0, 180.0), (725.0, 360.0), (629.0, 680.0), (340.0, 630.0), (303.0, 380.0)]]
world.initializeTerrain(polygons, (255, 0, 0), 2)
world.setPlayerAgent(agent)
agent.setNavigator(nav)
nav.setWorld(world)
world.initializeRandomResources(NUMRESOURCES)
world.debugging = True
world.run()
