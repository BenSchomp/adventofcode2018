file = open('day02-input.txt', 'r')

twos = 0
threes = 0
for line in file:
  d = dict()
  for i in line.strip():
    if i in d:
      d[i] += 1
    else:
      d[i] = 1

  found2 = False
  found3 = False
  for key, value in d.items():
    if value == 2:
      found2 = True
    elif value == 3:
      found3 = True

  if found2:
    twos += 1
  if found3:
    threes += 1

print( "checksum: (%d x %d) = %d" % (twos, threes, twos * threes) )
file.close()
