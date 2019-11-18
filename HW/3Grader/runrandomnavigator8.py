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
polygons = [[(890.0, 320.0), (800.0, 480.0), (600.0, 370.0), (565.0, 100.0), (750.0, 180.0)], [(840.0, 740.0), (550.0, 940.0), (460.0, 800.0), (590.0, 600.0)], [(450.0, 285.0), (245.0, 400.0), (254.99999999999997, 150.0)], [(250.0, 590.0), (280.0, 910.0), (130.0, 925.0), (130.0, 580.0)]]
world.initializeTerrain(polygons, (255, 0, 0), 2)
world.setPlayerAgent(agent)
agent.setNavigator(nav)
nav.setWorld(world)
world.initializeRandomResources(NUMRESOURCES)
world.debugging = True
world.run()
