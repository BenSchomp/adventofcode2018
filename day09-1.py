# day 9, part 1
# 423 players; last marble is worth 71944 points

NUM_PLAYERS = 423
NUM_MARBLES = 71944

marbles = []

marble = 0
marbles.append( 0 )
cur = 0
scores = {}
highScore = 0
print( marbles )

marble = 1
player = 0
while marble <= NUM_MARBLES:
  if marble % 23:
    if cur == len(marbles)-2:
      cur += 2
      marbles.append( marble )
    else:
      cur += 2
      if cur >= len(marbles):
        cur -= len(marbles)
      marbles.insert( cur, marble )

  else: # marble is divisible by 23
    if not player in scores:
      scores[player] = 0
    scores[player] += marble
    cur -= 7
    if cur < 0:
      cur = len(marbles) + cur
    removed = marbles.pop( cur )
    scores[player] += removed
    if scores[player] > highScore:
      highScore = scores[player]

  #print( marbles )

  marble += 1
  player += 1
  if player >= NUM_PLAYERS:
    player = 0

print( 'High Score: %d' % highScore )

