'''
 * Copyright (c) 2014, 2015 Entertainment Intelligence Lab, Georgia Institute of Technology.
 * Originally developed by Mark Riedl.
 * Last edited by Mark Riedl 05/2015
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import sys, pygame, math, numpy, random, time, copy, operator
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates a path node network that connects the midpoints of each nav mesh together
def myCreatePathNetwork(world, agent = None):
	nodes = [];
	edges = [];
	polys = [];

	points = world.getPoints();
	lines = world.getLines();
	obstacles = [];
	for obstacle in world.getObstacles(): obstacles.append(obstacle.getPoints());
	newLines = [];

	# Create all possible triangles
	for first in points:
		for second in points:
			if second is first: continue;

			if rayTraceWorldNoEndPoints(first, second, lines + newLines):
				if (first, second) not in lines + newLines and (second, first) not in lines + newLines: continue;

			for third in points:
				if third in (first, second): continue;

				if rayTraceWorldNoEndPoints(second, third, lines + newLines):
					if (second, third) not in lines + newLines and (third, second) not in lines + newLines: continue;

				if rayTraceWorldNoEndPoints(third, first, lines + newLines):
					if (first, third) not in lines + newLines and (third, first) not in lines + newLines: continue;

				newLines.append((first, second));
				newLines.append((second, third));
				newLines.append((third, first));
				polys.append([first, second, third]);

	# Remove triangles that are obstacles or repeated
	remove = [];
	for i in range(len(polys)):
		if polys[i] in remove: continue;

		triangles = [[polys[i][0], polys[i][1], polys[i][2]],
					 [polys[i][0], polys[i][2], polys[i][1]],
					 [polys[i][1], polys[i][0], polys[i][2]],
					 [polys[i][1], polys[i][2], polys[i][0]],
					 [polys[i][2], polys[i][0], polys[i][1]],
					 [polys[i][2], polys[i][1], polys[i][0]]];

		for obstacle in obstacles:
			if obstacle in triangles:
				remove.append(polys[i]);
				break;

		for j in range(i + 1, len(polys)):
			if polys[j] in triangles: remove.append(polys[j]);

	newPolys = [];
	for polygon in polys:
		if polygon not in remove: newPolys.append(polygon);
	polys = newPolys;

	# Remove triangles that contain/cut into obstacles
	remove = [];
	for polygon in polys:
		for obstacle in obstacles:
			for point in obstacle:
				if pointInsidePolygonPoints(point, polygon) and not pointOnPolygon(point, polygon):
					remove.append(polygon);
					break;

			for i in range(len(polygon)):
				midpoint = ((polygon[i][0] + polygon[(i + 1) % len(polygon)][0]) / 2,
							(polygon[i][1] + polygon[(i + 1) % len(polygon)][1]) / 2);
				if pointInsidePolygonPoints(midpoint, obstacle) and not pointOnPolygon(midpoint, obstacle):
					remove.append(polygon);
					break;

	newPolys = [];
	for polygon in polys:
		if polygon not in remove: newPolys.append(polygon);

	# Create larger polygons from adjacent triangles/smaller polygons
	i = 0;
	while i < len(newPolys):
		j = 0;
		while j < len(newPolys):
			if newPolys[j] is newPolys[i] or not polygonsAdjacent(newPolys[i], newPolys[j]):
				j += 1;
				continue;

			shared = polygonsAdjacent(newPolys[i], newPolys[j]);

			newPolygon = newPolys[i] + newPolys[j];
			for point in shared: newPolygon.remove(point);

			# Sort points in polygon by angle from center
			center = ((shared[0][0] + shared[1][0]) / 2, (shared[0][1] + shared[1][1]) / 2);

			toSort = [];
			for point in newPolygon:
				angle = math.atan2(point[1] - center[1], point[0] - center[0]);
				toSort.append((angle, point));
			toSort.sort(key = lambda p: p[0]);
			newPolygon = [];
			for pair in toSort: newPolygon.append(pair[1]);

			if isConvex(newPolygon):
				newPolys.append(newPolygon);
				newPolys.remove(newPolys[i]);
				newPolys.remove(newPolys[j - 1]);
				i -= 1;
				break;
			j += 1;
		i += 1;

	# Create nodes at centers of polygons and midpoints of edges
	centers = [];
	for first in newPolys:
		xtotal = 0;
		ytotal = 0;
		for point in first:
			xtotal += point[0] / len(first);
			ytotal += point[1] / len(first);

		nodes.append((xtotal, ytotal));
		centers.append((xtotal, ytotal));

		for second in newPolys:
			if second is first: continue;

			shared = polygonsAdjacent(first, second);
			if shared:
				midpoint = ((shared[0][0] + shared[1][0]) / 2, (shared[0][1] + shared[1][1]) / 2);
				if midpoint not in nodes: nodes.append(midpoint);

	# Connect unblocked nodes within each polygon
	connectedNodes = [];
	for polygon in newPolys:
		for first in nodes:
			for second in nodes:
				if second is first: continue;

				if (pointOnPolygon(first, polygon) or pointInsidePolygonPoints(first, polygon)) and \
					(pointOnPolygon(second, polygon) or pointInsidePolygonPoints(second, polygon)) and \
					(first, second) not in edges and (second, first) not in edges:

					collision = False;
					for obstacle in obstacles:
						for point in obstacle:
							if minimumDistance((first, second), point) < world.getAgent().getMaxRadius():
								collision = True;
								break;

					if not collision:
						edges.append((first, second));
						if first not in connectedNodes: connectedNodes.append(first);
						if second not in connectedNodes: connectedNodes.append(second);

	return connectedNodes, edges, newPolys;