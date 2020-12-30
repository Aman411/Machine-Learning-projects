import sys
file_name=sys.argv[1]
sp=file_name.split('.')
new_file=sp[0]+'_'+'copy'+'_'+'copy'
with open (file_name,'r') as file1:
	with open (new_file,'w') as file2:
		file2.write(file1.read())
with open (new_file,'r') as file3:
	