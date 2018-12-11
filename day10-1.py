# day 6, part 1
#

import re, numpy

NUM_SECS = 3

sky = None
points = {}
point = 0
xRange = yRange = xMin = xMax = yMin = yMax = 0
with open( 'day10-input.txt' ) as fIn:
  for line in fIn:
    point += 1
    pieces = re.findall(r'[-]?\d+', line)
    startPos = (int(pieces[0]), int(pieces[1]))
    delta = (int(pieces[2]), int(pieces[3]))
    points[point] = [startPos[0], startPos[1], delta]

def updateSky( update=True ):
  global points, xRange, yRange, xMin, xMax, yMin, yMax

  for v in points.values():
    if update:
      v[0] += v[2][0]
      v[1] += v[2][1]

  xRange = yRange = xMin = xMax = yMin = yMax = 0
  for v in points.values():
    if v[0] < xMin:
      xMin = v[0]
    if v[0] > xMax:
      xMax = v[0]
    if v[1] < yMin:
      yMin = v[1]
    if v[1] > yMax:
      yMax = v[1]

    xRange = xMax - xMin + 1
    yRange = yMax - yMin + 1

def drawSky():
  global points, xRange, yRange, xMin, yMin
  print()

  sky = numpy.zeros( (xRange,yRange) )
  for k, v in points.items():
    sky[v[0]-xMin, v[1]-yMin] = k 

  for i in range(yRange):
    y = i + yMin
    for j in range(xRange):
      x = j + xMin
      if sky[x,y] > 0:
        print( '#', end='' )
      elif x == 0 and y == 0:
       print( 'X', end='' )
      else:
        print( '.', end='' )
    print( flush=True )


updateSky(False)
#drawSky()
#for t in range(NUM_SECS):
t =0
while t < 13000:
  print( t, xMin, xMax, yMin, yMax, xRange, yRange )
  updateSky()
  if xRange < 250 and yRange < 250:
    drawSky()
  t += 1

print( t, xMin, xMax, yMin, yMax, xRange, yRange )
drawSky()



