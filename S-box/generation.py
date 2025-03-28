import numpy as np
from itertools import product

def generate_linear_functions(num_variables=8):
    # Generate all 8-variable linear Boolean functions.
    num_rows = 2 ** num_variables
    variables = np.array(list(product([0, 1], repeat=num_variables)))
    linear_functions = []

    # Generate all coefficients for linear functions (including constant term)
    for coeffs in product([0, 1], repeat=num_variables + 1):
        linear_function = (np.dot(variables, coeffs[:-1]) + coeffs[-1]) % 2
        linear_functions.append(linear_function)

    return np.array(linear_functions)

def calculate_hamming_distance(func1, func2):
    # Hamming distance between two Boolean functions.
    return np.sum(func1 != func2)

def calculate_nonlinearity(boolean_function, linear_functions):
    hamming_distances = [
        calculate_hamming_distance(boolean_function, linear_func)
        for linear_func in linear_functions
    ]
    return min(hamming_distances)

if __name__ == "__main__":
    sbox_filename = "D:\Repos\Cryptography\S-box\sbox.SBX"
    from extraction import read_sbox_file, extract_boolean_functions

    sbox_data = read_sbox_file(sbox_filename)
    boolean_functions = extract_boolean_functions(sbox_data)

    # Generate all 8-variable linear functions
    linear_functions = generate_linear_functions()

    # Calculate nonlinearity for each Boolean function
    for i, boolean_function in enumerate(boolean_functions):
        nonlinearity = calculate_nonlinearity(boolean_function, linear_functions)
        print(f"Nonlinearity of Function F{i+1}: {nonlinearity}")