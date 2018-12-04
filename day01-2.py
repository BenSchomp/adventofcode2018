# day 1, part 2
# store a running total of +/- values
# keep parsing the file until a repeated total is seen

value = 0     # the running total
history = {0} # history of seen totals

while 1:
  file = open('day01-input.txt', 'r')
  for line in file:
    diff = int(line)
    value += diff

    if value in history:
      print( "repeated value: %d" % value )
      exit()

    history.add( value )

  file.close()

