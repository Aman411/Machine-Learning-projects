try:
    n = int(input())
except ValueError:
    print("ValueError")
    n = 0

try:
    a = [1,2,3]
    print(a[n])

finally:
	except IndexError:
		print("Something wrong with the code")

print("Finally, n is", n)
print("End")