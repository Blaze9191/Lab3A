def fact(n):
	m=1
	for i in range(1, n+1):
		m*=i
	return m
def isfive(n):
	while n%5==0:
		n=n//5
	else:
		if n==1:
			return True
		else:
			return False
def gcd(a, b):
    while a*b!=0:
        a=a%b
        return gcd(b, a)
    return max(a, b)
