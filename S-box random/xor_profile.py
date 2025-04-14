import numpy as np
import matplotlib.pyplot as plt

def calculate_xor_profile(s_box):
    size = len(s_box)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for input_diff in range(size):
        for x in range(size):
            y1 = s_box[x]
            y2 = s_box[x ^ input_diff]
            output_diff = y1 ^ y2
            matrix[input_diff][output_diff] += 1
    print("Max value in XOR profile:", np.max(matrix[1::]))
    return matrix

def plot_max_xor_profile(sboxes):
    max_xor_values = []

    for sbox in sboxes:
        xor_profile = calculate_xor_profile(sbox)
        max_value = np.max(xor_profile[1:])  # Exclude the first row (input_diff = 0)
        max_xor_values.append(max_value)

    # S-box indices
    x = np.arange(1, len(sboxes) + 1)

    # Plotting the graph
    plt.figure(figsize=(12, 6))
    plt.plot(x, max_xor_values, marker='o', linestyle='-', color='blue', label='Max XOR Profile Value')

    plt.xlabel('S-box Index')
    plt.ylabel('Max XOR Profile Value')
    plt.title('Max XOR Profile Value for Each S-box')
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

    plot_max_xor_profile(sboxes)