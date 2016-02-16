def odd_numbers(low,high):
	if type(low)== int and type(high)== int and high>low:
		num= range(low,high)
		myList=[]
		for i in num:
			if i%2==1:
				myList.append(i)
		    return myList

		else:
			return "Even"

print odd_numbers(1,100)

