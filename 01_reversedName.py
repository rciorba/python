import sys

def reversedNameFirstVariant():
	#simple
	reversedName = ""
	print "Your name"
	name = raw_input();
	for i in reversed(range(len(name))):
		reversedName = reversedName + name[i].upper();
	print "Reversed and uppercased: " + reversedName
		
def reversedNameSecondVariant():
	#slicing
	print "Your name"
	name = sys.stdin.readline();
	print "Reversed and uppercased: " + name.upper()[::-1]
	
def reversedNameThirdVariant():
    #overdoing it
	print "".join([x for x in reversed(raw_input("Name "))]).upper()
	

reversedNameThirdVariant();