# /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pdb
import sys
from random import randint, uniform, gauss
## define the function
def MaxLikelihood(m, b, Pb, Vb, Yb):
    """
    Calculate maxium likelihood value
    input paramter:
      m: gradient
      b: intercept
      Pb, Vb, Yb: bayesian analysis parameters
    """
    
    global x, y, dy
    y_mod = m * x + b
    c = 1e48 # a constant value to normalize
    if (Pb > 1.0) or (Pb < 0.0) or (Vb < 0) or (Yb < 0): #exclude nonphysical value
        return 0
    else:
        return c * np.prod((1 - Pb)/np.sqrt(2 * np.pi * dy**2) * np.exp(-(y - y_mod)**2/(2 * dy**2)) 
            + Pb/np.sqrt(2 * np.pi * (dy**2 + Vb)) * np.exp(-(y - Yb)**2/(2 * dy**2)))
        
    
def MCMC(m0, b0, Pb0, Vb0, Yb0, step = 1.0, n_step = 1e5):
    step_length = np.array([0.01, 10.0, 0.1, 400, 70]) * step # set the basic step length
                                                      # ~1% for m, and b
                                                      # ~10% for p, v, y
    ML0 = MaxLikelihood(m0, b0, Pb0, Vb0, Yb0)
    m1, b1, Pb1, Vb1, Yb1, ML1 = m0, b0, Pb0, Vb0, Yb0, ML0 # 0 represent old, 1 represent new 
    m_list = []
    b_list = []
    Pb_list = []
    Vb_list = []
    Yb_list = []
    ML_list = []
    for para_list, para in zip([m_list, b_list, Pb_list, Vb_list, Yb_list, ML_list], [m1, b1, Pb1, Vb1, Yb1, ML1]):
        para_list.append(para)
    
    for i in range(n_step):
        change_id = randint(0, 4) # randomly choose a parameter to change
        if change_id == 0:
           m1 = m0 + np.random.normal(0, step_length[0])
        elif change_id == 1:
           b1 = b0 + np.random.normal(0, step_length[1])
        elif change_id == 2:
           Pb1 = Pb0 + np.random.normal(0, step_length[2])
        elif change_id == 3:
           Vb1 =  Vb0 + np.random.normal(0, step_length[3])
        elif change_id == 4:
           Yb1 =  Yb0 + np.random.normal(0, step_length[4])
        ML1 = MaxLikelihood(m1, b1, Pb1, Vb1, Yb1)
        #pdb.set_trace()
        if ML1 > ML0: #accept
            for para_list, para in zip([m_list, b_list, Pb_list, Vb_list, Yb_list, ML_list], [m1, b1, Pb1, Vb1, Yb1, ML1]):
                para_list.append(para)
            m0, b0, Pb0, Vb0, Yb0 = m1, b1, Pb1, Vb1, Yb1
            ML0 = ML1
        elif ((ML1 <= ML0) and (ML1 != 0)):
            criterion = uniform(0, 1)
            if ML1/ML0 > criterion: #accept
                for para_list, para in zip([m_list, b_list, Pb_list, Vb_list, Yb_list, ML_list], [m1, b1, Pb1, Vb1, Yb1, ML1]):
                    para_list.append(para)
                m0, b0, Pb0, Vb0, Yb0 = m1, b1, Pb1, Vb1, Yb1
                ML0 = ML1
        else:
            pass
        #print '{0} step finished, {1} points accepted'.format(i, len(ml_list))
            
    return m_list, b_list, Pb_list, Vb_list, Yb_list, ML_list

if __name__ == '__main__':
    m0, b0, Pb0, Vb0, Yb0, step, n_step = map(float, sys.argv[1:])
    n_step = int(n_step)
    print n_step
    (data_id, x, y, dy, dx, rho_xy) = np.loadtxt('sample_data.txt', comments = '%', unpack = True)
    m_list, b_list, Pb_list, Vb_list, Yb_list, ML_list = MCMC(m0, b0, Pb0, Vb0, Yb0, step, n_step = n_step)
       
