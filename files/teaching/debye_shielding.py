#!/usr/bin/env python3
import numpy as np
from scipy.constants import k as kB, epsilon_0, e
import matplotlib.pyplot as plt
import matplotlib as mp
import argparse
from langmuir import *

def calc_unscreened_potential(r, qT):
   return qT * e / 4 / np.pi / epsilon_0 / r
def calc_e_potential(r, lam_De, qT):
    return calc_unscreened_potential(r, qT) * np.exp(-r / lam_De)


parser = argparse.ArgumentParser(description='Deep Neural Network for Plasma Radiation (deepRadiation)')
parser.add_argument('-t','--Te', default=1.e8, type=float, help='Electron temperature in eV')
parser.add_argument('-d','--den', default=1.e26, type=float, help='Electron density in (cm-3)')

args        = parser.parse_args()
# plasma electron temperature (eV) and density (cm-3) for a typical tokamak.
Te, n0 = args.Te * kB, args.den
lam_De   = Electron(n=args.den*1.e-6, eV=args.Te).debye
print('Debye Length:',lam_De)

# range of distances to plot phi for, in m.
rmin = lam_De / 10
rmax = lam_De * 5
r = np.linspace(rmin, rmax, 100)
qT = 1
phi_unscreened = calc_unscreened_potential(r, qT)
phi = calc_e_potential(r, lam_De, qT)



##### FIG SIZE CALC ############
figsize = np.array([90,90/1.618]) #Figure size in mm
dpi = 300                         #Print resolution
ppi = np.sqrt(1920**2+1200**2)/24 #Screen resolution

mp.rc('text', usetex=False)
mp.rc('font', family='sans-serif', size=10, serif='Computer Modern Roman')
mp.rc('axes', titlesize=10)
mp.rc('axes', labelsize=10)
mp.rc('xtick', labelsize=10)
mp.rc('ytick', labelsize=10)
mp.rc('legend', fontsize=10)
########################################
# Plot the figure. Apologies for the ugly and repetitive unit conversions from
# m to µm and from V to mV.
fig, ax = plt.subplots(figsize=figsize/25.4,constrained_layout=True,dpi=dpi)
ax.plot(r*1.e6, phi_unscreened * 1000,
                label=r'Unscreened: $\phi = \frac{e}{4\pi\epsilon_0 r}$')
ax.plot(r*1.e6, phi * 1000,
                label=r'Screened: $\phi = \frac{e}{4\pi\epsilon_0 r}'
                      r'e^{-r/\lambda_\mathrm{D}}$')
ax.axvline(lam_De*1.e6, ls='--', c='k')
ax.annotate(r'$\lambda_\mathrm{D} = %.1f \mathrm{\mu m}$'%(lam_De*1.e6),xy=(lam_De*1.1*1.e6, max(phi_unscreened)/2 * 1000))
ax.legend()
ax.set_xlabel(r'$r/\mathrm{\mu m}$')
ax.set_ylabel(r'$\phi/\mathrm{mV}$')
plt.savefig('debye_length.png',dpi=dpi)
plt.show()
