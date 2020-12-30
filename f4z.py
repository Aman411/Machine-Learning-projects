import sys
file_name=sys.argv[1]
s=file_name.split('.')
new_file=s[0]+'_'+'copy'+'.'+'txt'
with open (file_name,'r') as file1:
	with open (new_file,'w') as file2:
		file2.write(file1.read())