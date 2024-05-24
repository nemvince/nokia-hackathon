from collections import deque

with open('./input.txt', 'r') as f:
  data = f.read().strip().split("\n\n")

mazes = []
for maze in data:
  temp = maze.split("\n")
  mazes.append([temp[0], temp[1::]])

dmap = {
    (1, 0): "D ",
    (-1, 0): "U ",
    (0, 1): "R ",
    (0, -1): "L "
}

def bfs(maze, start):
  r, c = start
  queue = deque()
  visited = {}
  visited[(r, c)] = (-1, -1)
  queue.append((r, c))
  
  while queue:
    r, c = queue.popleft()
    
    if maze[r][c] == 'G':
      path = []
      while r != -1:
        path.append((r, c))
        r, c = visited[(r, c)]
      path.reverse()
      return path
    
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
      new_r, new_c = r + dy, c + dx
        
      if (0 <= new_r < len(maze) and 
        0 <= new_c < len(maze[0]) and 
        (new_r, new_c) not in visited and
        maze[new_r][new_c] != '#'):
        
        visited[(new_r, new_c)] = (r, c)
        queue.append((new_r, new_c))

final = []

for maze in mazes:
  name = maze[0]
  maze = [x.replace(' ', '').replace('.', ' ') for x in maze[1]]
  start = None
  for i, e in enumerate(maze):
    try:
      start = (i, e.index("S"))
    except ValueError:
      pass
  
  path = bfs(maze, start)
  
  output = "S "
  for i in range(1, len(path)):
    prev_x, prev_y = path[i - 1]
    curr_x, curr_y = path[i]
    
    diff = (curr_x - prev_x, curr_y - prev_y)
    
    output += dmap[diff]
  output += "G"
  
  final.append(f"{name}\n{output}")

print('\n\n'.join(final))
