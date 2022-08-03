from Parameters import Par
import matplotlib.pyplot as plt
from Matrix_expo import *
import numpy as np


time_step_number = 70  # making the time size of the event
sol = [[Par.I0, Par.Pois0]]   # collecting in a list the initial Iodine and Xenon concentration

# Iterating
for i in range(time_step_number):
    sol.append(matrix_exp(sol[i][0], sol[i][1]))
sol = np.array(sol)*Par.sigma_Xe / (Par.sigma_f * Par.v)

# Plotting the solution
fig1 = plt.figure()
plt.title("Solution by matrix_exponential_method")
plt.plot(sol[:, 1], '*r', label='Xenon-135')
plt.plot(sol[:, 0], '-go', label='Iodine-135')
plt.xlabel("Time [hours]")
plt.ylabel("Xenon & Iodine")
plt.legend()
plt.grid(True)
plt.show()

# Poisoning plot
fig2 = plt.figure()
plt.title("Poisoning by matrix_expm")
plt.plot(sol[:, 1], '-bo', label='Xenon Poisoning')
plt.xlabel("Time [hours]")
plt.ylabel("Poisoning [pcm]")
plt.legend()
plt.grid(True)
plt.show()