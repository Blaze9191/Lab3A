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
<<<<<<< HEAD
def is_prime(n):
    for i in range(2, (n+1)//2):
        if n%i==0:
            return "No"
    return "Yes"
def gcd(a, b):
    while a*b!=0:
        a=a%b
        return gcd(b, a)
    return max(a, b)
