with open ("temp1.txt",'a') as f:
	print("pos",f.tell())
	print(f)
	print(f.closed)
print(f.closed)
print("End")