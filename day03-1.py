# day 3, part 1
#  a 2d coordinate space
#  input is an id, starting location, and rectangle size
#    ie #1 @ 1,3: 4x4
#  find the number of overlapping grid points
import numpy
file = open('day03-input.txt', 'r')

# problem states 1000x1000 space
maxX = 1000
maxY = 1000
grid = numpy.zeros( (maxX,maxY) )

lines = []
for line in file:
  pieces = line.strip().split(' ')
  id = pieces[0][1:]
  start = pieces[2][:-1].split(',')
  size = pieces[3].split('x')

  # each row is: id, startX, startY, width, height
  data = [ id, int(start[0]), int(start[1]), int(size[0]), int(size[1]) ]
  lines.append( data )

  x = data[1]
  y = data[2]
  w = data[3]
  h = data[4]

  # for this rectangle, for each point, increment a counter
  for i in range(x, x+w):
    for j in range(y, y+h):
      grid[j,i] += 1

file.close()

# any point with a count > 1 has been "overlapped"
count = 0
for i in range(maxX):
  for j in range(maxY):
    if grid[j,i] > 1:
      count += 1

print( "overlaps: %d" % count )

