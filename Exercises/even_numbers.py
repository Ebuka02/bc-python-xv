def even_numbers(low, high):

	if type(low) == int and type(high) == int and low < high:
		num = range(low,high)
		myList = []
		for i in num:
			if i%2 == 0:
				myList.append(i)
		return myList

	else:
		return "odd"

print (even_numbers(1, 100))

