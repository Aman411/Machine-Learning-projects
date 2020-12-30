import sys
file_name=sys.argv[1:]
try:
    with open(file_name[0],'r') as f:
        content=list(f.read())
        for c in range(len(content)):
            if content[c] == ' ':
                content[c] = '#'
            elif content[c].isnumeric():
                content[c] = '?'
            elif content[c].lower() in 'aeiou':
                content[c] = '0'
        copiedFileName="_copy.".join(file_name[0].split("."))
        with open(copiedFileName, 'w') as f2:
            f2.write("".join(content))
except Exception as err:
    print(err)