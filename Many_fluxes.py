from Parameters import Par
import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt 


def evolve(t):
    return np.matmul(expm(t*A_matrix),np.array([Par.I0, Par.Xe0]))
t_domain = np.linspace(0,70*3600,70)

flux_arrays = []
for j in range(10):
    A_matrix = np.array([[-Par.lambda_I, 0],
                     [Par.lambda_I, - Par.lambda_Xe - Par.sigma_Xe * Par.phi * (1/(j+1)) * 1e-7]])
    newvals = []
    for idx,i in enumerate(t_domain):
        newvals.append(evolve(i))
    flux_arrays.append(np.array(newvals))
    
for i in list(range(10))[::2]:
    legend_var=round(1-i*0.1, 1)
    plt.plot(Par.sigma_Xe * flux_arrays[i][:,1]/(Par.v*Par.sigma_f), '--', label=(legend_var))
    plt.legend()
    plt.xlabel("Time [hours]")
    plt.ylabel("Poisoning at different flux %")
    plt.title("Poisoning at different fluxes")
    plt.grid(True)
    
plt.show()