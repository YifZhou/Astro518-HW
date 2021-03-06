from pylab import *
import time

mm=arange(1.,3.,0.03)
bb=arange(0,250,3.)

# Create P,Y,V
P=arange(0.,1.1,0.1)
V=arange(0.,4001.,400.)
Y=arange(0.,701.,70.)

ML=zeros((len(mm),len(bb)))

data = matrix(loadtxt('data.dat', skiprows=3))
alldata=(data[:,:])
x=array(alldata[:,1].T)[0]  #column vector with x values in it
y=array(alldata[:,2].T)[0]  #column vector with y values in it
s=array(alldata[:,3].T)[0]  #column vector with sigy values in it
i=0
start = time.time()
for m in mm:

 j=0
 for b in bb:
   summy=0.
   for pb in P:
     for vb in V:
       for yb in Y:
         p1=divide((1.-pb),(sqrt(multiply(2.*pi,square(s)))))
         p2=exp(divide(-square(subtract(subtract(y,multiply(m,x)),b)),(multiply(2.,square(s)))))
         p3=divide(pb,sqrt(multiply(2.*pi,add(square(s),vb))))
         p4=exp(divide(-(square(subtract(y,yb))),multiply(2.,square(s))))
         n=add(multiply(p1,p2),multiply(p3,p4))
         summy+=prod(n)
   ML[i,j]=summy
   j+=1
 i+=1

print 'total time: ', time.time() - start