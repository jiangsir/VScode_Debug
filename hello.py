n = int(input())
a = 0
b = 1
for i in range(n):
	b = a + b
	a = b - a
	print(b)
