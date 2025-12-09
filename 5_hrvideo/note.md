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