from enum import Enum


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, x, y, state, cost):
        self.x = x
        self.y = y
        self.state = state
        self.cost = cost


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
def treeSearch(problemSpace, initialLocation) -> Node:
    fringe = []
    fringe = Insert(Make_Node(initialLocation.x, initialLocation.y, problemSpace, 0), fringe)
    while True:
        if len(fringe) == 0:
            return None
        currNode = fringe.pop(0)
        print(str(currNode.x) + ", " + str(currNode.y))
        if Goal_Test(currNode.state):
            return currNode
        fringe = Insert_All(Expand(currNode), fringe)


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


def Make_Node(x, y, state, cost) -> Node:
    return Node(x, y, state, cost)


def Expand(node):
    nodes = []
    # left
    if node.y > 1:
        nodes.append(Make_Node(node.x, node.y-1, node.state, node.cost+1))
    # right
    if node.y < max_y:
        nodes.append(Make_Node(node.x, node.y+1, node.state, node.cost+.9))
    # up
    if node.x > 1:
        nodes.append(Make_Node(node.x-1, node.y, node.state, node.cost+.8))
    # down
    if node.x < max_x:
        nodes.append(Make_Node(node.x+1, node.y, node.state, node.cost+.7))
    # suck
    if node.state[node.x][node.y] == 'D':
        newState = node.state[:]
        newState[node.x][node.y] = 'C'
        nodes.append(Make_Node(node.x, node.y, newState, node.cost+.6))

    return nodes


# returns True if no dirty rooms, returns False if any dirty rooms found
def Goal_Test(problemSpace) -> bool:
    for i in range(max_x+1):
        for j in range(max_y+1):
            if problemSpace[i][j] == 'D':
                return False
    return True


result1 = treeSearch(instance1, Location(2, 2))
print("\nresult: " + str(result1.x) + " " + str(result1.y) + " " + str(result1.cost))
print("Problem Space:")
for i in range(max_x+1):
    for j in range(max_y+1):
        print(result1.state[i][j], end='')
    print('')

# result2 = treeSearch(instance2, Location(3, 2))
# print(str(result2.x) + " " + str(result2.y) + " " + str(result2.cost))
