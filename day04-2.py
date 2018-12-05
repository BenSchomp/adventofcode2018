# day 4, part 2
# parse guard sleep times
# find which minute is most slept through

file = open('day04-input.txt', 'r')

events = dict()
for line in file:
  pieces = line.strip().split( ']' )
  events[pieces[0][1:]] = pieces[1]
file.close()

# handle each event in sorted-by-date/time order

shifts = dict()
for key in sorted(events.iterkeys()):
  pieces = key.split(' ')
  date = pieces[0]
  time = pieces[1]

  event = events[key].strip()
  if event.startswith( 'Guard' ):
    pieces = event.split('#')
    guard = int(pieces[1].split(' ')[0])
    # don't know the shift date yet ...

  else:
    # now we know the shift date
    if date not in shifts:
      shifts[date] = (guard, [0] * 60)

    # since all events are processed sorted-by-date/time,
    #   starting at event_minute, update every future minute with the new state
    event_minute = int( time.split(':')[1] )
    for i in range(event_minute, 60):
      if event.startswith( 'falls' ):
        shifts[date][1][i] = 1
      else: # startswith( 'wakes' )
        shifts[date][1][i] = 0

# now group by guard, combining each minute asleep into one totaled array

guard_totals = dict()
for key in sorted(shifts.iterkeys()):
  (guard, shift) = shifts[key]

  if guard not in guard_totals:
    # init entry
    guard_totals[guard] = shift
  else:
    # add each minute to total
    for i in range(60):
      guard_totals[guard][i] += shift[i]

# now find the minute with the most slept minutes across all guards

max_minute = None
max_minute_value = -1
max_guard = None
for guard, shift in guard_totals.items():
  for i in range(60):
    if shift[i] > max_minute_value:
      max_minute_value = shift[i]
      max_minute = i
      max_guard = guard

print( "output: %d" % (max_guard * max_minute) )


