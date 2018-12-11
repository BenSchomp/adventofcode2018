# day 6, part 1
# track multiple points and their movement deltas across a 2d plane
# stop when the bounding box is at a minimum and see if there are letters

point = 0
points = {}
sky = set()
global xRange, yRange, xMin, xMax, yMin, yMax

# parse input
with open( 'day10-input.txt' ) as fIn:
  import re
  for line in fIn:
    point += 1
    pieces = re.findall(r'[-]?\d+', line)
    startPos = (int(pieces[0]), int(pieces[1]))
    delta = (int(pieces[2]), int(pieces[3]))
    points[point] = [startPos[0], startPos[1], delta]

# do one time tick: update all point positions, and min, max, and ranges
def update( updatePositions=True ):
  global points, sky, xRange, yRange, xMin, xMax, yMin, yMax

  for v in points.values():
    # update points according to their deltas
    if updatePositions:
      v[0] += v[2][0]
      v[1] += v[2][1]

  sky.clear()
  xMin = xMax = points[1][0]
  yMin = yMax = points[1][1]

  # set sky bits and update min, max, and ranges
  for v in points.values():
    sky.add( (v[0], v[1] ) )

    if v[0] < xMin:
      xMin = v[0]
    if v[0] > xMax:
      xMax = v[0]
    if v[1] < yMin:
      yMin = v[1]
    if v[1] > yMax:
      yMax = v[1]

  xRange = xMax - xMin
  yRange = yMax - yMin

# display the sky grid
def draw():
  global points, sky, xRange, yRange, xMin, yMin
  print()

  for i in range(yRange+1):
    y = i + yMin
    for j in range(xRange+1):
      x = j + xMin
      if (x, y) in sky:
        print( '#', end='' )
      else:
        print( '.', end='' )
    print( flush=True )


# seed everything w starting positions
t = 0
update(False)

min_yRange = yRange
while True:
  if yRange < 200:
    draw()
    print( 't = %d' % t )
  
  update()
  t += 1

  if yRange < min_yRange:
    min_yRange = yRange
  else:
    # this is not a guaranteed stop condition, but it works for the given input
    exit()

