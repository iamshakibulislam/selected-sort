def selection_sort(items):
	sortedlist=[]
	myitems=items
	is_sorted = False
	minval = 0

	while not is_sorted :

		for x in myitems :
			if myitems[minval] > x :
				minval = myitems.index(x)
		sortedlist.append(myitems[minval])
		myitems.remove(myitems[minval])
		minval=0

		if len(myitems)==0:
			return sortedlist
			break



listi=[6,0,9,1,23,4,8,7,7,11,66,44,98]

print(selection_sort(listi))

