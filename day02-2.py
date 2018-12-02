file = open('day02-input.txt', 'r')

ids = []
for line in file:
  ids.append( line.strip() )

print( ids )

n = len(ids)
for i in range( 0, n ):
  for j in range( i+1, n ):

    a = ids[i]
    b = ids[j]
    diffs = 0
    for x in range( 0, len(a) ):
      if a[x] != b[x]:
        diffs += 1

    #print( diffs, a, b )
    if diffs == 1:
      result = ''
      for x in range( 0, len(a) ):
        if a[x] == b[x]:
          result += str( a[x] )

      print( result )
      exit()

file.close()
