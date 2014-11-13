
# coding: utf-8

# # Astro518 Homework 3
# ## Markov Chain Monte Carlo

# In[15]:

from random import randint, random


# In[2]:

(data_id, x, y, dy, dx, rho_xy) = np.loadtxt('sample_data.txt', comments = '%', unpack = True) ## readin data


# In[ ]:

get_ipython().run_cell_magic(u'time', u'', u'## define the function\ndef MaxLikelihood(p): \n    """\n    Calculate maxium likelihood value\n    input paramter:\n      m: gradient\n      b: intercept\n      Pb, Vb, Yb: bayesian analysis parameters\n    """\n    \n    global x, y, dy\n    m, b, Pb, Vb, Yb = p\n    y_mod = m * x + b\n    c = 10.**48 # a constant value to normalize\n    max_list = np.array([4.0, 150., 1., 4000., 700.]) # maximum boundary \n    min_list = np.array([0., -150., 0., 0., 0.]) #minimum boundary\n    if (p > max_list).any() or (p < min_list).any(): #exclude nonphysical value\n        return 0\n    else:\n        return c * np.prod((1 - Pb)/np.sqrt(2 * np.pi * dy**2) * np.exp(-(y - y_mod)**2/(2 * dy**2)) \n            + Pb/np.sqrt(2 * np.pi * (dy**2 + Vb)) * np.exp(-(y - Yb)**2/(2 * dy**2)))\n    \ndef MCMC(p0, step, n_step = 1e5):\n    base_length = np.array([0.004, 0.3, 0.01, 40, 7]) # set the basic step length\n                                                      # 0.1% for m, and b\n                                                      # 1% for p, v, y\n    ml0 = MaxLikelihood(p0)\n    n = 0\n    p_new = p0\n    para_list = []\n    ml_list = []\n    para_list.append(p0)\n    ml_list.append(ml0)\n    while(n < n_step):\n        change_id = randint(0, 4) # randomly choose a parameter to change\n        p_new[change_id] = p0[change_id] + step * base_length[change_id]\n        ml = MaxLikelihood(p_new)\n        if ml >= ml0: #accept\n            p0 = p_new\n            ml0 = ml\n            para_list.append(p_new)\n            ml_list.append(ml)\n            n+=1\n        elif ml < ml0:\n            criterion = random()\n            if ml/ml0 >= criterion: #accept\n                p0 = p_new\n                ml0 = ml\n                para_list.append(p_new)\n                ml_list.append(ml)\n                n+=1\n        print \'{0} step finished, mostlikelihood = {1}\'.format(n, ml)\n            \n    return para_list, ml_list\n\npara1, ml_list1 = MCMC(np.array([2, 0, 0.5, 200, 300]), 1.0)')


# In[ ]:



