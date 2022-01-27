import math
MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
    global MAX,MIN
   
    if depth ==math.log(n,2):
        return values[nodeIndex]
 
    if maximizingPlayer:
      
        best = MIN
 

        for i in range(0, 2):
             
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
              print("Pruned:","alpha:",alpha,"Beta:",beta,"nodeIndex",nodeIndex)
              break
          
        return best
      
    else:
        best = MAX
 
   
        for i in range(0, 2):
          
            val = minimax(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
 
            if beta <= alpha:
             print("Pruned:","alpha:",alpha,"Beta:",beta,"nodeIndex",nodeIndex)
             break
          
        return best
      
values=[]
print("Enter size")
n=int(input())

print("Enter values:")
for i in range(n):
	a=int(input())

	values.append(a)
	
	
print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))

