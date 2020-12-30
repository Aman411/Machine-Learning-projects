import traceback
try:
    n = int(input("Enter a num: "))
    print("n=", n)
    r = 4//n
    print("r=", r)
except:
	print("Nothing is there")
except ValueError as err: # exception handlers
    print("Invalid value",err)
    traceback.print_tb(err.__traceback__)
except Exception: # exception handlers
    print("Don't give zeroes")
