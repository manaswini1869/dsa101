- Linear will at some point surpass constant O(n) > O(1)
- If we need a two-dimensional array of size nxn, this will require 0 ( n * ) space.
- If your algorithm is in the form "do this, then, when you're all done, do that" then you add the runtimes.
- If your algorithm is in the form "do this for each time you do that" then you multiply the runtimes.
- cost amortized : sometimes bad occurrence will happen, but when it passes, it will rarely happen again
- log N runtimes: What is k in the expression 2k = N? This is exactly what l o g expresses.
        T - 16 -> log16 = 4
        logN = k -> 2* = N
- When you see a problem where the number of elements in the problem space gets halved each time, that will likely be a 0( l o g N) runtime.
- runtime for recursive algorithms: Try to remember this pattern. When you have a recursive function that makes multiple calls, the runtime will often (but not always) took likeO(branchest ! e p t , 1), where branches is the number of times each recursive call branches. In this case, this gives us 0( 2").
- This technique, called memoization, is a very common one to optimize exponential time recursive algorithms.
-