# Add any extra import statements you may need here


# Add any helper functions you may need here


def getTrappedRainWater(arr):
  # Write your code here
  trap = 0
  left_max, right_max = 0, 0
  left, right = 0, len(arr)-1

  while left < right:
    if arr[left] < arr[right]:
      if arr[left] > left_max:
        left_max = arr[left]
      else:
        trap += abs(arr[left] - left_max)
      left += 1
    else:
      if arr[right] > right_max:
        right_max = arr[right]
      else:
        trap += abs(right_max - arr[right])
      right -= 1
  return trap











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
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  outputOne = getTrappedRainWater([7,4,0,9]);
  check(10, outputOne);
  outputTwo = getTrappedRainWater([6,9,9]);
  check(0, outputTwo)
  # Add your own test cases here
