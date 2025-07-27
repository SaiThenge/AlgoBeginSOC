import sys
import heapq
from collections import deque

def solve_dijkstra(maze):
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    
    start = None
    end = None
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    
    if not start or not end:
        return -1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heap = []
    heapq.heappush(heap, (0, start[0], start[1]))
    visited = [[float('inf')] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = 0
    
    while heap:
        cost, x, y = heapq.heappop(heap)
        
        if (x, y) == end:
            return cost
        
        if cost > visited[x][y]:
            continue
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                cell = maze[nx][ny]
                new_cost = cost
                
                if cell == '.':
                    new_cost += 1
                elif cell == 'T':
                    new_cost += 3
                elif cell == 'M':
                    new_cost += 5
                elif cell == 'E':
                    new_cost += 1
                
                if new_cost < visited[nx][ny]:
                    visited[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))
    
    return -1

def solve_bfs(maze):
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    
    start = None
    end = None
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    
    if not start or not end:
        return -1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, cost = queue.popleft()
        
        if (x, y) == end:
            return cost
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                cell = maze[nx][ny]
                new_cost = cost
                
                if cell == '.':
                    new_cost += 1
                elif cell == 'T':
                    new_cost += 3
                elif cell == 'M':
                    new_cost += 5
                elif cell == 'E':
                    new_cost += 1
                
                visited[nx][ny] = True
                queue.append((nx, ny, new_cost))
    
    return -1

def main():
    print("MAZE SOLVER - Choose input method:")
    print("1. Enter maze manually")
    print("2. Generate random maze")
    choice = input("Your choice (1/2): ").strip()
    
    if choice == '1':
        print("\nEnter your maze (one row per line, space between cells):")
        print("Example:")
        print("S . T")
        print(". M E")
        print("Type 'done' when finished\n")
        
        maze = []
        while True:
            line = input().strip()
            if line.lower() == 'done':
                break
            if line:
                maze.append(line.split())
        
        print("\nYour maze:")
        for row in maze:
            print(' '.join(row))
        
    elif choice == '2':
        import random
        rows = int(input("Enter rows (3-10): ") or 5)
        cols = int(input("Enter cols (3-10): ") or 5)
        
        maze = [['.' for _ in range(cols)] for _ in range(rows)]
        maze[0][0] = 'S'
        maze[rows-1][cols-1] = 'E'
        
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] in ['S', 'E']:
                    continue
                rand = random.random()
                if rand < 0.1:
                    maze[i][j] = 'T'
                elif rand < 0.2:
                    maze[i][j] = 'M'
        
        print("\nGenerated maze:")
        for row in maze:
            print(' '.join(row))
    
    else:
        print("Invalid choice!")
        return
    
    dijkstra_cost = solve_dijkstra(maze)
    bfs_cost = solve_bfs(maze)
    
    print(f"\nDijkstra solution cost: {dijkstra_cost}")
    print(f"BFS solution cost: {bfs_cost}")

if __name__ == "__main__":
    main()