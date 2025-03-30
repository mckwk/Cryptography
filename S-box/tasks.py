import numpy as np


def check_balance(boolean_functions):
    for i, func in enumerate(boolean_functions):
        ones = sum(func)
        zeros = len(func) - ones
        balanced = ones == zeros
        print(f"Function F{i+1}: Balanced = {balanced} (1s = {ones}, 0s = {zeros})")

def verify_sac(boolean_functions):
    num_variables = int(np.log2(len(boolean_functions[0])))
    total_flips = 0  # Total number of bit flips across all functions
    for i, func in enumerate(boolean_functions):
        for bit_position in range(num_variables):
            # Create a mask to flip the specific bit
            mask = 1 << bit_position
            xor_results = []
            for input_index in range(len(func)):
                flipped_index = input_index ^ mask  # Flip the bit at `bit_position`
                xor_results.append(func[input_index] ^ func[flipped_index])
            # Check if the XOR results are balanced
            ones = sum(xor_results)
        total_flips += ones
        print(f"Function F{i+1}: SAC = {ones} out of {len(func)} (probability = {ones/len(func)})")
    print(f"Overall SAC Probability for the block: {total_flips /((2**num_variables)*num_variables)}")
