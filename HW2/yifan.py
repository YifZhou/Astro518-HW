from pylab import *
import time
import numpy as np

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
dy=array(alldata[:,3].T)[0]  #column vector with sigy values in it



PVB_mesh = [(pi, vj, yk) for pi in P for vj in V for yk in Y]
ML_mesh = []

def ml_i(p):
    global y
    global dy
    global y_mod
    pb, vb, yb = p
    return np.prod((1 - pb)/np.sqrt(2 * np.pi * dy**2) * np.exp(-(y - y_mod)**2 / (2 * dy**2) + pb / np.sqrt(2 * np.pi * (dy**2 + vb)) * np.exp(-(y - y_mod)**2 / (2 * dy**2))))

start = time.time()
for (m, b) in [(mi, bj) for mi in mm for bj in bb]:
    y_mod = m * x + b
    ML_mesh.append(sum([ml_i(para) for (para) in PVB_mesh]))
    





    

print 'total time spend:', time.time() - start