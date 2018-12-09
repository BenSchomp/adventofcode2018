# day 6, part 1

file = open('day06-input.txt', 'r')

nodes = dict()
xMin = xMax = yMin = yMax = None
i = 0
for line in file:
  i += 1
  coord = line.strip()
  (x, y) = coord.split(',')
  x = int(x)
  y = int(y)
  p = ( x, y )
  nodes[i] = p

  if not xMin or x < xMin:
    xMin = x
  if not xMax or x > xMax:
    xMax = x
  if not yMin or y < yMin:
    yMin = y
  if not yMax or y > yMax:
    yMax = y

file.close()

# try out all spaces 1 away first, then try all spaces 2 away
# have to look at ALL the 2's though ... but as soon as you find a negative number, you're done
# if you find more than 1, you can stop (its a 0)
# if you find only 1, its positive the number

grid = dict()
for x in range(xMin, xMax+1):
  for y in range(yMin, yMax+1):
    done = False

    distances = dict()
    for key, n in nodes.items():
      d = abs(x-n[0]) + abs(y-n[1])
      if d == 0:
        grid[(x,y)] = key
        done = True
        break
      else:
        distances[key] = d

    if done:
      continue

    tmp = sorted(distances.items(), key=lambda l: l[1])
    if tmp[0][1] == tmp[1][1]:
      grid[(x,y)] = 0
      continue

    grid[(x,y)] = tmp[0][0]  

infinite = set()
#for key, n in nodes.items():
#  if n[0] == xMin or n[0] == xMax:
#    infinite.add( key )
#  if n[1] == yMin or n[1] == yMax:
#    infinite.add( key )

for y in range(yMin, yMax+1):
  infinite.add( grid[(xMin,y)] )
  infinite.add( grid[(xMax,y)] )
for x in range(xMin, xMax+1):
  infinite.add( grid[(x,yMin)] )
  infinite.add( grid[(x,yMax)] )

maxNode = (None, 0)
values = sorted(grid.values())
result = dict()
for key in nodes:
  if key in infinite:
    continue

  c = values.count(key)
  result[key] = c
  if c > maxNode[1]:
    maxNode = (key, c)

print( maxNode )
#print( sorted( result.items(), key=lambda l:l[1] ) )
