source = open('/Users/Matthew/python/kindleClippingsToList/FrClippings.txt','r')

destination = open('/Users/Matthew/python/kindleClippingsToList/destination.txt','r+')

myArray = []

for line in source:
	myArray.append(line)

destination.read()
print destination.read()
for line in destination:
	print line

newlist = []
for w in myArray:
	if w[0]!='=' and w[0]!='-':
		print w[:3]
		if w[:3]!='Fra':
			newlist.append(w)

list(enumerate(myArray))

print newlist

for e in newlist:
	destination.write(e+'\n')