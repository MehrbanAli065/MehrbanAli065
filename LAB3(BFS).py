class BFS:
    def __init__(self,state,parent,actions,total_cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.total_cost=total_cost


graph={'A': BFS('A',None,['B','C','E'],None),
       'B': BFS('B',None,['A','D','E'],None),
       'C': BFS('C',None,['A','F','G'],None),
       'D': BFS('D',None,['B','E'],None),
       'E': BFS('E',None,['A','B','D'],None),
       'F': BFS('F',None,['C'],None),
       'G': BFS('G',None,['C'],None)
       }
print(graph.keys())
def BFS():
    initialstate='D'
    goalstate='F'
graph={'A': BFS('A',None,['B','C','E'],None),
       'B': BFS('B',None,['A','D','E'],None),
       'C': BFS('C',None,['A','F','G'],None),
       'D': BFS('D',None,['B','E'],None),
       'E': BFS('E',None,['A','B','D'],None),
       'F': BFS('F',None,['C'],None),
       'G': BFS('G',None,['C'],None)
       }
frontier=[initialstate]
explored=[]
while len(frontier)!=0:
    currentnode=frontier.pop(0)
    explored.append(currentnode)
    for child in graph[currentnode].actions:
        if child not in frontier and child not in explored:
            graph[child].parent=currentnode
            if graph[child].state==goalstate:
                return actionSequence(graph,initialstate,goalstate)
            frontier.append(child)
solution=BFS
print(solution)



