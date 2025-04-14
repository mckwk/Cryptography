import numpy as np
import matplotlib.pyplot as plt

def check_sbox_balance(sbox):
    total_bits = len(sbox) * 8  # Each value in the S-box is 8 bits
    ones_count = sum(bin(value).count('1') for value in sbox)
    zeros_count = total_bits - ones_count
    return ones_count, zeros_count

def plot_ones_and_zeroes_bar(sboxes):
    ones_counts = []
    zeros_counts = []
    for sbox in sboxes:
        ones, zeros = check_sbox_balance(sbox)
        ones_counts.append(ones)
        zeros_counts.append(zeros)

    # S-box indices
    x = np.arange(1, len(sboxes) + 1)

    # Creating the bar chart
    width = 0.35  # Width of the bars
    plt.figure(figsize=(12, 6))
    plt.bar(x - width / 2, ones_counts, width, label='Ones', color='skyblue')
    plt.bar(x + width / 2, zeros_counts, width, label='Zeroes', color='salmon')

    plt.xlabel('S-box Index')
    plt.ylabel('Number of Bits')
    plt.title('Number of Ones and Zeroes in S-boxes')
    plt.xticks(x)
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

    for i, sbox in enumerate(sboxes):
        ones, zeros = check_sbox_balance(sbox)
        print(f"S-box {i+1}: Ones = {ones}, Zeroes = {zeros}")

    plot_ones_and_zeroes_bar(sboxes)