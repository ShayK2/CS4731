import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from mycreatepathnetwork import *


################
### RandomNavigator
###
### The RandomNavigator dynamically creates a path network. 
### But when asked to move the agent, it computes a random path through the network and probably fails to reach its destination.
		
class RandomNavMeshNavigator(NavMeshNavigator):

	def __init__(self):
		Navigator.__init__(self)

	### Create the path node network and pre-compute all shortest paths along the network
	### self: the navigator object
	### world: the world object		
	def createPathNetwork(self, world):
		self.pathnodes, self.pathnetwork, self.navmesh = myCreatePathNetwork(world, self.agent)
		return None
		
	### Finds the shortest path from the source to the destination.
	### self: the navigator object
	### source: the place the agent is starting from (i.e., its current location)
	### dest: the place the agent is told to go to
	def computePath(self, source, dest):
		# Make sure that the pathnodes have been created.
		if self.agent != None and self.world != None and self.pathnodes != None:
			start = findClosestUnobstructed(source, self.pathnodes, self.world.getLines())
			end = findClosestUnobstructed(dest, self.pathnodes, self.world.getLines())
			current = start
			path = [current]
			count = 0
			last = current
			while current != end and count < 100:
				count = count + 1
				successors = []
				for l in self.pathnetwork:
					if l[0] == current and l[1] != last:
						successors.append(l[1])
					elif l[1] == current and l[0] != last:
						successors.append(l[0])
				# If successors are empty because we don't allow the agent to return to the last point,
				# then try again but allow the agent to return to the last point
				if len(successors) == 0:
					for l in self.pathnetwork:
						if l[0] == current:
							successors.append(l[1])
						elif l[1] == current:
							successors.append(l[0])
				if len(successors) == 0:
					print "No path found."
					return
				r = random.randint(0, len(successors)-1)
				last = current
				current = successors[r]
				path.append(current)
			self.setPath(path)
			self.source = source
			self.destination = dest
			# Get the first way point
			first = path.pop(0)
			# Tell the agent to move to the first waypoint
			if first is not None:
				self.agent.moveToTarget(first)
			





