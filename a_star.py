import heapq

def a_star(graph, start, goal, heuristic, cost):
    priority_queue = []
    heapq.heappush(priority_queue, (0+heuristic[start], start))
    visited = set()
    parent = {start: None}
    g_cost = {start: 0}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            break
        
        for neighbor in graph[current_node]:
            new_cost = g_cost[current_node] + cost[(current_node, neighbor)]
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost +  heuristic[neighbor]
                heapq.heappush(priority_queue, (f_cost, neighbor))
                parent[neighbor] = current_node

    node = goal
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return g_cost[goal],path

graph = {
    'S' : ['A', 'G'],
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['D', 'G'],
    'D' : ['G']
}

heuristic = {
    'S' : 5,
    'A' : 3,
    'B' : 4,
    'C' : 2,
    'D' : 6,
    'G' : 0
}

cost = {
    ('S', 'A') : 1,
    ('S', 'G') : 10,
    ('A', 'B') : 2,
    ('A', 'C') : 1,
    ('B', 'D') : 5,
    ('C', 'D') : 3,
    ('C', 'G') : 4,
    ('D', 'G') : 2
}

c,path = a_star(graph,'S','G',heuristic,cost)
print("The path from 'S' to 'G' is: ",path,"with cost: ",c)