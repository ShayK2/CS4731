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

import sys, pygame, math, numpy, random, time, copy
from pygame.locals import *

from constants import *
from utils import *
from core import *
from moba import *

class MyMinion(Minion):
    def __init__(self, position, orientation, world, image = NPC, speed = SPEED, viewangle = 360, hitpoints = HITPOINTS, firerate = FIRERATE, bulletclass = SmallBullet):
        Minion.__init__(self, position, orientation, world, image, speed, viewangle, hitpoints, firerate, bulletclass)
        self.states = [Idle, Move, Attack, End]

    def start(self):
        Minion.start(self)
        self.changeState(Idle)

class Idle(State):
    def enter(self, oldstate):
        State.enter(self, oldstate)
        self.agent.stopMoving()

    def execute(self, delta = 0):
        State.execute(self, delta)
        minDist = float("inf")
        target = None
        enemyTypes = [self.agent.world.getEnemyNPCs(self.agent.getTeam()),
                    self.agent.world.getEnemyTowers(self.agent.getTeam()),
                    self.agent.world.getEnemyBases(self.agent.getTeam())]
        for enemyType in enemyTypes:
            if enemyType and len(enemyType) > 0:
                for enemy in enemyType:
                    dist = distance(self.agent.getLocation(), enemy.getLocation())
                    if dist < minDist:
                        target = enemy
                        minDist = dist
            if target: self.agent.changeState(Move, target, enemyType)
        self.agent.changeState(End)

class Move(State):
    def parseArgs(self, args):
        self.target = args[0]
        self.enemies = args[1]

    def enter(self, oldstate):
        self.agent.navigateTo(self.target.getLocation())

    def execute(self, delta = 0):
        if (not self.agent.moveTarget) and self.target: self.agent.navigateTo(self.target.getLocation())
        for enemy in self.enemies:
            if enemy in self.agent.getVisible() and distance(self.agent.getLocation(), enemy.getLocation()) <= BULLETRANGE: self.agent.changeState(Attack, enemy)
        self.agent.changeState(Idle)

class Attack(State):
    def parseArgs(self, args): self.enemies = args[0]

    def enter(self, oldstate):
        self.agent.navigator.path = None
        self.agent.navigator.destination = None

    def execute(self, delta = 0):
        if self.enemies in self.agent.getVisible() and distance(self.agent.getLocation(), self.enemies.getLocation()) <= BULLETRANGE:
            self.agent.turnToFace(self.enemies.getLocation())
            self.agent.shoot()
        self.agent.changeState(Idle)

class End(State):
    def enter(self, args): self.agent.stopMoving()