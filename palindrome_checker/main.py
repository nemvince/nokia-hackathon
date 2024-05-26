import re

with open('./input.txt', 'r') as f:
  data = f.read().strip().split("\n")

for word in data:
  word = re.compile(r'[\W_]+').sub('', word).lower()
  if word == word[::-1]:
    print(f"YES, {len(set(word))}")
  else:
    print("NO, -1")
    
# code golfed :)