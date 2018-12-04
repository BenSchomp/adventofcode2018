# day 4, part 1
# parse guard sleep times
# find guard most asleep, then which min he slept the most

file = open('day04-input.txt', 'r')

events = dict()
for line in file:
  pieces = line.strip().split( ']' )
  events[pieces[0][1:]] = pieces[1]
file.close()

# handle each event in sorted by date/time order

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

    # since all events are processed sorted by date/time,
    #   starting at event_min, mark every future min the new state
    event_min = int( time.split(':')[1] )
    for i in range(event_min, 60):
      if event.startswith( 'falls' ):
        shifts[date][1][i] = 1
      else: # startswith( 'wakes' )
        shifts[date][1][i] = 0

# now group by guard, combining each min asleep into one totaled array

guard_totals = dict()
for key in sorted(shifts.iterkeys()):
  (guard, shift) = shifts[key]

  if guard not in guard_totals:
    # init entry
    guard_totals[guard] = shift
  else:
    # add each min to total
    for i in range(60):
      guard_totals[guard][i] += shift[i]

max_asleep_mins = -1 # the running max of number of total minutes a guard has slept
max_asleep_guard = None # which guard slept for the above max_asleep_mins
for guard, shift in guard_totals.items():
  max_min = None # the cur guard's max slept minutes
  max_min_value = -1 # which minute is responsible for the above max_min

  # total up all minutes asleep
  total_asleep = 0
  for i in range(60):
    total_asleep += shift[i]

    # is this minute the new max slept minute?
    if shift[i] > max_min_value:
      max_min_value = shift[i]
      max_min = i

  # if this guard is the new max, set everything accordingly
  if total_asleep > max_asleep_mins:
    max_asleep_mins = total_asleep
    max_asleep_guard = guard
    max_asleep_min = max_min
    max_asleep_min_value = max_min_value

# output checksum
print( "output: %d" % (max_asleep_guard * max_asleep_min) )


