visited=[]
frontier=[]
flag=0

def ucs(goal):
    global frontier
    global visited
    global graph
    global flag 
    if frontier:
        whole=sorted(frontier)[0]
        frontier.remove(whole)
        node=whole[1]
        cost=whole[0]
        visited.append(node)
        for a in graph[node]:
            frontier.append((cost+graph[node][a],a))
            
            if(a==goal):
                print("city found, total cost: "+str(cost+graph[node][a]))
                print('path is', visited)
                flag=1
        if flag!=1:
            ucs(goal)
graph={
                '1':{'2':2,'3':1},
                '2':{'4':4},
                '3':{'4':4},
                '4':{}
}
search=input("Enter the city to be searched\n")
start=input("Enter the starting city\n")
frontier.append((0,start))
ucs(search)
if flag!=1:
  print("City not found")