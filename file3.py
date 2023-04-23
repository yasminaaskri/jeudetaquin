import copy,time
s0 = [[1,2,3],[8,6,-1],[7,5,4]]
goal = [[1,2,3],[8,-1,4],[7,6,5]]
def successorsOf(t):
    size_of_tareaux = [len(t), len(t[0])]
    position_empty = empty_case_position(t)
    generated_list = []
    generated_list.append(move_down(copy.deepcopy(t), position_empty, size_of_tareaux))
    generated_list.append(move_up(copy.deepcopy(t), position_empty, size_of_tareaux))
    generated_list.append(move_left(copy.deepcopy(t), position_empty, size_of_tareaux))
    generated_list.append(move_right(copy.deepcopy(t), position_empty, size_of_tareaux))
    return generated_list

def empty_case_position(t):
    for row in range(len(t)):
        for col in range(len(t[0])):
            if t[row][col] == -1:
                return [row, col]
    return None

def move_up(t, position_empty, size_of_tareaux):
    t2 = copy.deepcopy(t)
    if position_empty[0]-1 > -1:
        t2[position_empty[0]][position_empty[1]] = t[position_empty[0]-1][position_empty[1]]
        t2[position_empty[0]-1][position_empty[1]] = -1
    return t2

def move_down(t, position_empty, size_of_tareaux):
    t2 = copy.deepcopy(t)
    if position_empty[0]+1 < size_of_tareaux[0]:
        t2[position_empty[0]][position_empty[1]] = t[position_empty[0]+1][position_empty[1]]
        t2[position_empty[0]+1][position_empty[1]] = -1
    return t2

def move_right(t, position_empty, size_of_tareaux):
    t2 = copy.deepcopy(t)
    if position_empty[1]+1 < size_of_tareaux[1]:
        t2[position_empty[0]][position_empty[1]] = t[position_empty[0]][position_empty[1]+1]
        t2[position_empty[0]][position_empty[1]+1] = -1
    return t2

def move_left(t, position_empty, size_of_tareaux):
    t2 = copy.deepcopy(t)
    if position_empty[1]-1 > -1:
        t2[position_empty[0]][position_empty[1]] = t[position_empty[0]][position_empty[1]-1]
        t2[position_empty[0]][position_empty[1]-1] = -1
    return t2

def affiche(t):
    for x in t:
        for y in x:
            print(y, end=" ")
        print()

def recherchDFS(s0,goal):
    firstState=list(s0);
    closedNodes=[];
    generatedList=[];
    freeNodes=[firstState];
    goalNode=list(goal);
    success=False
    n=0
    while len(freeNodes)!=0 and not(success):
        n+=1
        firstState=freeNodes[0];
        freeNodes.pop(0);
        closedNodes.append(firstState);
        generatedList=successorsOf(firstState);#successorsOf is the function  you need to create to genere the node fron exixte node
        generatedList = [x for x in generatedList if x not in freeNodes and x not in closedNodes]
        
        for x in generatedList:
            if (x==goalNode) :
                success=True;
                closedNodes.append(goal)
                for x in closedNodes :
                    affiche(x)
                    print('|')
                print("the goal is with coutt=:",end="")
                print(n)
                break
        freeNodes=generatedList+freeNodes;
    return (closedNodes,success,len(freeNodes+closedNodes))

def recherchDFSL(s0,goal,L):
    firstState=list(s0);
    closedNodes=[];
    generatedList=[];
    freeNodes=[firstState];
    goalNode=list(goal);
    success=False
    n=0
    while len(freeNodes)!=0 and not(success) and n<=L:
        firstState=freeNodes[0];
        freeNodes.pop(0);
        closedNodes.append(firstState);
        generatedList=successorsOf(firstState);#successorsOf is the function  you need to create to genere the node fron exixte node
        generatedList = [x for x in generatedList if x not in freeNodes and x not in closedNodes]
        n+=1
        if (firstState==goalNode) :
            success=True;
            break
        freeNodes=generatedList+freeNodes;
    for x in closedNodes:
        affiche(x)
        
    return (closedNodes,success,len(freeNodes+closedNodes))

def recherchBFS(s0,goal):
    firstState=list(s0);
    closedNodes=[];
    generatedList=[];
    freeNodes=[firstState];
    goalNode=list(goal);
    success=False
    while len(freeNodes)!=0 and not(success):
        
        firstState=freeNodes[0];
        freeNodes.pop(0);
        closedNodes.append(firstState);
        generatedList=successorsOf(firstState);#successorsOf is the function  you need to create to genere the node fron exixte node
        generatedList = [x for x in generatedList if x not in freeNodes and x not in closedNodes]
        if (firstState==goalNode) :
            success=True;
            break
        freeNodes+=generatedList;
    for x in closedNodes:
        affiche(x)
    return (closedNodes,success,len(freeNodes+closedNodes))
#atoile
def h(s0,goal):
  nb=0
  for i in range(len(s0)):
    for j in range(len(s0[i])):
      if (s0[i][j]!=goal[i][j])and (s0[i][j]!=0):
        nb=nb+1
  return nb

def aetoile(s0,goal):
  success=False 
  n = 0
  freeNodes = []
  freeNodes.append(s0)
  closedNodes = [] 
  generatedList=[]
  while (freeNodes!=[]) and (not success) and (n < 100): 
    firstState = freeNodes[0] 
    n += 1
    freeNodes.remove(firstState) 
    closedNodes.append(firstState)
    generatedList = successorsOf(firstState)
    affiche(firstState)
    if (firstState==goal) :
        success=True;
        break
    freeNodes=generatedList+freeNodes;

    freeNodes.sort(key = lambda el:(n+h(el,goal))) 

  if n == 100:
    print("Inconclusive research")
  else:
    print(" \n --> Goal  attend in ",n," steps .")
  return (closedNodes,success,len(freeNodes+closedNodes))

recherchBFS(s0,goal)


