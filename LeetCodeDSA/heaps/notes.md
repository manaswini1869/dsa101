implementation of priority queue

supports add, remove, find the minimum element in O(1)

A heap can also find the max elements instead of the min elements, if a heap is configured to find/remove the min element -> min heap

we can implement heap using a binary tree -> the binary tree must be a complete tree
children indices = 2i+1, 2i+2
parent.val <= child.val

## Heap operations
heapq.heappush - O(log n) time
heapq.heappop - O(log n)
heapify - O(n) takes an array of integers and converts it to a min heap structure

if a problem involves finding median - good to think about implementing it with two heaps

finding the min element = O(1)

The heap property is that children have values larger than their parents. This doesn't imply that the maximum element will be the last element in the heap


## Top K

sorting takes O(n.logk)
max_heap, iterate over the input while pushing every element on the heap and pop once the size of the heap exceeds k as the heap size is bound by k

