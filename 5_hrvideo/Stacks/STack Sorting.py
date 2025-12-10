def stackSorting(stack):
	temp = []
	while stack:
		curr = stack.pop()
		while temp and temp[-1] < curr:
			t = temp.pop()
			stack.append(t)
		temp.append(curr)
	print(temp)

stack = input().split()
stackSorting(stack)