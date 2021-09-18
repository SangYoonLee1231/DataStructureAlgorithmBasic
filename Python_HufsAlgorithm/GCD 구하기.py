# 나머지 연산을 이용하여 구현
def gcd_mod(a, b) :
	while (b != 0):
		temp = a % b
		a = b
		b = temp
	return a

# 뺄셈을 이용하여 구현
def gcd_sub(a, b):
	temp = -1
	while (temp != 0) :
		if a > b :
			temp = a - b
			a = b
			b = temp
		else:
			temp = b - a
			b = temp
	return a

a, b = map(int, input().split())
print(gcd_mod(a, b))
print(gcd_sub(a, b))
