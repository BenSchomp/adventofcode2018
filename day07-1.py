# day 7, part 1
# build a tree stucture and walk it semi-alphabetically

tree = dict()
class Node:
  def __init__( self ):
    self.parents = []
    self.children = []
    self.done = False

  def __repr__( self ):
    p = '-'.join(self.parents)
    c = '-'.join(self.children)
    return ( '%s > [%d] > %s' % (p, self.done, c) )
  
  def addChild( self, value ):
    self.children.append( value )

  def addParent( self, value ):
    self.parents.append( value )

  def markDone( self ):
    self.done = True

  def isReady( self ):
    for i in self.parents:
      if not tree[i].done:
        return False
    return True

file = open( 'day07-input.txt' )
for line in file:
  # "Step C must be finished before step F can begin."
  this = line[5]
  next = line[36]

  if this not in tree:
    tree[this] = Node()
  tree[this].addChild( next )

  if next not in tree:
    tree[next] = Node()
  tree[next].addParent( this )
file.close()

# find starting nodes
todo = set()
for k, v in tree.items():
  if v.isReady() and not v.done:
    todo.add( k )

# walk the tree
output = ''
while todo:
  for cur in sorted(list(todo)):
    if tree[cur].isReady():
      tree[cur].done = True
      todo.remove(cur)
      output += cur
      for i in tree[cur].children:
        todo.add( i )
      break

print( output )

