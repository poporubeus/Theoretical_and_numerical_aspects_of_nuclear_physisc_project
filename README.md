# Theoretical_and_numerical_aspects_of_nuclear_physisc_project
Implementation of Bateman equation using Runge-Kutta method and matrix exponential method.

In this project we solve the Bateman's equations for a decay process that involves Iodine-135 and Xenon-135 numerically. In particular, Iodine-135 decays into Xenon-135 and the main process we see is a poison growing. 
The poisoning function ![first equation](![immagine](https://user-images.githubusercontent.com/93386417/182612688-550b6c8c-bbb7-4655-8fdf-5c0a4061804f.png)
) represents how much Xenon-135 grows by  Iodine-135 decay. If the thermal neutron flux $\phi$ is modified we can observe many curves one inside the other. 

The method chosen for this code are fourth-order Runge-Kutta method and the matrix exponential method.

