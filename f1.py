with open("temp.txt",'r') as f:
	while True:
		s=f.read(5)
		if len(s)==0:
			break
		print(s,f.tell())
	print()
	f.seek(5)
	print("reread:",f.read())
print("End")
