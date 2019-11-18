import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from randomnavmeshnavigator import *
			
			
			
			
nav = RandomNavMeshNavigator()
	
			
world = GameWorld(SEED, (1000, 1000), (1000, 1000))
agent = Agent(AGENT, (200, 100), 0, SPEED, world)

world.initializeTerrain([[(320, 110), (480, 200), (370, 400), (100, 435), (180, 250)],
                         [(740, 160), (940, 450), (800, 540), (600, 410)],
                         [(285, 550), (400, 755), (150, 745)],
                         [(590, 750), (910, 720), (925, 870), (580, 870)]]) 
world.setPlayerAgent(agent)
agent.setNavigator(nav)
nav.setWorld(world)
world.initializeRandomResources(NUMRESOURCES)
world.debugging = True
world.run()
