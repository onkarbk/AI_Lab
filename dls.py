graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':[],
    '8':[]
}
visited=list()
def dls(x,visited,source,limit,depth):
    print("\nCurrent Level: ", depth)
    visited.append(source)
    if source == x:
        print("Goal node found")
        return visited
    print('Goal node not found')
    if depth==limit:
        return False
    for child in graph[source]: 
        if dls(x,visited,child,limit,depth+1):  
            return visited
        visited.pop()
    return False

x=input("Enter the node to be searched: ")
limit=int(input("\nEnter the limit of the graph: "))
y=dls(x,visited,'5',limit,0)
if(y):
    print(x, "is found. Path is: ", visited)
else: 
    print('Path not found')
