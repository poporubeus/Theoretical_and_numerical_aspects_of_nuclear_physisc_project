from tabulate import tabulate
from rk4_method_2 import (iodine_evolve_rungekutta, iodine_first_derivative, iodine_second_derivative, iodine_third_derivative, iodine_fourth_derivative, xenon_evolve_rungekutta, xenon_first_derivative, xenon_fourth_derivative, xenon_second_derivative, xenon_third_derivative,
xenon_first_derivative, xenon_second_derivative, xenon_third_derivative, xenon_fourth_derivative,
xenon_evolve_rungekutta, iodine_evolve_rungekutta)
from Parameters import Par

#-------------------- Lists ------------------------------------------------------

iodine_k1 = []   # Derivative coefficients of Iodine (k's) and Xenon (g's)
iodine_k2 = []
iodine_k3 = []
iodine_k4 = []
xenon_g1 = []
xenon_g2 = []
xenon_g3 = []
xenon_g4 = []

iodine_vals= []
xenon_vals = []
poisoning_vals = [0]

table = []
table_coeff = []

#-------------------- End of Lists ------------------------------------------------


# Iteration and uploading values in to the lists
def rk4_visualization(duration):
    iodine_t = Par.I0
    xenon_t = Par.Xe0
    
    
    
    for i in range(Par.duration):
        iodine_t = iodine_evolve_rungekutta(iodine_t)
        xenon_t = xenon_evolve_rungekutta(xenon_t, iodine_t)
        iodine_vals.append(iodine_t)
        xenon_vals.append(xenon_t)
        iodine_k1.append(iodine_first_derivative(iodine_t))
        iodine_k2.append(iodine_second_derivative(iodine_t))
        iodine_k3.append(iodine_third_derivative(iodine_t))
        iodine_k4.append(iodine_fourth_derivative(iodine_t))
        xenon_g1.append(xenon_first_derivative(xenon_t, iodine_t))
        xenon_g2.append(xenon_second_derivative(xenon_t, iodine_t))
        xenon_g3.append(xenon_third_derivative(xenon_t, iodine_t))
        xenon_g4.append(xenon_fourth_derivative(xenon_t, iodine_t))
        poisoning_vals.append(-Par.sigma_Xe*xenon_evolve_rungekutta(xenon_t, iodine_t) / (Par.sigma_f * Par.v))
        table.append([i, iodine_vals[i], xenon_vals[i], poisoning_vals[i]])
        table_coeff.append([i, iodine_k1[i], iodine_k2[i], iodine_k3[i], iodine_k4[i], xenon_g1[i], xenon_g2[i], xenon_g3[i], xenon_g4[i]])

    print("Table of data")
    print(" ")
    table_of_data = print(tabulate(table, headers=['t', 'iodine', 'xenon', 'poisoning']))
    print(" ")
    table_of_coefficients = print("Table of derivative coefficients")
    print(" ")
    print(tabulate(table_coeff, headers=['t', 'iodine_coeff1', 'iodine_coeff2', 'iodine_coeff3', 'iodine_coeff4', 'xenon_coeff1', 'xenon_coeff2', 'xenon_coeff3', 'xenon_coeff4']))
    print(" ")    
    return table_of_data, table_of_coefficients


