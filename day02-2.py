# day 2, part 2
# for each input, compare against each other input
# when two inputs that differ by exactly one character,
#  the answer has been found

file = open('day02-input.txt', 'r')

ids = []
for line in file:
  ids.append( line.strip() )

n = len(ids)
for i in range( 0, n ):
  for j in range( i+1, n ):

    a = ids[i]
    b = ids[j]
    diffs = 0
    for x in range( 0, len(a) ):
      if a[x] != b[x]:
        diffs += 1

    if diffs == 1:
      result = ''
      for x in range( 0, len(a) ):
        if a[x] == b[x]:
          result += str( a[x] )

      # the final output is the characters that were in both a and b
      print( "output: %s" % result )
      exit()

file.close()
