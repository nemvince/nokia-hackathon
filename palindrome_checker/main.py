import re

with open('./input.txt', 'r') as f:
  data = f.read().strip().split("\n")

pattern = re.compile(r'[\W_]+')

for word in data:
  word = pattern.sub('', word)
  word = word.lower()
  if word == word[::-1]:
    unique = len(set(word))
    print(f"YES, {unique}")
  else:
    print("NO, -1")