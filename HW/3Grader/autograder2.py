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

class AutoGrader:
	def runAutoGrader(self, classFile):
		grade = 0

		# If blank, use root mycreatepathnetwork.py.
		if classFile:
			classFile += "/"
		self.gridnav= imp.load_source('module.name', classFile+"mycreatepathnetwork.py")

		if not self.gridnav==None:
			allMeshes = []
			sumOfReachGrades = 0.0
			sumOfMapCoverageGrades = 0.0

			#1
			mapNumber = 1
			print "==Map " + str(mapNumber) + "=="
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (500, 500), 0, SPEED, world)
			world.setPlayerAgent(agent)
			polygons = [[(150, 100), (390, 100), (390, 150), (295, 220), (295, 280), (390, 350), (390, 400), (150, 400)],
			                     [(850, 90), (610, 90), (610, 140), (705, 210), (705, 270), (610, 340), (610, 390), (850, 390)],
			                     [(100, 565), (340, 565), (340, 833), (100, 833)],
			                     [(900, 585), (660, 585), (660, 813), (900, 813)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2, TREE)
			nodes, edges, polys = self.tryCreatePathNetwork(world, agent)
			allMeshes.append(polys)
			mapReachGrade = getReachabilityGrade(nodes,edges, world,[((500,100), (500,900)),
																((30,30), (970,970)),
																((500,500), (30,30)),
																((30,30), (970,30))],
																mapNumber)
			sumOfReachGrades+=mapReachGrade
			mapCoverageGrade = getCoverageGrade(world, polys)
			sumOfMapCoverageGrades += mapCoverageGrade
			print "Map reachability grade:", mapReachGrade
			print "Map coverage grade:", mapCoverageGrade
			#print "Sum Of Reach Grade: "+ str(sumOfReachGrades)

			#2
			mapNumber += 1
			print "==Map " + str(mapNumber) + "=="
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (200, 200), 0, SPEED, world)
			world.setPlayerAgent(agent)
			polygons = [[(180, 420), (360, 275), (680, 371), (630, 660), (380, 697)]]

			world.initializeTerrain(polygons, (255, 0, 0), 2)
			nodes, edges, polys = self.tryCreatePathNetwork(world, agent)
			allMeshes.append(polys)
			mapReachGrade = getReachabilityGrade(nodes,edges, world,[((30,100), (500,100)),
																((30,30), (970,970)),
																((970,30), (30,30)),
																((30,30), (970,30))],
																mapNumber)
			sumOfReachGrades+=mapReachGrade
			mapCoverageGrade = getCoverageGrade(world, polys)
			sumOfMapCoverageGrades += mapCoverageGrade
			print "Map reachability grade:", mapReachGrade
			print "Map coverage grade:", mapCoverageGrade

			#print "Sum Of Reach Grade: "+ str(sumOfReachGrades)
			#3
			mapNumber += 1
			print "==Map " + str(mapNumber) + "=="
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (200, 100), 0, SPEED, world)
			world.setPlayerAgent(agent)
			polygons = [[(126, 160), (870, 260), (126, 320)],
			                     [(38, 475), (265, 575), (38, 595)],
			                     [(92, 800), (640, 870), (92, 960)],
			                     [(974, 320), (220, 440), (560, 560), (380, 650), (974, 650)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			nodes, edges, polys = self.tryCreatePathNetwork(world, agent)
			allMeshes.append(polys)
			mapReachGrade = getReachabilityGrade(nodes,edges, world,[((500,50), (500,950)),
																((500,50), (50,0)),
																((500,950), (500,50)),
																((500,950), (300,580))],
																mapNumber)
			sumOfReachGrades+=mapReachGrade
			mapCoverageGrade = getCoverageGrade(world, polys)
			sumOfMapCoverageGrades += mapCoverageGrade
			print "Map reachability grade:", mapReachGrade
			print "Map coverage grade:", mapCoverageGrade

			#print "Sum Of Reach Grade: "+ str(sumOfReachGrades)
			#4
			mapNumber += 1
			print "==Map " + str(mapNumber) + "=="
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (200, 100), 0, SPEED, world)
			world.setPlayerAgent(agent)
			polygons = [[(320, 110), (480, 200), (370, 400), (100, 435), (180, 250)],
			                     [(740, 160), (940, 450), (800, 540), (600, 410)],
			                     [(285, 550), (400, 755), (150, 745)],
			                     [(590, 750), (910, 720), (925, 870), (580, 870)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			nodes, edges, polys = self.tryCreatePathNetwork(world, agent)
			allMeshes.append(polys)
			mapReachGrade = getReachabilityGrade(nodes,edges, world,[((500,50), (950,950)),
													((500,50), (50,0)),
													((950,950), (500,50)),
													((950,950), (400,580))],
																mapNumber)
			sumOfReachGrades+=mapReachGrade
			mapCoverageGrade = getCoverageGrade(world, polys)
			sumOfMapCoverageGrades += mapCoverageGrade
			print "Map reachability grade:", mapReachGrade
			print "Map coverage grade:", mapCoverageGrade


			#5
			mapNumber += 1
			print "==Map " + str(mapNumber) + "=="
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (500, 500), 0, SPEED, world)
			world.setPlayerAgent(agent)
			polygons = [[(900.0, 150.0), (900.0, 390.0), (850.0, 390.0), (780.0, 295.0), (720.0, 295.0), (650.0, 390.0), (600.0, 390.0), (600.0, 150.0)], [(910.0, 850.0), (910.0, 610.0), (860.0, 610.0), (790.0, 705.0), (730.0, 705.0), (660.0, 610.0), (610.0, 610.0), (610.0, 850.0)], [(435.0, 100.0), (435.0, 340.0), (167.0, 340.0), (167.0, 100.0)], [(415.0, 900.0), (415.0, 660.0), (187.0, 660.0), (187.0, 900.0)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			nodes, edges, polys = self.tryCreatePathNetwork(world, agent)
			allMeshes.append(polys)
			mapReachGrade = getReachabilityGrade(nodes,edges, world,[((500,100), (500,900)),
																((30,30), (970,970)),
																((500,500), (30,30)),
																((30,30), (970,30))],
																mapNumber)
			sumOfReachGrades+=mapReachGrade
			mapCoverageGrade = getCoverageGrade(world, polys)
			sumOfMapCoverageGrades += mapCoverageGrade
			print "Map reachability grade:", mapReachGrade
			print "Map coverage grade:", mapCoverageGrade


			#6
			mapNumber += 1
			print "==Map " + str(mapNumber) + "=="
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (200, 200), 0, SPEED, world)
			world.setPlayerAgent(agent)
			polygons = [[(580.0, 180.0), (725.0, 360.0), (629.0, 680.0), (340.0, 630.0), (303.0, 380.0)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			nodes, edges, polys = self.tryCreatePathNetwork(world, agent)
			allMeshes.append(polys)
			mapReachGrade = getReachabilityGrade(nodes,edges, world,[((30,100), (500,100)),
																((30,30), (970,970)),
																((970,30), (30,30)),
																((30,30), (970,30))],
																mapNumber)
			sumOfReachGrades+=mapReachGrade
			mapCoverageGrade = getCoverageGrade(world, polys)
			sumOfMapCoverageGrades += mapCoverageGrade
			print "Map reachability grade:", mapReachGrade
			print "Map coverage grade:", mapCoverageGrade



			#7
			mapNumber += 1
			print "==Map " + str(mapNumber) + "=="
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (300, 300), 0, SPEED, world)
			world.setPlayerAgent(agent)
			polygons = [[(840.0, 126.0), (740.0, 870.0), (680.0, 126.0)], [(525.0, 38.0), (425.0, 265.0), (405.0, 38.0)], [(200.0, 92.0), (130.0, 640.0), (40.0, 92.0)], [(680.0, 974.0), (560.0, 220.0), (440.0, 560.0), (350.0, 380.0), (350.0, 974.0)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			nodes, edges, polys = self.tryCreatePathNetwork(world, agent)
			allMeshes.append(polys)
			mapReachGrade = getReachabilityGrade(nodes,edges, world,[((950.0, 500.0), (50.0, 950.0)), ((950.0, 500.0), (1000.0, 49.99999999999994)), ((50.0, 950.0), (950.0, 500.0)), ((50.0, 950.0), (420.0, 300.0))],
																mapNumber)
			sumOfReachGrades+=mapReachGrade
			mapCoverageGrade = getCoverageGrade(world, polys)
			sumOfMapCoverageGrades += mapCoverageGrade
			print "Map reachability grade:", mapReachGrade
			print "Map coverage grade:", mapCoverageGrade



			#8
			mapNumber += 1
			print "==Map " + str(mapNumber) + "=="
			world = GameWorld(SEED, (1000,1000), (1000,1000))
			agent = Agent(AGENT, (500, 500), 0, SPEED, world)
			world.setPlayerAgent(agent)
			polygons = [[(890.0, 320.0), (800.0, 480.0), (600.0, 370.0), (565.0, 100.0), (750.0, 180.0)], [(840.0, 740.0), (550.0, 940.0), (460.0, 800.0), (590.0, 600.0)], [(450.0, 285.0), (245.0, 400.0), (254.99999999999997, 150.0)], [(250.0, 590.0), (280.0, 910.0), (130.0, 925.0), (130.0, 580.0)]]
			world.initializeTerrain(polygons, (255, 0, 0), 2)
			nodes, edges, polys = self.tryCreatePathNetwork(world, agent)
			allMeshes.append(polys)
			mapReachGrade = getReachabilityGrade(nodes,edges, world,[((30,100), (500,500)),
																((30,30), (800,700)),
																((500,30), (500,970)),
																((30,30), (970,30))],
																mapNumber)
			sumOfReachGrades+=mapReachGrade
			mapCoverageGrade = getCoverageGrade(world, polys)
			sumOfMapCoverageGrades += mapCoverageGrade
			print "Map reachability grade:", mapReachGrade
			print "Map coverage grade:", mapCoverageGrade


			print "==Mesh optimization=="
			meshGrade = getMeshGrade(allMeshes)
			print "Mesh grade:", meshGrade
			#print "Mesh Grade: "+str(meshGrade)
			reachGrade = 6.0*(sumOfReachGrades/8.0)
			coverageGrade = 2.0 * (sumOfMapCoverageGrades/8.0)

			grade = meshGrade + reachGrade + coverageGrade


		self.gridnav = None


		#sys.path.remove(classFile)
		comment = "Reachability: " + str(reachGrade) + "/6 points, "
		comment += "Coverage: " + str(coverageGrade) + "/2 points, "
		comment += "Mesh optimization: " + str(float(meshGrade)) + "/2 points, "
		comment += "Total grade: "+str(grade)
		print comment
		return grade, comment

	def tryCreatePathNetwork(self, world, agent):
		try:
			nodes, edges, polys = self.gridnav.myCreatePathNetwork(world, agent)
		except TimeoutFunctionException:
			raise TimeoutFunctionException
		except:
			traceback.print_exc()
			nodes = []
			edges = []
			polys = []
		return nodes, edges, polys


# calculate the coverage grade (between 0 and 1) for this world based on the area covered by the path network
def getCoverageGrade(world, polys):
	worldArea = calculateWorldArea(world)
	#print("world area = " + str(worldArea))
	obstaclesArea = calculateObstaclesArea(world)
	#print("obstacles area = " + str(obstaclesArea))
	networkArea = calculateNetworkArea(polys)
	emptyArea = worldArea - obstaclesArea
	#print "Area: " + str(networkArea), str(emptyArea)

	coverageGrade = (1.0 - abs(1.0 - networkArea/emptyArea))
	coverageGrade = numpy.clip(coverageGrade, 0.0, 1.0)

	return coverageGrade

# calculate the total area of the path network's poylgons
def calculateNetworkArea(polys):
	networkArea = 0.0
	for poly in polys:
		networkArea += calculatePolyArea(poly)

	return networkArea

# calculate the total area of all obstacles
def calculateObstaclesArea(world):
	obstaclesArea = 0
	for o in world.obstacles:
		obstaclesArea += calculatePolyArea(o.getPoints())

	return obstaclesArea

# calculate the area of a single polygon
def calculatePolyArea(poly):
	area = 0.0
	j = len(poly)-1 	# index of previous point starts at last point
	for i in range (0, len(poly)):
		this_point = poly[i]
		last_point = poly[j]
		area += (last_point[0] + this_point[0]) * (last_point[1] - this_point[1])
		j = i

	return abs(area/2)

# calculate the area of this world map
def calculateWorldArea(world):
	dimensions = world.getDimensions()
	return dimensions[0] * dimensions[1]

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

# Get a list of lists of polygons that are the meshes
def getMeshGrade(allMeshes):
	hitNotConvex = False
	sizeFour = False
	sizeFive = False

	for navmesh in allMeshes:
		for polygon in navmesh:
			if not isConvex(polygon):

				hitNotConvex=True
			if len(polygon)>=4:
				sizeFour = True
			if len(polygon)>=5:
				sizeFour = True
				sizeFive = True

	if hitNotConvex:
		print "Non-convex polygons."
		return 0
	elif sizeFour and not sizeFive:
		print "No pentagons."
		return 1
	elif sizeFour and sizeFive:
		return 2

	print "No quadrilaterals or pentagons."
	return 0

#Determines the reachability for one world at a time
def getReachabilityGrade(pathnodes, pathnetwork, world, pairsToCheck, mapNumber = 0):
	mapNumber += 1

	sumOfAttempts = 0.0

	if len(pathnodes)==0:
		#print "No pathnodes"
		return 0

	if None in pathnodes:
		print "Path node cannot be None."
		return 0

	obstacleLines = []

	for o in world.getObstacles():
		for oLine in o.getLines():
			obstacleLines.append(oLine)

	try:
		for pair in pairsToCheck:
			foundPath = False
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
						foundPath = True
			if not foundPath:
				print "No path found between " + str(pair[0]) + " and " + str(pair[1]) + "."
	except TimeoutFunctionException:
		raise TimeoutFunctionException
	except:
		print sys.exc_info()[0]
		return 0

	#print "Sum of Attempts: "+str(sumOfAttempts)
	gradeForThesePoints = (sumOfAttempts/len(pairsToCheck))
	#print "Reach Grade: "+str(gradeForThesePoints)
	return gradeForThesePoints