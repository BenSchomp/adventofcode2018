
value = 0
history = {0}

while 1:
  file = open('day01-input.txt', 'r')
  for line in file:
    diff = int(line)
    value += diff

    if value in history:
      print( "repeated value:", value )
      exit()

    history.add( value )

  file.close()

print( "value:", value )
