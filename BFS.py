from collections import deque

graph = {
    1: [2, 3, 4],
    2: [9, 8],
    3: [7],
    4: [5, 6],
    5: [4],
    6: [4],
    7: [3],
    8: [2],
    9: [2]
}

def bfs(graph, start):
    path = []
    queue = deque([start])
    
    while queue:   
        v = queue.popleft()
        
        if v not in path:   
            path.append(v)
            print("Path:", path)
            
            for n in graph[v]:
                if n not in path:   
                    queue.append(n)
            print("Queue:", queue)
            print()
    
    print("Final Path:", path)

# Run BFS
def main():
    a=int(input("Start value : "))
    bfs(graph, a)
main()

