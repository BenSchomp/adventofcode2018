import numpy
file = open('day03-input.txt', 'r')

lines = []
for line in file:
  pieces = line.strip().split(' ')
  id = pieces[0][1:]
  start = pieces[2][:-1].split(',')
  size = pieces[3].split('x')

  lines.append( [ id, start, size ] )
file.close()

maxX = 1000
maxY = 1000
grid = numpy.zeros( (maxX,maxY) )

for line in lines:
  x = int(line[1][0])
  y = int(line[1][1])
  w = int(line[2][0])
  h = int(line[2][1])

  for i in range(x, x+w):
    for j in range(y, y+h):
      grid[j,i] += 1


count = 0
for i in range(maxX):
  for j in range(maxY):
    if grid[j,i] > 1:
      count += 1

print( count )

