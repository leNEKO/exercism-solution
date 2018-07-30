from math import gcd

def primitive_triplets(number_in_triplet):
	triplets=[]
	
	if number_in_triplet%4!=0:
		raise ValueError('ValueError')

	a=1
	b=number_in_triplet
	c=b+1
	while a<b:
			if a**2+b**2<c**2:
				a+=1
			elif a**2+b**2>c**2:
				c+=1
			else:
				if gcd(a,b)==1:
					if gcd(b,c)==1:
						if gcd(a,c)==1:
							triplets.append((a,b,c))
				a+=1

	a=number_in_triplet
	b=a+1
	c=a+2
	while True:
			if a**2+b**2<c**2:
				if b<c-1:
					b+=1
				elif c**2-b**2>2*a+1:
					break
				
			elif a**2+b**2>c**2:
				c+=1
			else:
				if gcd(a,b)==1:
					if gcd(b,c)==1:
						if gcd(a,c)==1:
							triplets.append((a,b,c))
				b+=1

	return set(triplets)

def triplets_in_range(range_start, range_end):
	
	triplets=[]
	for a in range(range_start,range_end-1):
		b=a+1
		c=a+2
		while a<=range_end and b<=range_end and c<=range_end:
			if a**2+b**2<c**2:
				if b<range_end-1:
					b+=1
				elif c**2-b**2>2*a+1:
					break
			elif a**2+b**2>c**2:
				c+=1
			else:
				triplets.append((a,b,c))
				b+=1
				c+=1
				

	return set(triplets)


def is_triplet(triplet):
	ls=list(triplet)
	ls.sort()
	return ls[0]**2+ls[1]**2==ls[2]**2


