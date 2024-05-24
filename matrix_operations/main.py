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

def multiadd(*args):
  print(args)
  result = args[0]
  for arg in args[1:]:
    result = addition(result, arg)
  return result

def multiplication(a, b):
  return [[sum(c * d for c, d in zip(ar, bc)) 
            for bc in zip(*b)]
              for ar in a]

final = []
for op in operations:
  oop = op
  op = op.split()
  to_be_evaluated = []
  while "*" in op:
    i = op.index("*")
    b = op.pop(i+1)
    _ = op.pop(i)
    a = op.pop(i-1)
    to_be_evaluated.append(f"multiplication(matrices['{a}'], matrices['{b}'])")

  op = [x for x in op if x != "+"] 
  for x in op:
    to_be_evaluated.append(f"matrices['{x}']")

  result = eval(f"multiadd({', '.join(to_be_evaluated)})")
  
  final.append(f"{oop}\n" + "\n".join([" ".join(map(str, x)) for x in result]))
  
print("\n\n".join(final))