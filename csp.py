def solve(list1, tables):
    for i in list1:
        if i in tables:
            return False
    return True
n = int(input("Number of People: "))
c = int(input("Number of tables: "))
list1 = {}
tables = {}
for i in range(c):
    tables[i] = []
for i in range(n):
    list1[i] = []
print("Give the enemy list:(Type exit for exit)")
while(True):
    string = input()
    if(string == "exit"):
        break
    a, b = map(int,string.split())  
    list1[a].append(b)
    list1[b].append(a)
print(list1)
 
flag1 = True
for i in range(n):
    flag = False
    for j in range(c):
        print(str(i)+ " " + str(j) + " " + str(solve(list1[i],tables[j])))
        if solve(list1[i],tables[j]):
            tables[j].append(i)
            flag = True
            break
        
    if flag == False:
        print("False")
        flag1 = False
        break
if flag1:
    print(tables)