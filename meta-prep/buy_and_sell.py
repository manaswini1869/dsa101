import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def bestDaysToBuyAndSell(arr):
  # Write your code here
  res = []
  minBuyDay = 0
  minBuy = arr[0]
  maxProfit = 0
  for i in range(1, len(arr)):
    profit = arr[i] - minBuy
    if profit > maxProfit:
      maxProfit = profit
      res = [minBuyDay, i]
    if arr[i] < minBuy:
      minBuy = arr[i]
      minBuyDay = i
  return res









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

def printMultipleIntegerList(array):
  for j in range(len(array)):
    if j != 0:
      print(' or ', end='')
    size = len(array[j])
    print('[', end='')
    for i in range(size):
      if i != 0:
        print(', ', end='')
      print(array[j][i], end='')
    print(']', end='')


test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if output in expected:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printMultipleIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [100,180,260,310,40,535,695]
  expected_1 = [[4, 6]]
  output_1 = bestDaysToBuyAndSell(test_1)
  check(expected_1, output_1)

  test_2 = [4,2,2,2,4]
  expected_2 = [[1, 4],[2, 4],[3, 4]]
  output_2 = bestDaysToBuyAndSell(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
