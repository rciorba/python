def binarySearch(l, item):
	first = 0
	last = len(l) - 1
	found = False

	while first <= last and not found:
		print "Searching between ", first, " and ", last
		midpoint = (first + last) // 2
		if l[midpoint] == item:
			found = True
		else:
			if item < l[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1

	return found

print binarySearch([1, 2, 3, 5, 6], 3)