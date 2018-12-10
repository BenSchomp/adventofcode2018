# day 9, part 2
# 423 players; last marble is worth 71944 points
# original playuers score ... if NUM_MARBLES x 100

NUM_PLAYERS = 423
NUM_MARBLES = 7194400

marbles = []

marble = 0
marbles.append( 0 )
cur = 0
scores = {}
highScore = 0
highScorePlayer = -1
#print( marbles )

phase = 1
marble = 1
player = 0
count = 0
while marble <= NUM_MARBLES:
  count += 1
  if count < 23:
    if cur == len(marbles)-2:
      cur += 2
      marbles.append( marble )
    else:
      cur += 2
      if cur >= len(marbles):
        cur -= len(marbles)
      marbles.insert( cur, marble )

  else: # marble is divisible by 23
    count = 0
    if not player in scores:
      scores[player] = 0
    scores[player] += marble
    cur -= 7
    if cur < 0:
      cur = len(marbles) + cur
    removed = marbles[ cur ]
    del marbles[ cur ]
    scores[player] += removed

    if scores[player] > highScore:
      highScore = scores[player]

    if marble == NUM_MARBLES / 100:
      highScorePlayer = player
      print( 'Marble %d: highScore = %d, highScorePlayer = %d **'  % (marble, highScore, highScorePlayer) )

  if not marble % 100000:
    if highScorePlayer >= 0:
      print( 'Marble %d: highScore = %d, highScorePlayer = %d, scores[x] = %d'  % (marble, highScore, highScorePlayer, scores[highScorePlayer]) )
    else:
      print( 'Marble %d: highScore = %d, highScorePlayer = %d'  % (marble, highScore, highScorePlayer) )

  #print( marbles )

  marble += 1
  player += 1
  if player >= NUM_PLAYERS:
    player = 0

print( 'Marble %d: highScore = %d, highScorePlayer = %d, scores[x] = %d'  % (marble, highScore, highScorePlayer, scores[highScorePlayer]) )
print( 'Final Score: %d' % scores[highScorePlayer] )

