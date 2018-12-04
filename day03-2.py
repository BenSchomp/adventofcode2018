# day 3, part 2
#  same problem spec as part 1, but after the grid is constructed,
#    need to run through the input again and find the rectangle
#    that has no overlaps (ie all points have count == 1)
import numpy
file = open('day03-input.txt', 'r')

maxX = 1000
maxY = 1000
grid = numpy.zeros( (maxX,maxY) )

lines = []
for line in file:
  pieces = line.strip().split(' ')
  id = pieces[0][1:]
  start = pieces[2][:-1].split(',')
  size = pieces[3].split('x')

  data = [ id, int(start[0]), int(start[1]), int(size[0]), int(size[1]) ]
  lines.append( data )

  x = data[1]
  y = data[2]
  w = data[3]
  h = data[4]

  for i in range(x, x+w):
    for j in range(y, y+h):
      grid[j,i] += 1

file.close()

# now iterate through them again, finding a rectangle
#  whose counts are all 1
for line in lines:
  x = line[1]
  y = line[2]
  w = line[3]
  h = line[4]

  found = True
  for i in range(x, x+w):
    if not found:
      break

    for j in range(y, y+h):
      if grid[j,i] != 1:
        found = False
        break

  if found:
    print( "found id: %s" % line[0] )
    exit()

print( "Not found!" )

