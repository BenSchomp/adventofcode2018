serialNumber = 8868
serialNumber = 18

scores = {}

cellScores = {}
def getCellScore( x, y ):
  if (x,y) not in cellScores:
    rackId = x + 10
    powerLevel = rackId * y
    powerLevel += serialNumber
    powerLevel *= rackId
    powerLevel = int(powerLevel / 100)
    powerLevel = powerLevel % 10
    powerLevel -= 5
    scores[x,y,1] = powerLevel
  else:
    powerLevel = cellScores(x,y)

  return powerLevel

squareScores = {}
def getSquareScore( x, y, size ):
  squareScore = 0
  if size == 1:
    squareScore = getCellScore( x, y )
    squareScores[x,y] = {}
    squareScores[x,y][size] = squareScore

  elif (x,y) in squareScores and size in squareScores[x,y]:
    return squareScores[x,y][size]

  else:
    squareScore = getSquareScore(x,y,size-1)

    j = size
    for i in range(size):
      squareScore += getCellScore(x+i, y+j)

    i = size
    for j in range(size):
      squareScore += getCellScore(x+i, y+j)

    squareScores[x,y][size] = squareScore

  return squareScore

def showScore():
  global scores
  results = sorted(scores, key=scores.get)
  result = results.pop()
  print( ' + x,y,s:', result )
  print( ' + largest power level:', getSquareScore( result[0], result[1], result[2] ) )

MAX = 300
for y in range(1, MAX):
  print( "Starting row: %d" % y )
  for x in range(1, MAX):
    for s in range( 3, 4 ):
      if( x+s > MAX or y+s > MAX ):
        break

      squareScore = getSquareScore( x, y, s )
      scores[x,y,s] = squareScore

  print( 'Largest so far ...' )
  showScore()

print( 'Done!' )
showScore()


