import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from matplotlib import rc
from scipy.optimize import fsolve
rc('text', usetex=True)
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text.latex', preamble=r'''\usepackage{amsmath}
\usepackage{physics}
\usepackage{siunitx}
''')

plt.close()

R = np.linspace(0, 3, num=200)
f = lambda x: (x-1) * np.exp(x) 
# fig = plt.figure(1)
# plt.plot(R, f(R))
# plt.grid()
# plt.show()
# plt.close()

@np.vectorize
def r(U, V, hint=None):
    """
    a numerical solution to 
    U**2 - V**2 = (r-1) * exp(r/2)
    """

    LHS = U ** 2 - V ** 2
    if (LHS < 0):
        return (0)
    function = lambda x: (x-1)*np.exp(x) - LHS
    if(not hint):
        hint = max(np.log(LHS), 0)
    
    return fsolve(function, x0=hint)

def U_from_r(r, V):
    return( (r-1)*np.exp(r) + V**2)

# Us = np.linspace(-10, 10, num=200)
for V0 in range(4):
#     rs = r(Us, V0)
    if (V0 == 0):
        lab = f"$V_0 = $ {V0}"
    else:
        lab= f"$V_0 = \pm$ {V0}"
#     plt.plot(rs, Us, label=lab)
    rs = np.linspace(0, 2, num=200)
    Us = U_from_r(rs, V0)
    positive_U = np.nonzero(Us>0)
    rs = rs[positive_U]
    Us = Us[positive_U]
    plt.plot(np.append(np.flip(rs), rs), np.append(np.flip(Us), -Us), label=lab)
plt.xlabel("$r(U^2 - V^2) / 2GM$")
plt.ylabel("$U$")
plt.legend()
plt.savefig('kruskal_constant_V.pdf', format='pdf')
plt.close()