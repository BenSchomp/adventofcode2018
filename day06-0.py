# day 6, part 1
# 

import numpy

size = 10
grid = numpy.zeros( (size,size) )
infinite = set()
xMin = size
xMax = 0 
yMin = size
yMax = 0 


file = open('day06-input.txtx', 'r')
i = 0
for line in file:
  i += 1
  coord = line.strip()
  pieces = coord.split(',')
  x = int(pieces[0])
  y = int(pieces[1])
  grid[x,y] = i * -1

  if x < xMin:
    xMin = x
  if x > xMax:
    xMax = x
  if y < yMin:
    yMin = y
  if y > yMax:
    yMax = y
file.close()

for x in range(xMin, xMax+1):
  if grid[x,yMin] < 0:
    infinite.add( grid[x,yMin] )
  if grid[x,yMax] < 0:
    infinite.add( grid[x,yMax] )

for y in range(yMin, yMax+1):
  if grid[xMin,y] < 0:
    infinite.add( grid[xMin,y] )
  if grid[xMax,y] < 0:
    infinite.add( grid[xMax,y] )

print( grid )
print( xMin, xMax, yMin, yMax )
print( infinite )
print

# try out all spaces 1 away first, then try all spaces 2 away
# have to look at ALL the 2's though ... but as soon as you find a negative number, you're done
# if you find more than 1, you can stop (its a 0)
# if you find only 1, its positive the number

for x in range(xMin, xMax+1):
  for y in range(yMin, yMax+1):
    if grid[x,y] != 0:
      continue

    delta = 0
    found = 0
    while not found:
      delta += 1

      for dx in range(-delta, delta+1):
        for dy in range(-delta, delta+1):
          curX = x + dx
          curY = y + dy

          if curX < 0 or curX >= size or curY < 0 or curY >= size:
            continue

          if abs(dx) + abs(dy) != delta:
            continue

          value = grid[curX, curY]
          if value < 0:
            found += 1
            found_value = value

    if found == 1:
      grid[x, y] = -found_value

tally = dict()
for x in range(xMin, xMax+1):
  for y in range(yMin, yMax+1):
    value = abs(grid[x,y])
    if value != 0 and -value not in infinite:
      if value in tally:
        tally[value] += 1
      else:
        tally[value] = 1

print( grid )
print
print( tally )


