from collections import deque

def read_input(input_file = "./input.txt"):
  with open('./input.txt', 'r') as f:
    data = f.read().strip().split("\n\n")

  mazes = []
  for entry in data:
    temp = entry.split("\n")
    maze = [x.replace(' ', '') for x in temp[1::]]
    mazes.append([temp[0], maze])

  return mazes

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
    
    for dx, dy in dmap.keys():
      new_r, new_c = r + dy, c + dx
        
      if (0 <= new_r < len(maze) and 
        0 <= new_c < len(maze[0]) and 
        (new_r, new_c) not in visited and
        maze[new_r][new_c] != '#'):
        
        visited[(new_r, new_c)] = (r, c)
        queue.append((new_r, new_c))

def solve_maze(maze, start):
  path = bfs(maze, start)
  
  output = "S "
  for i in range(1, len(path)):
    prev_x, prev_y = path[i - 1]
    curr_x, curr_y = path[i]
    
    diff = (curr_x - prev_x, curr_y - prev_y)
    
    output += dmap[diff]
  output += "G"
  
  return output

def parse_mazes(mazes):
  final = []

  for maze in mazes:
    name, maze = maze
    start = None
    for i, e in enumerate(maze):
      try:
        start = (i, e.index("S"))
      except ValueError:
        pass

    final.append(f"{name}\n{solve_maze(maze, start)}")
    
  return final

if __name__ == "__main__":
  final = parse_mazes(read_input())

  print('\n\n'.join(final))
