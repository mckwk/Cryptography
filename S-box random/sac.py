import numpy as np
import matplotlib.pyplot as plt

def calculate_sac(sbox):
    """
    Calculate the average SAC (Strict Avalanche Criterion) value for an S-box.
    SAC measures how flipping one input bit affects the output bits.
    """
    size = len(sbox)
    n_bits = int(np.log2(size))  # Number of input bits
    total_differences = 0

    for bit in range(n_bits):
        flipped_sbox = []
        for i in range(size):
            flipped_input = i ^ (1 << bit)  # Flip the current input bit
            flipped_sbox.append(sbox[flipped_input])

        # Compare the original and flipped outputs
        differences = [bin(sbox[i] ^ flipped_sbox[i]).count('1') for i in range(size)]
        total_differences += sum(differences)

    # Normalize by the total number of comparisons
    avg_sac_value = total_differences / (size * n_bits * n_bits)
    return avg_sac_value

def plot_sac(sboxes):
    """
    Plot the average SAC values for multiple S-boxes.
    """
    sac_values = [calculate_sac(sbox) for sbox in sboxes]

    # Plot SAC values
    plt.figure(figsize=(14, 7))
    plt.plot(range(1, len(sboxes) + 1), sac_values, marker='o', color='skyblue', label='SAC Value')

    # Ensure 100 values on the x-axis
    plt.xticks(range(1, len(sboxes) + 1))  # Show all S-box indices on the x-axis

    plt.xlabel('S-box Index')
    plt.ylabel('Average SAC Value')
    plt.title('Average SAC Values for S-boxes')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
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

    plot_sac(sboxes)