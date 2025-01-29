import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def combination_func(score, combination, res):
  if score == 0:
    res.append(list(combination))
    return
  for i in range(1, 4):
    if score - i >= 0:
      combination.append(i)
      combination_func(score-i, combination, res)
      combination.pop()

def gameScoring(score):
  # Write your code here
  res = []
  combination_func(score, [], res)


  return res












# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = True
  if len(expected) == len(output):
    for score in expected:
      result = result & (score in output)
    for score in output:
      result = result & (score in expected)
  else:
    result = False
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    print(expected)
    print(' Your output: ', end='')
    print(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = 4
  expected_1 = [
  [1, 1, 1, 1],
  [1, 1, 2],
  [1, 2, 1],
  [1, 3],
  [2, 1, 1],
  [2, 2],
  [3, 1]
   ]
  output_1 = gameScoring(test_1)
  check(expected_1, output_1)

  test_2 = 5
  expected_2 = [
  [1, 1, 1, 1, 1],
  [1, 1, 1, 2],
  [1, 1, 2, 1],
  [1, 1, 3],
  [1, 2, 1, 1],
  [1, 2, 2],
  [1, 3, 1],
  [2, 1, 1, 1],
  [2, 1, 2],
  [2, 2, 1],
  [2, 3],
  [3, 1, 1],
  [3, 2],
    ]
  output_2 = gameScoring(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
