from queue import PriorityQueue
 
graph={
    'arad':{'zerind':75,'sibiu':140,'timisoara':118},
    'zerind':{'arad':75,'oradea':71},
    'oradea':{'zerind':71,'sibiu':151},
    'timisoara':{'arad':118,'lugoj':111},
    'sibiu':{'arad':140,'oradea':151,'fagaras':99,'rimnicu vilcea':80},
    'lugoj':{'timisoara':111,'mehadia':70},
    'fagaras':{'sibiu':99,'bucharest':211},
    'rimnicu vilcea':{'sibiu':80,'pitesti':97,'craiova':146},
    'mehadia':{'lugoj':70,'dobreta':75},
    'dobreta':{'mehadia':75,'craiova':120},
    'bucharest':{'fagaras':211,'pitesti':101,'urziceni':85,'giurglu':90},
    'giurglu':{'bucharest':90},
    'pitesti':{'bucharest':101,'craiova':138,'rimnicu vilcea':97},
    'craiova':{'dobreta':120,'rimnicu vilcea':146,'pitesti':138},
    'urziceni':{'hirsova':98,'vaslui':142,'bucharest':85},
    'hirsova':{'urziceni':98,'eforie':86},
    'vaslui':{'urziceni':142,'lasi':92},
    'lasi':{'vaslui':92,'neamt':87},
    'eforie':{'hirsova':86},
    'neamt':{'lasi':87}
}

h_value={
    'arad':366,
    'zerind':374,
    'oradea':380,
    'timisoara':329,
    'sibiu':253,
    'lugoj':244,
    'fagaras':176,
    'rimnicu vilcea':193,
    'mehadia':241,
    'dobreta':242,
    'bucharest':0,
    'giurglu':77,
    'pitesti':100,
    'craiova':160,
    'urziceni':80,
    'hirsova':151,
    'vaslui':199,
    'lasi':226,
    'eforie':161,
    'neamt':234
}
 
 
def search(graph, start, end):
    queue = PriorityQueue()
    queue.put((0+h_value[start], [start]))
 
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
 
        if end in node[1]:
            print("Path found: " + str(node[1]) + ", \nCost = " + str(node[0]))
            break
 
        cost = node[0] - h_value[current]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor] + h_value[neighbor], temp))
 
 
search_city=input("Enter the city to be searched\n")
start_city=input("Enter the starting city\n")
search(graph, start_city, search_city)