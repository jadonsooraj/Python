#breadth first search(uninformed search)
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':['H','I'],
    'E':[],
    'F':['G'],
    'H':[],
    'I':['G'],
    'G':[]
}
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the BFS")
bfs(visited,graph,'A')