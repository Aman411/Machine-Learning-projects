import sys
import re
file_name=sys.argv[1]
sp=file_name.split('.')
d_file=sp[0]+'_'+'copy'+'.'+'txt'
with open (file_name,'r') as file1:
	with open (d_file,'w') as file2:
		file2.write(file1.read())
with open (d_file,'r') as file3:
	rep_space=re.sub(' ','#',file3.read())
	rep_digits=re.sub('[0-9]','?',rep_space)
with open (d_file,'w') as file4:
	file4.write(rep_digits)



