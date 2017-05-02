#1.Finds the gcd of two numbers using the Euclidean algorithm. 
#Order in which numbers are passed doesn't matter.
def gcd(a,b):

	if b < a:
		temp = a
		a=b
		b=temp
	r =b % a
	while(r!=0):
		b=a
		a=r
		r=b % a
	return a

#print gcd(462,1071)
#print gcd(1071,462)
#print "------------------------------------------------------------"
	
#2.Returns the multiplicative inverse of a mod b.
# a and b must be positive and relatively prime i.e. gcd(a,b)=1.
def modInv(a,b):
	
	#assigning initial values
	r = [a,b]
	s = [1,0]
	t = [0,1]
	#continue finding gcd until remainder becomes 0
	i = 0
	q = 0
	while(r[1]!=0):
		q = r[0]//r[1]
		s[1],t[1],r[1],s[0],t[0],r[0] = (s[0] -q*s[1]), (t[0]-q*t[1]), (r[0]-q*r[1]),s[1],t[1],r[1] 
	return s[0]%b

#print modInv(1073,462)
#print "---------------------------------------------------------------"

#3.Computes and returns the value of x^(y) mod n.
# x and y must be positive
#calculating base exponentiation first
def baseExp(k, b):
	q = k
	a = []
	while(q != 0):
		a.append(q % b)
		q = q // b
	return a

# comment and redefine
def modExp(b, k, m):
	a = baseExp(k, b)
	exp = 1
	p = b % m
	for i in range(0, len(a)):
		if (a[i] == 1):
			exp = (exp * p) % m
		else:
			exp = (exp * p**a[i]) % m
		p = (p**b) % m
	return exp

#print (modExp(23,20,29))
#print "-------------------------------------------------------------"

#4.Returns the public key(n,e) and private key d by computing n, phi,e and d.
#Arguments p and q must be prime. 
def generateRSAKeys(p,q):
	n = p*q
	phi = (p-1)*(q-1)
	#finding e starting with 3 and incrementing by 2, as even values are not prime, until we 
	#find an e relatively prime to phi
	e = 3
	while gcd(e,phi)!=1:
		e=e+2
	d = modInv(e,phi)#calling modular inversion function
	return [[n,e],[d]]

#print generateRSAKeys(7,11)
#print "----------------------------------------------------------------"


#RSA key generation, encryption and decryption
p = int(input("Enter a prime number: "))
q = int(input("Enter another prime number: "))
M = int(input("Enter an integer: "))
#making public and private keys
key = generateRSAKeys(p,q)
e = key[0][0]
n = key[0][1]
d = key[1][0]
print ("Public key and private key:" + str(key))
#encrpting M using public
C = modExp(M,e,n)
print ("Encrypted message: " + str(C))
#decrypting C using private key
R = modExp(C,d,n)
print ("Decrypted message: " + str(R))
