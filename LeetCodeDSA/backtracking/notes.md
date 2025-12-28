# Backtracking
Generate all possibilities and then check each of them for a solution

efficiently run through all possibilities in a problem. Uses an optimization technique which involves abandoning a path once we know the path is not the correct answer or the path will not lead to the answer
abandoning = pruning

problem = find all of something
exponential time complexities

// let curr represent the thing you are building
// it could be an array or a combination of variables

function backtrack(curr) {
    if (base case) {
        Increment or add to answer
        return
    }

    for (iterate over input) {
        Modify curr
        backtrack(curr)
        Undo whatever modification was done to curr
    }
}

time complexity is very hard to derive
it is

O(k⋅n! // (n−k)!⋅k!)
n = length of the matrix of the given limit
k = given limit




