a = int(input("Input the length of side a: "))
b = int(input("Input the length of side b: "))
c = int(input("Input the length of side c: "))

result = (a + b >= c) and (a + c >= b) and (b + c >= a)

if result:
	print("This is a Triangle")
else:
	print("This is not a Triangle")
