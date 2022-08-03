# Theoretical and numerical aspects of nuclear physisc project
Implementation of Bateman equation using Runge-Kutta method and matrix exponential method.

In this project we solve the Bateman's equations for a decay process that involves Iodine-135 and Xenon-135 numerically. In particular, Iodine-135 decays into Xenon-135 and the main process we see is a poison growing. 
The poisoning function represents how much Xenon-135 grows by  Iodine-135 decay. If the thermal neutron flux $\phi$ is modified we can observe many curves one inside the other.

## Numerical methods
The methods chosen for this code are fourth-order Runge-Kutta and the matrix exponential method.
Runge-Kutta is an iterative method to compute the solution of a system of ODE;
matrix exponential method does the same using a costant coefficient matrix and arrays inside which collecting the equations.

## Plots
The plots inserted here want to show the different poisoning curves coming from the implementation of the two different methods.
Poisoning plot coming from matrix exponential method: [[/images/

## Math formulas
All of the math formulas are collected into 

## Python libraries
1. numpy;
2. matplotlib.pyplot;
3. scipy.linalg.expm;
4. tabulate.

