from collections import deque

with open('./input.txt', 'r') as f:
  data = f.read().strip().split("\n\n")

mazes = []
for maze in data:
  temp = maze.split("\n")
  mazes.append([temp[0], temp[1::]])

directions = [
  (-1, 0, 'U '),
  (1, 0, 'D '),
  (0, -1, 'L '),
  (0, 1, 'R '),
]

def bfs(maze, start, goal):
  queue = deque([start])
  visited = set()
  visited.add(start)
  parent = {start: None}
  
  while queue:
      current = queue.popleft()
      
      if current == goal:
        path = []
        while current:
          path.append(current)
          current = parent[current]
        path.reverse()
        return path
        
      r, c = current
      for dr, dc, _ in directions:
        nr, nc = r + dr, c + dc
        if (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and
          maze[nr][nc] != '#' and (nr, nc) not in visited):
          queue.append((nr, nc))
          visited.add((nr, nc))
          parent[(nr, nc)] = current

  return None

final = []

for maze in mazes:
  name = maze[0]
  maze = maze[1]
  start, goal = None, None
  for i, e in enumerate(maze):
    try:
      start = (i, e.index("S"))
    except ValueError:
      try:
        goal = (i, e.index("G"))
      except ValueError:
        pass
    
  
  path = bfs(maze, start, goal)
  output = "S "
  
  for i in range(1, len(path)):
    r1, c1 = path[i-1]
    r2, c2 = path[i]
    for dr, dc, d in directions:
      if (r1 + dr == r2) and (c1 + dc == c2):
        output += d
        break
  output += "G"
  final.append(f"{name}\n{output}")

print('\n\n'.join(final))
