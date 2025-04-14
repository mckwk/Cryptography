import numpy as np
import matplotlib.pyplot as plt

def calculate_cycles(sbox):
    visited = [False] * len(sbox)
    cycle_count = 0

    for i in range(len(sbox)):
        if not visited[i]:
            cycle_count += 1
            current = i
            while not visited[current]:
                visited[current] = True
                current = sbox[current]

    return cycle_count

def plot_cycles(sboxes):
    cycle_counts = []

    for sbox in sboxes:
        cycles = calculate_cycles(sbox)
        cycle_counts.append(cycles)

    # S-box indices
    x = np.arange(1, len(sboxes) + 1)

    # Plotting the graph
    plt.figure(figsize=(12, 6))
    plt.bar(x, cycle_counts, color='purple', alpha=0.7, label='Number of Cycles')

    plt.xlabel('S-box Index')
    plt.ylabel('Number of Cycles')
    plt.title('Number of Cycles in Each S-box')
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

    for i, sbox in enumerate(sboxes):
        cycles = calculate_cycles(sbox)
        print(f"S-box {i+1}: Number of Cycles = {cycles}")

    plot_cycles(sboxes)