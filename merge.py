import os

merged = ""

for f in os.listdir('source/data'):
  file = os.path.join('source/data', f)
  if os.path.isfile(file):
    with open(file, 'r') as o:
      data = o.read()
    merged += data + '\n'

with open('source/index.html.md', 'w') as f:
  f.write(merged)