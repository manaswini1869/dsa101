sorted: returns a new sorted list from the list in the given iterable, (sorted(array), options key=None, reverse=True/False)

array.sort() -> permanent change, doesn't return anything, only for lists with no return

lambda arguments: expression
sort dict by value
sorted(dict.items(), key=lambda y:y[1])

Compiled Languages

A compiler translates the entire source code into a machine code (binary executable) before the program runs.

Characteristics:

Full program is converted at once

Produces a standalone binary

Errors are shown at compile-time

Faster execution (after compilation)

Examples:

C, C++, Rust, Go, Swift

Expanded Explanation:
When you run a compiled language, the compiler does parsing → optimization → machine code generation, producing a file like a.out or .exe.
Then the CPU executes that binary directly.

✅ Interpreted Languages

An interpreter executes the program line-by-line (statement-by-statement) at runtime, without converting the entire program to machine code upfront.

Characteristics:

Program is read and executed one piece at a time

No standalone binary

Errors appear during execution

Slower than compiled (because parsing happens every run)

Examples:
Python, Ruby, JavaScript, PHP, Bash

Expanded Explanation:
The interpreter translates each line into intermediate instructions or bytecode and runs it immediately.

Depending on the question, you need to simulate, make sure to add pointers in the direction or the corners you are traversing

Greedy Algorithm: A greedy algorithm is where you make a locally optimal solution/choice at each step to make a global optimal solution at the end

Sliding Window : Arrays, linked lists, linear data
Finding max / min substring;

Bit Manipulation:

binary digit : operands mathematical computations between the digits

AND a&b returns 1 only if both the bits are 1
OR a|b return 1 if either bit is 1
NOT ~a returns the complement of a (1->0, 0->1)
XOR a^b return 0 if both bit are same else 1
left shift a<<n shift a towards left by n digits
right shift a>>n shift a towards right by n digits

DP: works by breaking the problem into sub-problems and storing them.
instead of recalculating the solution again, it can be easily fetched
save time in computational effort
memoization means storing the values to these subproblems in a data structure
is a computer programming technique where an algorithmic problem is first broken down into sub-problems, the results are saved, and then reused to find a solution efficiently

Backtracking : involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end





