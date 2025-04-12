import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getSmallestClockAngle(timeString, unit):
  # Write your code here
  hours, minute = map(int, timeString.split(":"))

  hours = hours % 12

  minute_angle = minute * 6

  hour_angle = (hours * 30) + (minute*0.5)

  angle = abs(hour_angle - minute_angle)

  smallest_angle = min(angle, 360 - angle)

  if unit == "radians":
    smallest_angle = smallest_angle * math.pi / 180
    smallest_angle = round(smallest_angle, 4)

  return smallest_angle


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  output_1 = getSmallestClockAngle('03:00', 'radians')
  check(1.5708, output_1)

  output_2 = getSmallestClockAngle('09:30', 'degrees')
  check(105, output_2)

  # Add your own test cases here
