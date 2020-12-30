import sys
file_name=sys.argv[0]
if len(sys.argv)==2:
	print(sys.argv[1])


with open (file_name,'r') as file:
	content=file.read()
	print(content)

