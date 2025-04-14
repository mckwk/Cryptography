import numpy as np
from itertools import product
from extraction import read_sbox_file, extract_boolean_functions
from tasks import calculate_nonlinearity, calculate_xor_profile, check_balance, find_cycles, verify_sac

def generate_linear_functions(num_variables=8):
    # all 8-variable linear Boolean functions.
    variables = np.array(list(product([0, 1], repeat=num_variables)))
    linear_functions = []

    # oefficients
    for coeffs in product([0, 1], repeat=num_variables + 1):
        linear_function = (np.dot(variables, coeffs[:-1]) + coeffs[-1]) % 2
        linear_functions.append(linear_function)

    return np.array(linear_functions)


if __name__ == "__main__":
    sbox_filename = r"D:\Repos\Cryptography\S-box\sbox.SBX"

    # Read S-box data and extract Boolean functions
    sbox_data = read_sbox_file(sbox_filename)
    boolean_functions = extract_boolean_functions(sbox_data)

    # Generate all 8-variable linear functions
    linear_functions = generate_linear_functions()


    for i, boolean_function in enumerate(boolean_functions):
        nonlinearity = calculate_nonlinearity(boolean_function, linear_functions)
        print(f"Nonlinearity of Function F{i+1}: {nonlinearity}")

    check_balance(boolean_functions)

    verify_sac(boolean_functions)

    sbox = sbox_data[0::2] 
    xor_profile = calculate_xor_profile(sbox)

    cycles = find_cycles(sbox)
    print("Cycles in the S-box:")
    for cycle in cycles:
        print(cycle)