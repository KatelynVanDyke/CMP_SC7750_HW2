import copy
import time


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ") "

    def __repr__(self):
        return str(self)


class Node:
    def __init__(self, x, y, state, cost, path):
        self.x = x
        self.y = y
        self.state = state
        self.cost = cost
        self.path = path


max_x = 4
max_y = 5

instance1 = [['W', 'W', 'W', 'W', 'W', 'W'],
             ['W', 'C', 'D', 'C', 'C', 'C'],
             ['W', 'C', 'C', 'C', 'D', 'C'],
             ['W', 'C', 'C', 'C', 'C', 'D'],
             ['W', 'C', 'C', 'C', 'C', 'C']]
instance2 = [['W', 'W', 'W', 'W', 'W', 'W'],
             ['W', 'C', 'D', 'C', 'C', 'C'],
             ['W', 'D', 'C', 'C', 'D', 'C'],
             ['W', 'C', 'C', 'D', 'C', 'C'],
             ['W', 'C', 'C', 'C', 'C', 'C']]


# problemSpace -> a matrix of what's clean and dirty
# initialLocation -> the location of the vaccuum
def treeSearch(problemSpace, initialLocation):
    fringe = []
    fringe = Insert(Make_Node(initialLocation.x, initialLocation.y, problemSpace, 0, [initialLocation]), fringe)
    # variables to store metrics
    numOfGenerated = 0
    numOfExpanded = 0
    # clock variable
    clockEnd = time.time() + 600
    while time.time() < clockEnd:
        if len(fringe) == 0:
            return None, numOfGenerated, numOfExpanded
        currNode = fringe.pop(0)
        # print(str(currNode.x) + ", " + str(currNode.y))
        if Goal_Test(currNode.state):
            return currNode, numOfGenerated, numOfExpanded
        expandedNodes = Expand(currNode)
        # metrics
        numOfGenerated = numOfGenerated + len(expandedNodes)
        numOfExpanded = numOfExpanded + 1
        # insert expanded into fringe
        fringe = Insert_All(expandedNodes, fringe)
    # if we reach here we've timed out
    return None, numOfGenerated, numOfExpanded


def Insert(node, fringe):
    fringe.append(node)
    # sort based on node costs
    fringe.sort(key=lambda x: x.cost)
    return fringe


def Insert_All(nodes, fringe):
    fringe.extend(nodes)
    # sort based on node costs
    fringe.sort(key=lambda x: x.cost)
    return fringe


def Make_Node(x, y, state, cost, path) -> Node:
    return Node(x, y, state, cost, path)


def Expand(node):
    nodes = []
    path = node.path.copy()
    path.append(Location(node.x, node.y))
    # left
    if node.y > 1:
        nodes.append(Make_Node(node.x, node.y-1, node.state, node.cost+1, path))
    # right
    if node.y < max_y:
        nodes.append(Make_Node(node.x, node.y+1, node.state, node.cost+.9, path))
    # up
    if node.x > 1:
        nodes.append(Make_Node(node.x-1, node.y, node.state, node.cost+.8, path))
    # down
    if node.x < max_x:
        nodes.append(Make_Node(node.x+1, node.y, node.state, node.cost+.7, path))
    # suck
    if node.state[node.x][node.y] == 'D':
        newState = copy.deepcopy(node.state)
        newState[node.x][node.y] = 'C'
        nodes.append(Make_Node(node.x, node.y, newState, node.cost+.6, path))

    return nodes


# returns True if no dirty rooms, returns False if any dirty rooms found
def Goal_Test(problemSpace) -> bool:
    for i in range(max_x+1):
        for j in range(max_y+1):
            if problemSpace[i][j] == 'D':
                return False
    return True


# run instance 1
# record the start time
startTime = time.time()
# run the algorithm
problemSpace1 = copy.deepcopy(instance1)
result1, generated, expanded = treeSearch(problemSpace1, Location(2, 2))
# record the stop time
endTime = time.time()

if result1 is not None:
    print("\nresult: " + str(result1.x) + " " + str(result1.y) + " " + str(result1.cost))
    print("Problem Space:")
    for i in range(max_x+1):
        for j in range(max_y+1):
            print(result1.state[i][j], end='')
        print('')
    for elem in result1.path:
        print(elem, end=', ')
else:
    print("\nresult: No goal state found")

print("Time taken: %.5f" % (endTime-startTime))
print("Generated: " + str(generated) + ", Expanded: " + str(expanded) + "\n\n")

# run instance 2
# record the start time
startTime = time.time()
# run the algorithm
problemSpace2 = copy.deepcopy(instance2)
result2, generated, expanded = treeSearch(problemSpace2, Location(3, 2))
# record the stop time
endTime = time.time()

if result2 is not None:
    print("\nresult: " + str(result2.x) + " " + str(result2.y) + " " + str(result2.cost))
    print("Problem Space:")
    for i in range(max_x+1):
        for j in range(max_y+1):
            print(result2.state[i][j], end='')
        print('')
else:
    print("\nresult: No goal state found")

print("Time taken: %.5f" % (endTime-startTime))
print("Generated: " + str(generated) + ", Expanded: " + str(expanded) + "\n\n")
