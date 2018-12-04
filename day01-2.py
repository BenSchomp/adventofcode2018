file = open('day01-input.txt', 'r')

value = 0
for line in file:
  diff = int(line)
  value += diff

file.close()
print( "value:", value )
