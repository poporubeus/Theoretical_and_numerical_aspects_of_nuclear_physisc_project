class Par:

    # Class of costants and parameters entering in the code
    lambda_I = 2.874e-5
    lambda_Xe = 2.027e-5
    sigma_Xe = 2.75e-18
    phi = 4.42e+20
    gamma_I = 0.061
    gamma_Xe = 0.003
    sigma_f = 0.008
    v = 2.3

    # Iodine and Xenon concentration at initial time t = 0
    I0 = gamma_I * sigma_f * phi / lambda_I
    Xe0 = sigma_f * phi * (gamma_I + gamma_Xe) / (lambda_Xe + sigma_Xe * phi)
    Pois0 = 0

    # Size of the problem
    time_step = 3600
    duration = 70