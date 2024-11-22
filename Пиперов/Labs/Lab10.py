import numpy as np


def create_arrays():
    zeros_array = np.zeros(10)

    ones_array = np.ones(10)

    fives_array = np.full(10, 5)

    return zeros_array, ones_array, fives_array


zeros, ones, fives = create_arrays()

print("Масив нулей: \n", zeros)
print("Масив единиц: \n", ones)
print("Масив пятерок: \n", fives)
