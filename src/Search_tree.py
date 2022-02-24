graph = {
'origen': ['A','B','C'],
'A': ['D','E'],
'B': ['F'],
'C': ['G','H'],
'D': [],
'E': ['I','J'],
'F': [],
'G': [],
'H': ['K','L'],
'I': [],
'J': ['M'],
'K': ['N'],
'L': [],
'M': ['O'],
'N': [],
'O': []
}

class Node:
    def __init__(self, parent=None, state=None, cost=0, depth=0, action=None):
        self.parent = parent
        self.state = state
        self.cost = cost
        self.depth = depth
        self.action = action

    def setParent(self, p):
        self.parent = p

    def setState(self, s):
        self.state = s

    def setCost(self, c):
        self.cost = c

    def setDepth(self, d):
        self.depth = d

    def setAction(self, a):
        self.action = a


def depth_search_ltr(graph, first_state, goal):
    print("Depth_search (from left to right):\n")
    frontier = []
    path = []
    current_cost = 0
    current_depth = 0
    found = False

    root = Node(state=first_state, action=graph[first_state])
    frontier.append(root)

    while not found and frontier:
        current_node = frontier.pop()
        path.append(current_node)
        current_cost +=1
        current_node.setCost(current_cost)
        current_depth = current_node.depth

        if(current_node.state == goal):
            found = True
            break
        else:
            getSuccessor_reverse(current_node, frontier, current_cost, current_depth)

    printList(path)
    print("cost: ",current_cost)
    print("depth: ",current_depth)
    print("-----\n\n")

def depth_search_rtl(graph, first_state, goal):
    print("Depth_search (from right to left):\n")
    frontier = []
    path = []
    current_cost = 0
    current_depth = 0
    found = False

    root = Node(state=first_state, action=graph[first_state])
    frontier.append(root)

    while not found and frontier:
        current_node = frontier.pop()
        path.append(current_node)
        current_cost +=1
        current_node.setCost(current_cost)
        current_depth = current_node.depth

        if(current_node.state == goal):
            found = True
            break
        else:
            getSuccessor(current_node, frontier, current_cost, current_depth)

    printList(path)
    print("cost: ",current_cost)
    print("depth: ",current_depth)
    print("-----\n\n")

def breadth_search_rtl(graph, first_state, goal):
    print("Breadth_search (from right to left):\n")
    frontier = []
    path = []
    current_cost = 0
    current_depth = 0
    found = False

    root = Node(state=first_state, action=graph[first_state])
    frontier.append(root)

    while not found and frontier:
        current_node = frontier.pop(0)
        path.append(current_node)
        current_cost +=1
        current_node.setCost(current_cost)
        current_depth = current_node.depth

        if(current_node.state == goal):
            found = True
            break
        else:
            getSuccessor_reverse(current_node, frontier, current_cost, current_depth)

    printList(path)
    print("cost: ",current_cost)
    print("depth: ",current_depth)
    print("-----\n\n")

def breadth_search_ltr(graph, first_state, goal):
    print("Breadth_search (from left to right):\n")
    frontier = []
    path = []
    current_cost = 0
    current_depth = 0
    found = False

    root = Node(state=first_state, action=graph[first_state])
    frontier.append(root)

    while not found and frontier:
        current_node = frontier.pop(0)
        path.append(current_node)
        current_cost +=1
        current_node.setCost(current_cost)
        current_depth = current_node.depth

        if(current_node.state == goal):
            found = True
            break
        else:
            getSuccessor(current_node, frontier, current_cost, current_depth)

    printList(path)
    print("cost: ",current_cost)
    print("depth: ",current_depth)
    print("-----\n\n")

def iterative_depth_search_ltr(maxlimit,graph, first_state, goal):
    print("Iterative_depth_search (from left to right):\n")
    frontier = []
    path = []
    current_cost = 0
    current_depth = 0
    found = False
    limit = 0

    while limit<=maxlimit and not found:
        root = Node(state=first_state, action=graph[first_state])
        frontier.append(root)
        while not found and frontier:
            current_node = frontier.pop()
            path.append(current_node)
            current_cost +=1
            current_node.setCost(current_cost)
            current_depth = current_node.depth
            if(current_node.state == goal):
                found = True
                break
            else:
              getSuccessorLimited_reverse(current_node, frontier, current_cost, current_depth, limit)
        print("limit: ",limit)
        print("path:\n")
        printList(path)
        limit+=1
        path = []
    if(found):
      print("Goal state achieved!")
      print("cost: ",current_cost)
      print("depth: ",current_depth)
      print("-----\n\n")
    else:
      print("Max limit achieved without finding the goal state")

def iterative_depth_search_rtl(maxlimit,graph, first_state, goal):
    print("Iterative_depth_search (from right to left):\n")
    frontier = []
    path = []
    current_cost = 0
    current_depth = 0
    found = False
    limit = 0

    while limit<=maxlimit and not found:
        root = Node(state=first_state, action=graph[first_state])
        frontier.append(root)
        while not found and frontier:
            current_node = frontier.pop()
            path.append(current_node)
            current_cost +=1
            current_node.setCost(current_cost)
            current_depth = current_node.depth
            if(current_node.state == goal):
                found = True
                break
            else:
              getSuccessorLimited(current_node, frontier, current_cost, current_depth, limit)
        print("limit: ",limit)
        print("path:\n")
        printList(path)
        limit+=1
        path = []
    if(found):
      print("Goal state achieved!")
      print("cost: ",current_cost)
      print("depth: ",current_depth)
      print("-----\n\n")
    else:
      print("Max limit achieved without finding the goal state")

def printList(list):
    for element in list:
        print(element.state)
    print("----")

def getSuccessor(node, frontier, current_cost, current_depth):
    current_depth +=1
    for n in node.action:
        successor = Node(state=n)
        successor.setParent(node.state)
        successor.setCost(current_cost)
        successor.setDepth(current_depth)
        successor.setAction(graph[successor.state])
        frontier.append(successor)

def getSuccessor_reverse(node, frontier, current_cost, current_depth):
    current_depth +=1
    for n in node.action[::-1]:
        successor = Node(state=n)
        successor.setParent(node.state)
        successor.setCost(current_cost)
        successor.setDepth(current_depth)
        successor.setAction(graph[successor.state])
        frontier.append(successor)

def getSuccessorLimited(node, frontier, current_cost, current_depth, limit):
    current_depth +=1
    if(limit>=current_depth):
      for n in node.action:
          successor = Node(state=n)
          successor.setParent(node.state)
          successor.setCost(current_cost)
          successor.setDepth(current_depth)
          successor.setAction(graph[successor.state])
          frontier.append(successor)

def getSuccessorLimited_reverse(node, frontier, current_cost, current_depth, limit):
    current_depth +=1
    if(limit>=current_depth):
      for n in node.action[::-1]:
          successor = Node(state=n)
          successor.setParent(node.state)
          successor.setCost(current_cost)
          successor.setDepth(current_depth)
          successor.setAction(graph[successor.state])
          frontier.append(successor)

depth_search_ltr(graph, 'origen','O')
depth_search_rtl(graph, 'origen','O')
breadth_search_rtl(graph, 'origen','O')
breadth_search_ltr(graph, 'origen','O')
iterative_depth_search_ltr(5, graph, 'origen', 'O')
iterative_depth_search_rtl(5, graph, 'origen', 'O')
