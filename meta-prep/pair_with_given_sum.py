import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def countPairs(arr, k):
  # Write your code here
  res = []
  for i,n in enumerate(arr):
    diff = k - n
    if diff in arr[i+1:]:
      res.append([n, diff])
  print(res)
  return len(res)












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
  output_1 = countPairs([1, 2, 3, 4, 5, 6, 7], 8)
  check(3, output_1)

  output_2 = countPairs([1, 2, 3, 4, 5, 6, 7], 98)
  check(0, output_2)

  # Add your own test cases here
