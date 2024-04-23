import sys
self_file=sys.argv[0]
#print(self_file)
if len(sys.argv)==5:
	self_file=sys.argv[1]
with open (self_file,'r') as f:
	fol=f.read()
	print(fol)
