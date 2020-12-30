import sys
import re
pattern = '[0-9]'
file_name=sys.argv[1]
sp=file_name.split('.')
d_file=sp[0]+'_'+'copy'+'.'+'txt'
print(d_file)
with open (file_name,'r') as file1:
	with open (d_file,'w') as file2:
		file2.write(file1.read())
with open (d_file,'r') as file3:
	rep_spaces=re.sub(' ','#',file3.read())
	rep_digits=re.sub(pattern,'?',rep_spaces)
with open (d_file,'w') as file4:
	file4.write(rep_digits)



#with open (d_file,'r+') as file1:
	#content=list(file1.read())
	#for i in range(len(content)):
	#file1.write(re.sub(' ','#',file1))
			
				