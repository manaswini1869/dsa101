# dynamic programming

optimized recursive method.
define some recursive function, called dp which will return the answer to the original problem as if the argument you passed to it were the input
arguments the function takes in are called the state of the problem. in dp the state can be repeated
when we find the answer for a given state, we cache that value. in future we can reuse that value again


### Top down vs bottom up

recursion and memoization - top down approach dp
start at the bottom and work our way up to larger problems - tabulation - bottom up

### Characters

1. asking for an optimal value (max or min) of something or the number of ways to do something
2. Each step you make a decision and this decision effects future results

in greedy local decisions don't affect future decisions or results


state variables : index along the input string, array, or number; constraints given by the problem; boolean

Time Complexity : O(NF) -> N - possible states, F - work done at each state
Space Complexity : O(N) -> we will be storing the states

### Framework top down

1. function or data structure that will compute/contain the answer to the problem for any given state
2. a recurrence relation to transition between states
3. base case







