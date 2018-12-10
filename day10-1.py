import re

sky = {}
with open( 'day10-input.txtx' ) as fIn:
  for line in fIn:
    print( 'line', line.strip() )
    pieces = re.findall(r'[-]?\d+', line)
    startPos = (pieces[0], pieces[1])
    delta = (pieces[2], pieces[3])

    print( startPos, delta )

