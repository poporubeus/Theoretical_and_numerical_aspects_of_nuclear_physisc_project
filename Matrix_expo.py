from scipy.linalg import expm
import numpy as np
from Parameters import Par


# Creating the matrix A
A_matrix = np.array([[-Par.lambda_I, 0],
                     [Par.lambda_I, - Par.lambda_Xe - Par.sigma_Xe * Par.phi * 1e-10]
                     ])


def matrix_exp(iodine_t, xenon_t):
    """
    Function which implements matrix exponential method.

    Args:
        iodine_t(float) : concentration of Iodine at time t;
        xenon_t(float) : concentration of Xenon at time t.

    Returns:
        exp_matrix_product(float) : product between the exponential matrix and the array containing iodine_t and xenon_t.

    Example:
        make an array of [2 = rows, 1 = columns] then pass to np.matmul the matrix, the array:
            v = np.array([x, y])
            A = np.array([[a, b], [c, d]]) and take expm(t * A) to call exponentiation method,
            then use np.matmul(expm(t * A), v).

    """
    exp_matrix_product = np.matmul(expm(3600*A_matrix), np.array([iodine_t, xenon_t]))

    return exp_matrix_product



