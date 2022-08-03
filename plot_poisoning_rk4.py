import matplotlib.pyplot as plt
from datas import poisoning_vals, rk4_visualization
from Parameters import Par


# Calling the function rk4_visualization
visualize = rk4_visualization(Par.duration)

# Plotting function
fig1 = plt.figure()
plt.title("Poisoning_plot")
plt.plot(poisoning_vals, '-ro', label='Xenon poisoning')
plt.xlabel('Time [seconds]')
plt.ylabel('Poisoning [pcm]')
plt.grid(True)
plt.legend()
plt.show()


