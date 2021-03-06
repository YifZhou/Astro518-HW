## Question 3a: Marginalization

from pylab import *
import math
import numpy
import matplotlib
import time
from mpl_toolkits.mplot3d import Axes3D

def ML(x,y,s,m,b,pb,vb,yb):
   #print(m,b,pb,vb,yb)
   if(pb < 0. or pb > 1.):      return 0.
   if(vb<0. or yb<0.):      return 0.
   p1=divide((1.-pb),(sqrt(multiply(2.*pi,square(s)))))
   p2=exp(divide(-square(subtract(subtract(y,multiply(m,x)),b)),(multiply(2.,square(s)))))
   p3=divide(pb,sqrt(multiply(2.*pi,add(square(s),vb))))
   p4=exp(divide(-(square(subtract(y,yb))),multiply(2.,square(s))))
   n=add(multiply(p1,p2),multiply(p3,p4))
   #print(max(p1),max(p2),max(p3),max(p4),max(n))
   #print(min(p1),min(p2),min(p3),min(p4),min(n))
   #print(prod(n[:6]))
   return prod(n)


# Timing for my personal edification
start=time.time()

# Load data
alldata = matrix(loadtxt('sample_data.txt', skiprows=3))
xx=array(alldata[:,1].T)[0]  #column vector with x values in it
yy=array(alldata[:,2].T)[0]  #column vector with y values in it
ss=array(alldata[:,3].T)[0]  #column vector with sigy values in it

msave=[]
bsave=[]
pbsave=[]
vbsave=[]
ybsave=[]

mm=2.
bb=20.
pbb=.5
vbb=100.
ybb=100.
sig=.5
oldml=ML(xx,yy,ss,mm,bb,pbb,vbb,ybb)

#ion()
points=0.
vhigh=400.#2.*mean(yy)
yhigh=70.#(max(yy)-min(yy))**2.
phigh=.1
num=1000000

d=25

#i=0.
for i in range(num):
#while (points < num):
  #print(i)
  mnew=mm+numpy.random.normal(0.,.02)
  bnew=bb+numpy.random.normal(0.,1.)
  #pbnew=pbb+numpy.random.normal(0,phigh)
  #vbnew=vbb+numpy.random.normal(0,vhigh)
  #ybnew=ybb+numpy.random.normal(0,yhigh)
  #mnew=mm+numpy.random.uniform(-0,.02)
  #bnew=bb+numpy.random.uniform(-0.,1.)
  pbnew=pbb+numpy.random.uniform(-phigh,phigh)
  vbnew=vbb+numpy.random.uniform(-vhigh,vhigh)
  ybnew=ybb+numpy.random.uniform(-yhigh,yhigh)

  thisml=ML(xx,yy,ss,mnew,bnew,pbnew,vbnew,ybnew)
  R=numpy.random.random()
  if( (thisml!=0. and R<(thisml/oldml))):
    #(thisml>oldml) or 
    mm=mnew
    bb=bnew
    pbb=pbnew
    vbb=vbnew
    ybb=ybnew

    msave+=[mm]
    bsave+=[bb]
    pbsave+=[pbb]
    vbsave+=[vbb]
    ybsave+=[ybb]
    oldml=thisml
    points+=1.

# emm=loadtxt('m.dat',unpack=True)
# bbe=loadtxt('b.dat',unpack=True)
# emmell=loadtxt('matrix.dat',unpack=True)
# emel=reshape(emmell,(len(emm),len(bbe)))
# B, M = np.meshgrid(bbe, emm)
# contour(B,M,emel)
# scatter(bsave,msave)
# scatter(bsave[:d],msave[:d],c='r')
# title('rate: '+str(round(points/(num+1.),3)))
# axis([-50., 100., 1.5, 3.0])
# xlabel('b')
# ylabel('m')
# #show(block=False)
# savefig('scatter.jpeg')

# figure()
# nm, binm, patchesm = hist(array(msave[d:]),bins=100)
# xlabel('m')
# savefig('mhist.jpeg')
# figure()
# nb, binb, patchesb=hist(array(bsave[d:]),bins=100)
# print(binm[where(nm == nm.max())][0],binb[where(nb == nb.max())][0])
# xlabel('b')
# savefig('bhist.jpeg')

# figure()
# hist(array(ybsave[d:]),bins=100)
# xlabel('Yb')
# savefig('yhist.jpeg')
# figure()
# hist(array(vbsave[d:]),bins=100)
# xlabel('Vb')
# savefig('vhist.jpeg')
# figure()
# hist(array(pbsave[d:]),bins=100)
# xlabel('Pb')
# savefig('phist.jpeg')

# figure()
# hist2d(bsave[d:],msave[d:], bins=(50,100))
# xlabel('b')
# ylabel('m')
# savefig('twodhist.jpeg')

# show()
