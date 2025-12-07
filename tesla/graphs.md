# Graph

Vertices
Edges

E <= V**2

Directed Graph - edges have a direction
Trees are directed graphs also LinkedLists


## Matrix
Have a mtrix, zeroes means free to create an edge, 1 means no edge

## Adj Matrix
Less Common
space complexity is very high
for 4 edges we have 4x4 matrix

## Adj List
def __init__(self, val):
    self.val = val
    self.neigh = []

## Matrix DFS
DFS + backtracking

def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 1:
        return 0
    if r == ROWS -1 and c == COLS - 1:
        return 1

    visit.add((r, c))
    count = 0
    count += dfs(grid, r+1, c, visit)
    count += dfs(grid, r-1, c, visit)
    count += dfs(grid, r, c+1, visit)
    count += dfs(grid, r, c-1, visit)
    visit.remove((r, c)) // remove the node for the another valid path, the node is removed, multiple points can be visited
    in different paths
    return count

ans = dfs(grid, 0, 0, set())
return ans

time Complexity = 4**(n*m)

dfs = number of paths, going as deep as we can

## Matrix BFS
BFS + Backtracking

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    q = deque()
    q.append((0, 0))
    visit.add((r, c))

    length = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            if r == ROWS-1 and c == COLS-1:
                return length
            nei = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in nei:
                if min((r+dr), (c+dc)) < 0 or r + dr == ROWS or c + dc == COLS or (r+dr, c+dc) in visit or grid[r+dr][c+dc] == 1:
                    continue

            visit.append((r+dr, c+dc))
            q.append((r+dr, c+dc))
        length += 1

bfs(grid)

we are never going to visit the same position twice, we are going via layer by layer in this algorithm
going layer by layer
bfs : shortest path algorithm,
time complexity = O(m*n)

## Adj List

hashmap to represent a nodes map

dfs : using adj

def dfs(node, target, adj, visit):
    if node in visit:
        return 0
    if node == target:
        return 1

    count = 0
    visit.add(node)
    for n in adj[node]:
        count += dfs(n, target, adj, visit)
    visit.remove(node)

    return count

bfs : using adj

def bfs(node, target, adj):
    length = 0
    q = deque()
    visit = set()
    q.append(node)
    visit.add(node)
    while q:
        for i in range(len(q)):
            curr = q.popleft()
            if curr == target:
                return length

            if curr in visit:
                continue
            for n in adj[curr]:
                visit.add(n)
                q.append(n)
        length += 1
    return length



