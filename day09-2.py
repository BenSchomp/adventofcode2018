# day 9, part 2
# 423 players; last marble is worth 71944 points
# original playuers score ... if NUM_MARBLES x 100

NUM_PLAYERS = 423
NUM_MARBLES = 7194400

marbles = dict()
curMarble = None
class Node:
  def __init__( self ):
    self.prev = None
    self.next = None

  def __repr__( self ):
    return ( '%s< >%s' % (self.prev, self.next) )

def insert( newMarble ):
  global curMarble
  global marbles
  newNode = Node()

  l = len(marbles)
  if l == 0:
    # special case
    marbles[newMarble] = newNode
    newNode.prev = newMarble
    newNode.next = newMarble

  else:
    # advance 1 ...
    curMarble = marbles[curMarble].next

    curNode = marbles[curMarble]
    marbles[newMarble] = newNode

    newNode.next = curNode.next
    newNode.prev = curMarble

    marbles[curNode.next].prev = newMarble
    curNode.next = newMarble

  curMarble = newMarble

def remove( count ):
  global curMarble
  global marble

  for i in range( abs(count) ):
    if count > 0:
      curMarble = marbles[curMarble].next
    else:
      curMarble = marbles[curMarble].prev

  curNode = marbles[curMarble]
  prevNode = marbles[curNode.prev]
  nextNode = marbles[curNode.next]

  prevNode.next = curNode.next
  nextNode.prev = curNode.prev

  score = curMarble
  curMarble = curNode.next
  return score

scores = {}
highScore = 0

marble = 0
insert( marble )

marble = 1
player = 0
while marble <= NUM_MARBLES:
  if marble % 23: # normal marble insert
    insert( marble )

  else: # marble is divisible by 23
    if not player in scores:
      scores[player] = 0
    scores[player] += marble
    scores[player] += remove( -7 )

    if scores[player] > highScore:
      highScore = scores[player]

  marble += 1
  player += 1
  if player >= NUM_PLAYERS:
    player = 0

print( 'Final Score: %d' % highScore )

