#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def gauss(x, *p):
    """
    gaussian function
    """
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

def plotHist(para, p0, bars = 40):
    """
    plot function
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    npoints, barEdges, npatches = ax.hist(para, bins = bars)
    bin_centers = (barEdges[:-1] + barEdges[1:])/2.
    fittedPara, varMatrix = curve_fit(gauss, bin_centers, npoints, p0 = p0, sigma = np.sqrt(npoints))
    ax.plot(bin_centers, gauss(bin_centers, *fittedPara), '-o')
    return fig, np.abs(fittedPara)
