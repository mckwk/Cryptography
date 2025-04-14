import numpy as np
import matplotlib.pyplot as plt

def generate_affine_functions(n, m):
    """
    Generate all possible affine functions for given input and output bit sizes.
    """
    affine_functions = []
    for a in range(1, 2**n):  # Exclude a = 0 (constant function)
        for b in range(2**m):
            affine_functions.append((a, b))
    return affine_functions

def calculate_nonlinearity(sbox, affine_functions):
    """
    Calculate the nonlinearity of an S-box using precomputed affine functions.
    """
    size = len(sbox)
    min_hamming_distance = float('inf')

    for a, b in affine_functions:
        affine_output = [(bin(x & a).count('1') % 2) ^ b for x in range(size)]
        hamming_distance = sum(1 for i in range(size) if affine_output[i] != sbox[i])
        min_hamming_distance = min(min_hamming_distance, hamming_distance)

    # Nonlinearity is half the minimum Hamming distance
    return min_hamming_distance // 2

def plot_nonlinearity(sboxes, affine_functions):
    nonlinearity_values = []

    for sbox in sboxes:
        nonlinearity = calculate_nonlinearity(sbox, affine_functions)
        nonlinearity_values.append(nonlinearity)

    # S-box indices
    x = np.arange(1, len(sboxes) + 1)

    # Plotting the graph
    plt.figure(figsize=(12, 6))
    plt.plot(x, nonlinearity_values, marker='o', linestyle='-', color='green', label='Nonlinearity')

    plt.xlabel('S-box Index')
    plt.ylabel('Nonlinearity')
    plt.title('Nonlinearity of Each S-box')
    plt.xticks(x)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    sboxes = []
    with open("S-box random/random_sboxes.txt", "r") as f:
        current_sbox = []
        for line in f:
            if line.startswith("S-box"):
                if current_sbox:
                    sboxes.append(current_sbox)
                    current_sbox = []
            else:
                current_sbox.extend(map(int, line.split()))
        if current_sbox:
            sboxes.append(current_sbox)

    # Determine input and output bit sizes
    n = int(np.log2(len(sboxes[0])))  # Input bit size
    m = int(np.log2(max(max(sboxes)) + 1))  # Output bit size

    # Precompute affine functions
    affine_functions = generate_affine_functions(n, m)

    for i, sbox in enumerate(sboxes):
        nonlinearity = calculate_nonlinearity(sbox, affine_functions)
        print(f"S-box {i+1}: Nonlinearity = {nonlinearity}")

    plot_nonlinearity(sboxes, affine_functions)