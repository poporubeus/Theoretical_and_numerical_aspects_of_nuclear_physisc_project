from Parameters import Par


# ------------------- Functions -----------------------------------------------------

def iodine_first_derivative(iodine_t):
    """
    Function which calculates the first derivative of Runge-Kutta method of Iodine
    
    Args:
        iodine_t(float) : Iodine concentration at time t 

    Returns:
        first_deriv(float) : first derivative of Iodine at time t 
    """
    first_deriv = Par.time_step*( - Par.lambda_I*iodine_t)
    return first_deriv 


def iodine_second_derivative(iodine_t):
    """
    Function which calculates the second derivative of Runge-Kutta method of Iodine
    
    Args:
        iodine_t(float) : Iodine concentration at time t 

    Returns:
        second_deriv(float) : second derivative of Iodine at time t 
    """
    second_deriv = Par.time_step*(
        - Par.lambda_I*(
            iodine_t + 0.5*iodine_first_derivative(iodine_t)
        )
    )
    return second_deriv


def iodine_third_derivative(iodine_t):
    """
    Function which calculates the third derivative of Runge-Kutta method of Iodine
    
    Args:
        iodine_t(float) : Iodine concentration at time t 

    Returns:
        third_deriv(float) : third derivative of Iodine at time t 
    """
    second_deriv = iodine_second_derivative(iodine_t)
    third_deriv = Par.time_step*(
         - Par.lambda_I*(
            iodine_t + 0.5*second_deriv 
        )
    )

    return third_deriv


def iodine_fourth_derivative(iodine_t):
    """
    Function which calculates the fourth derivative of Runge-Kutta method of Iodine
    
    Args:
        iodine_t(float) : Iodine concentration at time t 

    Returns:
        fourth_deriv(float) : fourth derivative of Iodine at time t 
    """
    third_deriv = iodine_third_derivative(iodine_t)
    fourth_deriv = Par.time_step*(
        - Par.lambda_I*(
            iodine_t + third_deriv
        )
    )

    return fourth_deriv


def iodine_evolve_rungekutta(iodine_t):
    """
    Function that realize how the iodine at time t evolves following the Runge-Kutta formula
    until the fourth-order
    
    Args:
        iodine_t(float) : Iodine concentration at time t
        
    Returns:
        iodine_express (float) : increment of the Runge-Kutta formula of the fourth-order for Iodine
    """

    first_deriv = iodine_first_derivative(iodine_t)
    second_deriv = iodine_second_derivative(iodine_t)
    third_deriv = iodine_third_derivative(iodine_t)
    fourth_deriv = iodine_fourth_derivative(iodine_t)
    iodine_express = iodine_t + (1/6)*(first_deriv+2*second_deriv+2*third_deriv+fourth_deriv)
    return iodine_express


# New parameters to simplify the calculations
alpha0 = 0
beta = Par.lambda_Xe
poisoning_vals = [Par.Pois0]  # List to see how poisoning modifies


def xenon_first_derivative(xenon_t, iodine_t):

    """
    Function which calculates the first derivative of Runge-Kutta method of Xenon
    
    Args:
        xenon_t (float) : Xenon concentration at time t 

    Returns:
        first_deriv (float) : first derivative of Xenon at time t 

    """
   
    first_deriv = Par.time_step*( alpha0 + Par.lambda_I*iodine_t - beta* xenon_t)
    return first_deriv 


def xenon_second_derivative(xenon_t, iodine_t):

    """
    Function which calculates the second derivative of Runge-Kutta method of Xenon
    
    Args:
        xenon_t (float) : Xenon concentration at time t 

    Returns:
        second_deriv (float) : second derivative of Xenon at time t 

    """

    second_deriv = Par.time_step*(
        alpha0 + Par.gamma_I*(iodine_t + .5*iodine_first_derivative(iodine_t)) 
        -beta*(xenon_t + .5*xenon_first_derivative(xenon_t, iodine_t))
    )
    return second_deriv


def xenon_third_derivative(xenon_t, iodine_t):

    """
    Function which calculates the third derivative of Runge-Kutta method of Xenon
    
    Args:
        xenon_t (float) : Xenon concentration at time t 

    Returns:
        third_deriv (float) : third derivative of Xenon at time t 

    """
    # Uploading
    second_deriv = xenon_second_derivative(xenon_t, iodine_t)
    third_deriv = Par.time_step*(
         alpha0 + Par.gamma_I*(
         iodine_t+.5*iodine_second_derivative(iodine_t)) - beta* (
         xenon_t + .5*second_deriv)
    )

    return third_deriv


def xenon_fourth_derivative(xenon_t, iodine_t):

    """
    Function which calculates the fourth derivative of Runge-Kutta method of Xenon
    
    Args:
        xenon_t (float) : Xenon concentration at time t 

    Returns:
        fourth_deriv (float) : fourth derivative of Xenon at time t 

    """
    # Uploading 
    third_deriv = xenon_third_derivative(xenon_t, iodine_t)
    fourth_deriv = Par.time_step*(
        alpha0 + Par.gamma_I * (
        iodine_t + iodine_third_derivative(iodine_t)) - beta*(
        xenon_t + third_deriv)
    )

    return fourth_deriv


def xenon_evolve_rungekutta(xenon_t, iodine_t):

    """
    Function that realizes how the Iodine at time t evolves following the Runge-Kutta formula
    until the fourth-order
    
    Args:
        iodine_t (float) : Iodine concentration at time t
        
    Returns:
        iodine_express (float) : increment of the Runge-Kutta formula of the fourth-order for Iodine
    """

    first_deriv = xenon_first_derivative(xenon_t, iodine_t)
    second_deriv = xenon_second_derivative(xenon_t, iodine_t)
    third_deriv = xenon_third_derivative(xenon_t, iodine_t)
    fourth_deriv = xenon_fourth_derivative(xenon_t, iodine_t)
    return xenon_t + (1/6)*(first_deriv+2*second_deriv+2*third_deriv+fourth_deriv)

# ------------------- End functions ----------------------------------------------




