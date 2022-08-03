# Functions
import numpy as np
from Parameters import Par


def iodine_function(t):
    """ 
        Function that express the solution of the Iodine differential equation
        
        Args:
            t[float, int] : time where evaluating the function
        
        Returns:
        didt[float, int] : right-hand side of Iodine differential equation
    """
    didt = ((Par.gamma_I*Par.sigma_f*Par.phi) / Par.lambda_I) * np.exp(-Par.lambda_I * t)
    return didt 

def xenon_function(t):
    """ 
        Function that express the solution of the Xenon differential equation.
        
        Args:
            t[int, float] : time where evaluating the function.  
        
        Returns:
            dxdt[float, int] : right-hand side of Xenon differential equation.
    """
    dxdt = Par.sigma_f*Par.phi*((Par.gamma_I + Par.gamma_Xe)/(Par.lambda_Xe + Par.sigma_Xe*Par.phi)* np.exp(-Par.lambda_Xe*t) + (
        (Par.gamma_I)/(Par.gamma_I-Par.gamma_Xe)*(np.exp(-Par.lambda_Xe*t) - np.exp(-Par.lambda_I*t))
    ))
    return dxdt


def sub_function(t):
    """
        Function that express the subtraction between iodine_function and xenon_function
        in order to get the solution of the system.
        
        Args:
            t[float, int] : time.
        
        Returns 
            """
    z = iodine_function(t) - xenon_function(t)
    return z


def bisection(sub_function, a, b, tol):
    """
        Function that calculates the solution of the system of ODE by bisection method.
        
        Args: 
            sub_function : function defined as the difference between iodine_function and xenon_function.
            Example:
                z (sub_function) = f (iodine_function) - g (xenon_function).

            a(int, float) : first extrema of the domain.

            b(int, float) : second extrema of the domain.

            tol(int, float) : tolerance to arrest the process.
            Example: if np.abs(z(m)) == < tol:
                STOP THE PROCESS,
                else: 
                    CONTINUE    
        
        Returns:
            bisection() : the method to get the root of the function. In this case, the solution of the system.
    """

    if np.sign(sub_function(a)) == np.sign(sub_function(b)):
        raise Exception("There's no zeros here, try again.")

    # Get the midpoint
    m = (a+b)/2

    if np.abs(sub_function(m)) < tol:
        # Stopping condition, report m as a root
        return m 
    elif np.sign(sub_function(a)) == np.sign(sub_function(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return bisection(sub_function, m, b, tol)
    elif np.sign(sub_function(b)) == np.sign(sub_function(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return bisection(sub_function, a, m, tol)


first_point = input("Give the first extrema of the domain: ")
second_point = input("Give the second extrema of the domain: ")
error = input("Give the tolerance [--ATTENTION-- the tolerance should be less than the previous values you gave]: ")

root1 = bisection(sub_function, first_point, second_point, error)
print("The root is: ", root1)

print("That is the numerical solution of the system. ")
