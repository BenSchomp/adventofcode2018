# day 2, part 1
# for each input, count the number of repeated characters
# keep a running count of how many inputs had exactly
#  two repeated characters, and how many had exactly
#  three repeated characters
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

  found_two = False
  found_three = False
  for key, value in d.items():
    if value == 2:
      found_two = True
    elif value == 3:
      found_three = True

  if found_two:
    twos += 1
  if found_three:
    threes += 1

file.close()

# final output is the product of twos and threex
print( "checksum: (%d x %d) = %d" % (twos, threes, twos * threes) )

