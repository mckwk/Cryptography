import numpy as np

def generate_random_sbox(size=256):
    sbox = np.arange(size)
    # np.random.shuffle(sbox)
    sbox = np.random.randint(0, 256, size=256)
    return sbox

def generate_multiple_sboxes(count=100, size=256):
    sboxes = []
    for _ in range(count):
        sboxes.append(generate_random_sbox(size))
    return sboxes

def save_sboxes_to_file(sboxes, filename="S-box random/random_sboxes.txt"):
    with open(filename, "w") as f:
        for i, sbox in enumerate(sboxes):
            f.write(f"S-box {i+1}:\n")
            f.write(" ".join(map(str, sbox)) + "\n\n")

if __name__ == "__main__":

    random_sboxes = generate_multiple_sboxes(count=100, size=256)
    save_sboxes_to_file(random_sboxes, filename="S-box random/random_sboxes.txt")