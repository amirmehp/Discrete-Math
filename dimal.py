# Discrete Math Library
# Written by Amirmohammad Mehdipour

import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import matplotlib.pyplot as plt

def draw_matrix_graph(matrix):
    n = len(matrix)

    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)

    fig, ax = plt.subplots(figsize=(10, 10))

    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                dx = x[j] - x[i]
                dy = y[j] - y[i]

                dist = np.sqrt(dx**2 + dy**2)

                line_length = dist * 0.85
                angle = np.arctan2(dy, dx)

                ax.arrow(x[i], y[i], 
                         line_length * np.cos(angle), 
                         line_length * np.sin(angle), 
                         head_width=0.05, 
                         head_length=0.1, 
                         fc='black', 
                         ec='black',
                         alpha=0.5,
                         length_includes_head=True)

    ax.scatter(x, y, s=500, c='skyblue', edgecolors='black', zorder=10)
    
    for i in range(n):
        ax.text(x[i], y[i], str(i), 
                ha='center', 
                va='center', 
                fontweight='bold', 
                fontsize=12,
                zorder=11)

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.show()


def join_matrix(m1, m2):
    m = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            row = []
            for j in range(len(m1)):
                row.append(m1[i][j] or m2[i][j])
            m.append(row)
        return m
    else:
        print("Matrices are not match")

def meet_matrix(m1, m2):
    m = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            row = []
            for j in range(len(m1)):
                row.append(m1[i][j] and m2[i][j])
            m.append(row)
        return m
    else:
        print("Matrices are not match")


def bool_sum(n1, n2):
    if n1 == 0 and n2 == 0:
        return 0
    else:
        return 1
        
def bool_multiply(m1, m2):
    if len(m1) == len(m2[0]):
        m = len(m1)
        n = len(m2)
        p = len(m2[0]) if m2 else 0
        m3 = [[0] * p for _ in range(m)]

        for i in range(m):
            for j in range(p):
                for k in range(n):
                    m3[i][j] = m3[i][j] or (m1[i][k] and m2[k][j])
                    if m3[i][j]:
                        break
        return m3
    else:
        print("Your rows and cols don't add up")

def relation_matrix_n(matrix, n):
    for i in range (1, n):
        matrix = bool_multiply(matrix, matrix)
    return matrix

def transpose(m):
    transposed = []
    for i in range(len(m[0])):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        transposed.append(row)
    return transposed

def is_matrix_symetric(m):
    if m == transpose(m):
        return True
    else:
        return False

def identity_matrix(n):
    m = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        m.append(row)
    return m

def is_matrix_antisymetric(m):
    if len(m[0]) == len(m):
        m = meet_matrix(m, transpose(m))
        qotr = []
        for i in range(0, len(m[0])):
            for j in range(0, len(m)):
                if i == j:
                    qotr.append(m[i][j])
                elif m[i][j] != 0:
                    return False
        for n in qotr:
            if n <= 1:
                return True
            else:
                return False

def is_matrix_transitive(m):
    if bool_multiply(m, m) <= m:
        return True
    else:
        return False

def symetric_closure(m):
    return join_matrix(m, identity_matrix(len(m)))

def antisymetric_closure(m):
    return identity_matrix(len(m))

def transmitive_closure(m):
    for i in range(len(m[0])):
        m = join_matrix(m, m)
    return m

def deg(m):
    degrees = [0]*len(m)
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                degrees[i] += 1
    return degrees

def complement_matrix(m):
    n = len(m)
    for i in range(0, n):
        for j in range(0, n):
            m[i][j] = 1 - m[i][j]
    return m

def is_subgraph(g, h):
    if len(g) > len(h):
        print("ERR: Matrices do not match")
        exit(1)
    for i in range(len(g[0])):
        for j in range(len(g)):
            if (g[i][j] == 1 and h[i][j] == 0):
                return False
            elif(g[i][j] == 0 and h[i][j] == 1):
                return False
            
    return True

def dfs(graph, start, path):
    stack = [start]
    while stack:
        vertex = stack[-1]
        if graph[vertex]:  
            next_vertex = graph[vertex].pop()
            graph[next_vertex].remove(vertex)
            stack.append(next_vertex) 
        else:
            path.append(stack.pop())

def is_matrix_connected(matrix):
    def dfs(node, visited):
        visited[node] = True
        for neighbor in range(len(matrix)):
            if matrix[node][neighbor] and not visited[neighbor]:
                dfs(neighbor, visited)
                
    if not matrix or not matrix[0]:
        return False

    n = len(matrix)
    visited = [False] * n

    dfs(0, visited)

    return all(visited)

def path_length(m, w, path):
    length = 0
    for i in range(len(path)-1):
        u = path[i] - 1
        v  = path[i + 1] - 1
        if m[u][v] == 0:
            print(f"ERR: No edges between {path[i]} and {path[i+1]}")
            exit(1)
        else:
            length += w[u][v]
    return length

def eulerian_path(g):
    adj = {}
    for i in range(len(g)):
        adj[i] = []
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == 1:
                adj[i].append(j)

    print("Adjacency:", adj)
    odd_degree_vertices = [v for v in adj if len(adj[v]) % 2 != 0]
    print("Odd Degrees:", odd_degree_vertices)
    if len(odd_degree_vertices) not in [0, 2]:
        return None 

    start_vertex = odd_degree_vertices[0] if odd_degree_vertices else next(iter(adj))

    path = []
    dfs(adj, start_vertex, path)

    return path[::-1]

def dijkstra(start, end, adj, weight):
    path = []
    length = {}
    visited = set()
    T = [vertex for vertex in range(len(adj)) if vertex != start]

    for t in T:
        length[t] = weight[start][t] if adj[start][t] == 1 else float('inf')

    path.append(start)

    while T:
        min_key = min(T, key=lambda t: length.get(t, float('inf')))
        min_value = length[min_key]

        path.append(min_key)

        if min_key == end:
            print(f"The Shortest path from {start} to {end} is {path} with length {min_value}")
            return

        # Calculating the length of the path (Unnecessary)
        for neighbor in T:
            if adj[min_key][neighbor] == 1: 
                new_length = min_value + weight[min_key][neighbor]
                if neighbor not in length or new_length < length[neighbor]:
                    length[neighbor] = new_length

        visited.add(min_key)
        T.remove(min_key)
