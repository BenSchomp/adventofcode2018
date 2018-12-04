# day 1, part 1
# store a running total of +/- values

file = open('day01-input.txt', 'r')

value = 0
for line in file:
  diff = int(line)
  value += diff

file.close()
print( "final value: %d" % value )
