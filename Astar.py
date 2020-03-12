import numpy as np

class Node:
    def __init__(self,position,parent):
        self.position=position
        self.parent=parent

        self.f_cost=0
        self.g_cost=0
        self.h_cost=0
        self.traversible=True

    def __eq__(self, other):
        return self.position==other.position




def min_f_cost(list):
    min=1000
    index=0
    for i in range(len(list)):
        if list[i].f_cost<min:
            min=list[i].f_cost
            index=i
    return index

def astar(map,start,end):
    Start=Node(start,None)
    End=Node(end,None)

    Open=[Start]
    Closed=[]

    while len(Open)>0:
        min_index = min_f_cost(Open)
        current = Open[min_index]
        Closed.append(Open.pop(min_index))
        if current == End:
            path = []
            current_node=current
            while current_node is not None:
                path.append(current_node.position)
                current_node=current_node.parent
            return path[::-1]

        adj_pos = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
        children = []
        for pos in adj_pos:
            if map[pos[0],pos[1]] == 1:
                continue
            new_x, new_y = (current.position[0]+pos[0],current.position[1]+pos[1])
            child=Node((new_x,new_y),current)

            children.append(child)

        for child in children:
            for closed_child in Closed:
                if child == closed_child:
                    continue

            child.g_cost = current.g_cost + 1
            child.h_cost = ((child.position[0]-End.position[0])**2)+((child.position[1]-End.position[1])**2)
            child.f_cost = child.h_cost+child.g_cost

            for open_node in Open:
                if child == open_node and child.g_cost > open_node.g_cost:
                    continue

            Open.append(child)


map=np.zeros((5,5))
print(map)
start=(0,0)
end=(5,5)
print(astar(map,start,end))







