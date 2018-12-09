# day 7, part 2
# build a tree stucture and walk it semi-alphabetically
# now each step takes time to do and you can have 5 workers

# tree storage
tree = dict()
class Node:
  def __init__( self, value ):
    self.parents = []
    self.children = []
    # the length of time to complete a task is the 60s + the letter of the alphabet
    self.done = (ord(value) - 64) + 60

  def __repr__( self ):
    p = '-'.join(self.parents)
    c = '-'.join(self.children)
    return ( '%s > [%d] > %s' % (p, self.done, c) )
  
  def addChild( self, value ):
    self.children.append( value )

  def addParent( self, value ):
    self.parents.append( value )

  def doWork( self ):
    self.done -= 1
  
  def isDone( self ):
    return ( self.done <= 0 )

  def isReady( self ):
    for i in self.parents:
      if not tree[i].isDone():
        return False
    return True

# build the tree
file = open( 'day07-input.txt' )
for line in file:
  # "Step C must be finished before step F can begin."
  this = line[5]
  next = line[36]

  if this not in tree:
    tree[this] = Node(this)
  tree[this].addChild( next )

  if next not in tree:
    tree[next] = Node(next)
  tree[next].addParent( this )
file.close()

# find starting nodes
todo = set()
for k, v in tree.items():
  if v.isReady() and not v.isDone():
    todo.add( k )

print( tree )

# walk the tree
t = 0
output = ''
working = set()
max_workers = 5

done = False
while todo or working:
  num_workers = len(working)

  # if there are available workers, and if nodes are ready on the todo list,
  #  take them off todo and add them to working
  if num_workers < max_workers:
    for i in sorted(list(todo)):
      if tree[i].isReady:
        working.add( i )
        num_workers += 1
        todo.remove( i )
        if num_workers >= max_workers:
          break

  print( "t=%d, %s %s" % (t, working, output ) )

  # do work on all working nodes
  for cur in list(working):
    tree[cur].doWork()
    if tree[cur].isDone():
      working.remove(cur)
      output +=cur 
      for i in tree[cur].children:
        if tree[i].isReady() and not tree[i].isDone():
          todo.add( i )

  t += 1

print( 'Done!' )
print( output )
print( t )




