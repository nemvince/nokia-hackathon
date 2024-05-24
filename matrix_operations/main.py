import re

with open('./input.txt', 'r') as f:
  input = f.read().strip().split("\n\n")

opi = input.index("operations")
temp = [x.split("\n") for x in input[1:opi]]

operations = input[opi+1].split("\n")
matrices = {}
for entry in temp:
  matrix = []
  for line in entry[1:]:
    matrix.append([int(x) for x in line.split()])
  matrices[entry[0]] = matrix

def addition(a, b):
  return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def multiplication(a, b):
  return [[sum(c * d for c, d in zip(ar, bc)) 
            for bc in zip(*b)]
              for ar in a]

final = []
for op in operations:
  matrix_names = re.findall(r'[A-Z]', op)
  ops = re.findall(r'[*+]', op)
  
  result = matrices[matrix_names[0]]
  for i in range(len(ops)):
    if ops[i] == "+":
      result = addition(result, matrices[matrix_names[i+1]])
    else:
      result = multiplication(result, matrices[matrix_names[i+1]])
  
  final.append(f"{op}\n" + "\n".join([" ".join(map(str, x)) for x in result]))
  
print("\n\n".join(final))