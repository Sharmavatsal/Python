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



def dfs(graph, start):
    path = []  
    stack = [start]  
    
    while stack:   
        v = stack.pop()  
        
        if v not in path:
            path.append(v)  
            print("Path:", path)
            
            for n in reversed(graph[v]):
                if n not in path:
                    stack.append(n)
            
            print("Stack:", stack)
            print()
    
    print("Final Path:", path)
    return
def main():
    a=int(input("Start value : "))
    dfs(graph, a)
main()


