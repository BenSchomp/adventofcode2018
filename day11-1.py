serialNumber = 8868

def getCellScore( x, y ):
  rackId = x + 10
  powerLevel = rackId * y
  powerLevel += serialNumber
  powerLevel *= rackId
  powerLevel = int(powerLevel / 100)
  powerLevel = powerLevel % 10
  powerLevel -= 5
  return powerLevel

def getSquareScore( x, y ):
  squareScore = 0
  for i in range(3):
    for j in range(3):
      squareScore += getCellScore( x+i, y+j )
  return squareScore

scores = {}
for y in range(1, 297):
  for x in range(1, 297):
    squareScore = getSquareScore( x, y )
    scores[x,y] = squareScore

results = sorted(scores, key=scores.get)
result = results.pop()
print( 'x,y:', result )
print( 'largest power level:', getSquareScore( result[0], result[1] ) )

