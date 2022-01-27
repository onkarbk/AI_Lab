import math

def minimax(depth, nodeIndex, maximizingPlayer,
            values):
    global MAX,MIN
   
    if depth ==math.log(n,2):
        return values[nodeIndex]
 
    if maximizingPlayer:
        return max(minimax(depth + 1, nodeIndex * 2 + 0, False, values),minimax(depth + 1,nodeIndex * 2 + 1,False, values))
    else:
       return min(minimax(depth + 1, nodeIndex * 2 + 0,
                            True, values),minimax(depth + 1, nodeIndex * 2 + 1, 
                            True, values))
          
values=[]
print("Enter size")
n=int(input())

print("Enter values:")
for i in range(n):
	a=int(input())

	values.append(a)
	
	
print("The optimal value is :", minimax(0, 0, True, values))
