def func(n):
 x=2*n
 return x%10+x/10


def checksum(l):
 sum=0
 isSecond=0
 for i in range(len(l)-1, -1, -1):
	d=int(l[i])
 if(isSecond==1):
 	d=d*2
 sum+=d/10+d%10
 isSecond = (isSecond+1)%2
 return sum

l="543210******1234".replace('*', '0')
num=123457
#print(checksum(l))


for a in range(10):
 for b in range(10):
  for c in range(10):
   for d in range(10):
    for e in range(10):
     for f in range(10):
      x=list(l)
      if((func(a)+b+func(c)+d+func(e)+f)%10==1):
      	y=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
       	x[6:12]=list(y)
      	if(int(''.join(x))%num==0):
        	print("CTFlearn{" + ''.join(x) + "}")
