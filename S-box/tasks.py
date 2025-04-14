import numpy as np


def calculate_hamming_distance(func1, func2): # number of differing bits between two boolean functions
    return np.sum(func1 != func2)

def calculate_nonlinearity(boolean_function, linear_functions): # nonlinearity = min Hamming distance to all linear functions
    hamming_distances = [
        calculate_hamming_distance(boolean_function, linear_func)
        for linear_func in linear_functions
    ]
    return min(hamming_distances)

def check_balance(boolean_functions): # the number of 1s and 0s are equal in each boolean function
    for i, func in enumerate(boolean_functions):
        ones = sum(func)
        zeros = len(func) - ones
        balanced = ones == zeros
        print(f"Function F{i+1}: Balanced = {balanced} (1s = {ones}, 0s = {zeros})")

def verify_sac(boolean_functions): # Check if flipping one input bit changes the output about half the time
    num_variables = int(np.log2(len(boolean_functions[0])))
    total_flips = 0  # Total number of bit flips across all functions
    for i, func in enumerate(boolean_functions):
        for bit_position in range(num_variables):
            mask = 1 << bit_position # mask to flip the specific bit
            xor_results = []
            for input_index in range(len(func)):
                flipped_index = input_index ^ mask  # Flip the bit
                xor_results.append(func[input_index] ^ func[flipped_index])
            # Check if the XOR results are balanced
            ones = sum(xor_results)
        total_flips += ones
        print(f"Function F{i+1}: SAC = {ones} out of {len(func)} (probability = {ones/len(func)})")
    print(f"Overall SAC Probability: {total_flips /((2**num_variables)*num_variables)}")


def calculate_xor_profile(s_box):
    size = len(s_box)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for input_diff in range(size):
        for x in range(size):
            y1 = s_box[x]
            y2 = s_box[x ^ input_diff]
            output_diff = y1 ^ y2
            matrix[input_diff][output_diff] += 1
    np.savetxt("S-box/xor_profile_full.txt", matrix, fmt='%d', delimiter=' ')
    print("Max value in XOR profile:", np.max(matrix[1::]))
    return matrix

def find_cycles(sbox): # starting from i=0, checking where sbox[i] points to, and so on until we return to i=0
    visited = [False] * len(sbox)
    cycles = []
    for start in range(len(sbox)):
        if not visited[start]:
            cycle = []
            current = start
            while not visited[current]:
                cycle.append(current)
                visited[current] = True
                current = sbox[current]
            cycles.append(cycle)
    return cycles