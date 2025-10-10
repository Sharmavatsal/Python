import heapq

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

heuristic = {
    1:2,
    2:9,
    9:8,
    #8:2,
        3:7,
        7:0
    #3:7,
    #7:0
   
}

def bstfs(graph, start, goal, heuristic):
    path = []
    pq = [(heuristic.get(start, float('inf')), start)] 
    
    while pq: 
        h, v = heapq.heappop(pq)
        
        if v not in path: 
            path.append(v)
            print("Path:", path)
            
            if v == goal:
                print("Goal reached:", goal)
                print("Final Path:", path)
                return
            
            for n in graph[v]:
                if n not in path:
                    h_val = heuristic.get(n, float('inf'))
                    heapq.heappush(pq, (h_val, n))
            print("Priority Queue:", pq)
            print()
    
    print("Goal not found")
    print("Final Path:", path)

def main():
    a = int(input("Start value : "))
    b = int(input("Goal value : "))
    bstfs(graph, a, b, heuristic)

main()
