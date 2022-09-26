# CMP_SC 7750
# HW 2
# Group 15
# 09/25/22

import time
import math


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, Location, Left, Right, Up, Down, direction):
        self.Location = Location
        self.Left = Left
        self.Right = Right
        self.Up = Up
        self.Down = Down
        self.direction = direction


maxX = 4
maxY = 5

dirtyRooms1 = [Location(1, 2), Location(2, 4), Location(3, 5)]
initialLocation1 = Location(2, 2)

dirtyRooms2 = [Location(1, 2), Location(2, 1), Location(2, 4), Location(3, 3)]
initialLocation2 = Location(3, 2)


def iterativeDeepeningSearch(maxX, maxY, dirtyRooms, initialLocation):
    startTime = time.time()
    Root = Node(initialLocation, None, None, None, None, None)
    queue = [Root]
    numberGenerated = 1
    numberExpanded = 1
    while True:
        path = goalTest(Root, dirtyRooms, numberGenerated)
        currentTime = time.time()
        if (path is not None) or ((currentTime - startTime) > 300):
            endTime = time.time()
            print("First Five Expanded: ", end=None)
            for Room in firstFive(Root):
                print("(" + str(Room.Location.x) + ", " + str(Room.Location.y) + ")  ")
            print("Number of Nodes Expanded: " + str(numberExpanded))
            print("Number of Nodes Generated: " + str(numberGenerated))
            print("CPU Time: " + str(endTime - startTime))
            if path is not None:
                print("Solution Path: ", end=None)
                for Room in path:
                    print("(" + str(Room.Location.x) + ", " + str(Room.Location.y) + ")  ")
                print("Number of Moves in Solution: " + str(len(path)))
                print("Solution Cost: " + str(solutionCost(path, dirtyRooms)))
            return
        expandSearchLevel(queue, maxX, maxY, numberExpanded)


def goalTest(Root, dirtyRooms, numberGenerated) -> []:
    stack = [Root]
    result = [Root]
    while (len(stack)):
        if(len(dirtyRooms) == 0):
            return result
        Node = stack.pop()
        for i in range(0, len(dirtyRooms), 1):
            if (Node.Location.x == dirtyRooms[i].x) and (Node.Location.y == dirtyRooms[i].y):
                dirtyRooms.remove(i)
        if Node.Left is not None:
            stack.append(Node.Left)
            result.append(Node.Left)
            numberGenerated = numberGenerated + 1
        if Node.Right is not None:
            stack.append(Node.Right)
            result.append(Node.Right)
            numberGenerated = numberGenerated + 1
        if Node.Up is not None:
            stack.append(Node.Up)
            result.append(Node.Up)
            numberGenerated = numberGenerated + 1
        if Node.Down is not None:
            stack.append(Node.Down)
            result.append(Node.Down)
            numberGenerated = numberGenerated + 1
    return None


def firstFive(Root) -> []:
    return [Root, Root.Left, Root.Up, Root.Right, Root.Down]


def solutionCost(path, dirtyRooms) -> float:
    cost = [dirtyRooms * .6]
    for Room in path:
        Node = path.pop(0)
        if Node.direction == "left":
            cost.append(1)
        if Node.direction == "right":
            cost.append(.9)
        if Node.direction == "up":
            cost.append(.8)
        if Node.direction == "down":
            cost.append(.7)
    return math.fsum(cost)


def expandSearchLevel(queue, maxX, maxY, numberExpanded):
    for room in queue:
        node = queue.pop(0)
        if node.Location.x > 1:
            newNode = Node(Location(0, 0), None, None, None, None, "left")
            newNode.Location.x = node.Location.x - 1
            newNode.Location.y = node.Location.y
            node.Left = newNode
            queue.append(newNode)
            numberExpanded = numberExpanded + 1
        if node.Location.x < maxX:
            newNode = Node(Location(0, 0), None, None, None, None, "right")
            newNode.Location.x = node.Location.x + 1
            newNode.Location.y = node.Location.y
            node.Right = newNode
            queue.append(newNode)
            numberExpanded = numberExpanded + 1
        if node.Location.y > 1:
            newNode = Node(Location(0, 0), None, None, None, None, "up")
            newNode.Location.x = node.Location.x
            newNode.Location.y = node.Location.y - 1
            node.Up = newNode
            queue.append(newNode)
            numberExpanded = numberExpanded + 1
        if node.Location.y < maxY:
            newNode = Node(Location(0, 0), None, None, None, None, "down")
            newNode.Location.x = node.Location.x
            newNode.Location.y = node.Location.y + 1
            node.Down = newNode
            queue.append(newNode)
            numberExpanded = numberExpanded + 1


def printNode(Node):
    print("Location: " + str(Node.Location.x) + ", " + str(Node.Location.y))
    print("Node.left: " + str(Node.left))
    print("Node.right: " + str(Node.right))
    print("Node.up: " + str(Node.up))
    print("Node.down: " + str(Node.down))


iterativeDeepeningSearch(maxX, maxY, dirtyRooms1, initialLocation1)
