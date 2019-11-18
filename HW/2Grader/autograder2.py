import os

os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
pygame.init()
pygame.display.set_mode((1,1))

import sys, math, numpy, random, time, copy, traceback
from pygame.locals import *

from constants import *
from utils import *
from core import *
from timeoutfunction import TimeoutFunctionException

import imp

def importMyBuildPathnetwork(classFile):
	print "ClassFile: "+str(classFile)
	if classFile:
		classFile += "/"
	minion = imp.load_source('module', classFile + "mybuildpathnetwork.py")
	return minion

class AutoGrader:
	def testBuildPathNetwork(self, mybuildpathnetwork, pathnodes, world, agent, expectedNodes = -1):
		if (expectedNodes == -1):
			expectedNodes = len(pathnodes)
		try:
			tmpPathNodes = list(pathnodes)
			edges = mybuildpathnetwork.myBuildPathNetwork(tmpPathNodes, world, agent)
			#grade = getReachabilityGrade1(pathnodes, edges, world, pairsToCheck)
			grade = getReachabilityGrade(pathnodes, edges, world, expectedNodes)
			return grade
		except TimeoutFunctionException:
			raise TimeoutFunctionException
		except:
			print("Error occurred in user code.")
			traceback.print_exc()
			return 0

	def runAutoGrader(self, classFile):
		#Grab pathnetwork maker
		mybuildpathnetwork = importMyBuildPathnetwork(classFile)

		if not mybuildpathnetwork == None:

			grade = 0
			sumOfReachGrades = 0.0

			# Map 0
			polygons = [[(628, 698), (582, 717), (549, 688), (554, 566), (676, 548)], [(942, 484), (811, 396), (843, 299), (921, 300)], [(457, 422), (381, 490), (300, 515), (310, 400), (454, 350)]]
			world = GameWorld(SEED, (1224, 900), (1224, 900))
			agent = Agent(AGENT, (SCREEN[0]/2, SCREEN[1]/2), 0, SPEED, world)
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			world.setPlayerAgent(agent)
			pathnodes = [(400, 600), (650, 400), (650, 200), (1075, 150), (100, 200), (100, 500), (1000, 700), (450, 800)]
			grade = self.testBuildPathNetwork(mybuildpathnetwork, pathnodes, world, agent)
			sumOfReachGrades+=grade
			print "Map 0 Grade "+ str(grade)

			#1 Map 1
			polygons = [[(150, 100), (390, 100), (390, 150), (295, 220), (295, 280), (390, 350), (390, 400), (150, 400)],
								 [(850, 90), (610, 90), (610, 140), (705, 210), (705, 270), (610, 340), (610, 390), (850, 390)],
								 [(100, 565), (340, 565), (340, 833), (100, 833)],
								 [(900, 585), (660, 585), (660, 813), (900, 813)]]
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (500, 500), 0, SPEED, world)
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			world.setPlayerAgent(agent)
			pathnodes = [(50, 40), (500, 50), (950, 40), (500, 500), (380, 250), (620, 250), (30, 510), (970, 510), (50, 950), (950, 950), (500, 930), (525, 275)]
			grade = self.testBuildPathNetwork(mybuildpathnetwork, pathnodes, world, agent)
			sumOfReachGrades+=grade
			print "Map 1 Grade "+ str(grade)

			#2 Map 2
			polygons = [[(180, 420), (360, 275), (680, 371), (630, 660), (380, 697)]]
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (200, 200), 0, SPEED, world)
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			world.setPlayerAgent(agent)
			pathnodes = [(100, 200), (800, 800), (100, 800), (800, 200)]
			grade = self.testBuildPathNetwork(mybuildpathnetwork, pathnodes, world, agent)
			sumOfReachGrades+=grade
			print "Map 2 Grade "+ str(grade)

			# Map 3
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (200, 100), 0, SPEED, world)
			polygons = [[(5, 160), (670, 260), (5, 320)],
									 [(5, 475), (265, 575), (5, 595)],
									 [(5, 800), (640, 870), (5, 960)],
									 [(974, 320), (220, 440), (560, 560), (380, 650), (974, 650)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			world.setPlayerAgent(agent)
			pathnodes = [(200, 100), (900, 100), (950, 290), (75, 400), (375, 575), (200, 700), (900, 800), (900, 950), (600, 950)]
			grade = self.testBuildPathNetwork(mybuildpathnetwork, pathnodes, world, agent)
			sumOfReachGrades+=grade
			print "Map 3 Grade "+ str(grade)

			# Map 4
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (200, 100), 0, SPEED, world)
			polygons = [[(320, 110), (480, 200), (370, 400), (100, 435), (180, 250)],
								 [(740, 160), (940, 450), (800, 540), (600, 410)],
								 [(285, 550), (400, 755), (150, 745)],
								 [(590, 750), (910, 720), (925, 870), (580, 870)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			world.setPlayerAgent(agent)
			pathnodes = [(50, 50), (600, 50), (50, 550), (500, 450), (900, 175), (75, 900), (450, 950), (700, 650), (950, 650), (850, 940)]
			grade = self.testBuildPathNetwork(mybuildpathnetwork, pathnodes, world, agent)
			sumOfReachGrades+=grade
			print "Map 4 Grade "+ str(grade)

			# Map 5
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (500, 500), 0, SPEED, world)
			polygons = [[(900.0, 150.0), (900.0, 390.0), (850.0, 390.0), (780.0, 295.0), (720.0, 295.0), (650.0, 390.0), (600.0, 390.0), (600.0, 150.0)], [(910.0, 850.0), (910.0, 610.0), (860.0, 610.0), (790.0, 705.0), (730.0, 705.0), (660.0, 610.0), (610.0, 610.0), (610.0, 850.0)], [(435.0, 100.0), (435.0, 340.0), (167.0, 340.0), (167.0, 100.0)], [(415.0, 900.0), (415.0, 660.0), (187.0, 660.0), (187.0, 900.0)]]
			pathnodes = [(77, 52), (509, 47), (952, 69), (950, 494), (515, 475), (510, 222), (272, 488), (66, 422), (87, 960) ,(502, 920), (963, 950)]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			world.setPlayerAgent(agent)
			grade = self.testBuildPathNetwork(mybuildpathnetwork, pathnodes, world, agent)
			sumOfReachGrades+=grade
			print "Map 5 Grade "+ str(grade)


			# Map 6
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (500, 500), 0, SPEED, world)
			polygons = [[(840.0, 126.0), (740.0, 870.0), (680.0, 126.0)], [(525.0, 38.0), (425.0, 265.0), (405.0, 38.0)], [(200.0, 92.0), (130.0, 640.0), (40.0, 92.0)], [(680.0, 974.0), (560.0, 220.0), (440.0, 560.0), (350.0, 380.0), (350.0, 974.0)]]
			pathnodes = [(952, 69), (950, 494), (510, 222), (272, 488), (40, 422), (87, 960), (963, 950), (299, 61), (290, 294), (428, 365), (619, 54), (665, 595)]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			world.setPlayerAgent(agent)
			grade = self.testBuildPathNetwork(mybuildpathnetwork, pathnodes, world, agent, 12)
			sumOfReachGrades+=grade
			print "Map 6 Grade "+ str(grade)


			#7
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (500, 500), 0, SPEED, world)
			polygons = [[(890.0, 320.0), (800.0, 480.0), (600.0, 370.0), (565.0, 100.0), (750.0, 180.0)], [(840.0, 740.0), (550.0, 940.0), (460.0, 800.0), (590.0, 600.0)], [(450.0, 285.0), (245.0, 400.0), (254.99999999999997, 150.0)], [(250.0, 590.0), (280.0, 910.0), (130.0, 925.0), (130.0, 580.0)]]
			pathnodes = [(77, 52), (509, 47), (952, 119), (950, 494), (515, 475), (510, 222), (272, 488), (66, 422), (87, 960) , (963, 950), (428, 365), (665, 595)]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			world.setPlayerAgent(agent)
			grade = self.testBuildPathNetwork(mybuildpathnetwork, pathnodes, world, agent, 12)
			sumOfReachGrades+=grade
			print "Map 7 Grade "+ str(grade)


			#End Stuff
			reachGrade = 5.0*(sumOfReachGrades/8.0)
			print "Grade: "+str(reachGrade)
		else:
			print "Import student code failed"
			reachGrade = 0
		self.buildpathnetwork = None

		#sys.path.remove(classFile)
		print "Grade: "+str(reachGrade)
		return reachGrade

def computePath(pathnodes, pathnetwork, world, source, dest):
		# Make sure that the pathnodes have been created.
		start = findClosestUnobstructed(source, pathnodes, world.getLines())
		end = findClosestUnobstructed(dest, pathnodes, world.getLines())
		current = start
		path = [current]
		count = 0
		last = current
		successors = []
		while current != end and count < 100:
			count = count + 1

			for l in pathnetwork:
				if l[0] == current and l[1] != last and not l[1] in successors:
					successors.append(l[1])
				elif l[1] == current and l[0] != last and not l[0] in successors:
					successors.append(l[0])
			last = current
			best = None
			dist = 0
			for s in successors:
				d = distance(s, dest)
				if (best == None or d < dist) and not s in path:
					best = s
					dist = d


			if not best==None:
				current = best
				path.append(current)

		return path

def getReachabilityGrade(pathnodes, edges, world, expectedNodes):
	points = min(5.0, float(expectedNodes)-1.0)
	obstacleLines = []
	for o in world.getObstacles():
		for oLine in o.getLines():
			obstacleLines.append(oLine)

	validEdges = [edge for edge in edges if rayTraceWorld(edge[0], edge[1], obstacleLines)==None]
	invalidEdges = len(edges) - len(validEdges)
	edges = validEdges

	if invalidEdges > 0:
		print "invalidEdges:" + str(invalidEdges)

	maxSet = 0
	nodesSet = set(pathnodes)
	for node in pathnodes:
		intersect = set.intersection(nodesSet,dfs(node, edges))
		maxSet = max(len(intersect), maxSet)

	missing = abs(expectedNodes - maxSet)
	if missing > 0:
		print "Nodes not connected:" + str(missing)

	return max(0, (points-missing - invalidEdges)/points)

def dfs(node, edges):
	explored = set()
	unexplored = [node]
	while unexplored:
		current = unexplored.pop()
		if current in explored:
			continue
		explored.add(current)

		for l in edges:
			if l[0] == current:
				unexplored.append(l[1])
			elif l[1] == current:
				unexplored.append(l[0])
	return explored


#Determines the reachability for one world at a time
def getReachabilityGrade1(pathnodes, pathnetwork, world, pairsToCheck):
	sumOfAttempts = 0.0

	if len(pathnodes)==0:
		#print "No pathnodes"
		return 0

	obstacleLines = []

	for o in world.getObstacles():
		for oLine in o.getLines():
			obstacleLines.append(oLine)

	for pair in pairsToCheck:
		path = computePath(pathnodes, pathnetwork, world, pair[0], pair[1])
		#print "Attempting to path: "+str(pair)
		#print "Got path: "+str(path)
		if len(path)>=1:
			bestIndex = 0
			dist = None

			for index in range(len(path)):
				if not path[index]==None:
					newDist = distance(path[index],  pair[1])
					if dist==None or newDist<dist:
						dist = newDist
						bestIndex = index

			if not path[bestIndex] == None:
				hit = rayTraceWorld(path[bestIndex], pair[1], obstacleLines)
				hit2 = rayTraceWorld(path[len(path)-1], pair[1], obstacleLines)
				if hit == None or hit2==None:
					sumOfAttempts+=1.0


	#print "Sum of Attempts: "+str(sumOfAttempts)
	gradeForThesePoints = (sumOfAttempts/len(pairsToCheck))
	#print "Reach Grade: "+str(gradeForThesePoints)
	return gradeForThesePoints








