# %%

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
sp.init_printing()
lp = lambda x: print(sp.latex(x))
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')

# %%

# introduce time and kappa symbolic variables

t = sp.symbols('t', real=True)
kappa = sp.symbols('kappa', positive=True)

# define position as a function of time

x = (sp.sqrt(1 + kappa**2 * t**2) -1)/kappa

# differentiate it symbolically

v = sp.diff(x, t)

# %%

# plot velocity as a function of coordinate time
# using kappa = 1
# this does not work in vscode, don't know why

times = np.arange(-5,5, step=0.1)
velocity = sp.lambdify(t, v.subs(kappa, 1), 'numpy')

plt.plot(times, velocity(times))
plt.xlabel("Time [$1/\kappa$]")
plt.ylabel("Velocity [c]")
plt.savefig(fname='../figures/velocity.pdf', format = 'pdf')

#%%

# print gamma factor

gamma = sp.simplify(1/sp.sqrt(1-v**2))
lp(gamma)
#%%

sp.integrate(1/gamma, t)

#%%

tau = sp.symbols('tau', real=True)

lp(sp.simplify(x.subs(t, sp.sinh(kappa*tau)/kappa)))

#%%
