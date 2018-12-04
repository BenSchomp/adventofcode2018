# day 4, part 1
# parse guard sleep times
# find guard most asleep, then which min he slept the most

file = open('day04-input.txtx', 'r')

events = dict()
for line in file:
  pieces = line.strip().split( ']' )
  events[pieces[0][1:]] = pieces[1]
file.close()

shifts = dict()
for key in sorted(events.iterkeys()):
  pieces = key.split(' ')
  date = pieces[0]
  time = pieces[1]

  event = events[key].strip()
  if event.startswith( 'Guard' ):
    pieces = event.split('#')
    guard = pieces[1].split(' ')[0]
    # don't know the shift date yet ...

  else:
    # now we know the shift date
    if date not in shifts:
      shifts[date] = (guard, [0] * 60)

    event_min = int( time.split(':')[1] )
    for i in range(event_min, 60):
      if event.startswith( 'falls' ):
        shifts[date][1][i] = 1
      else: # startswith( 'wakes' )
        shifts[date][1][i] = 0


for key in sorted(shifts.iterkeys()):
  print "%s: %s" % (key, shifts[key])

