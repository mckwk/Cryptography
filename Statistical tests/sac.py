import numpy as np
import random
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes

def encrypt_aes(input_value):
    key = get_random_bytes(16)  # AES-128
    cipher = AES.new(key, AES.MODE_ECB)
    input_bytes = input_value.to_bytes(8, byteorder='big') + b'\x00' * 8  # Pad to 16 bytes
    encrypted_bytes = cipher.encrypt(input_bytes)
    encrypted_value = int.from_bytes(encrypted_bytes[:8], byteorder='big')  # Use first 64 bits of the output
    return encrypted_value

def encrypt_des(input_value):
    key = get_random_bytes(8)  # DES key size is 8 bytes
    cipher = DES.new(key, DES.MODE_ECB)
    input_bytes = input_value.to_bytes(8, byteorder='big')  # DES block size is 8 bytes
    encrypted_bytes = cipher.encrypt(input_bytes)
    encrypted_value = int.from_bytes(encrypted_bytes, byteorder='big')  # Use the entire 64-bit output
    return encrypted_value

def flip_bit(value, bit_index):
    return value ^ (1 << bit_index)

def calculate_sac(encrypt_function):
    sac_matrix = np.zeros((64, 64), dtype=int)

    for _ in range(2**20):
        input_value = random.getrandbits(64)
        original_output = encrypt_function(input_value)

        for i in range(64):
            modified_input = flip_bit(input_value, i)
            modified_output = encrypt_function(modified_input)
            xor_result = original_output ^ modified_output

            for j in range(64):
                if xor_result & (1 << j):
                    sac_matrix[i][j] += 1

    return sac_matrix

def save_matrix_to_file(matrix, filename):
    np.savetxt(filename, matrix, fmt='%d')

def calculate_bin_probabilities(matrix):
    bins = [0, 523857, 524158, 524417, 524718, 1048576]
    bin_counts = [0] * (len(bins) - 1)
    total_values = matrix.size

    for value in matrix.flatten():
        for i in range(len(bins) - 1):
            if bins[i] <= value < bins[i + 1]:
                bin_counts[i] += 1
                break

    bin_probabilities = [count / total_values for count in bin_counts]
    return bin_probabilities

if __name__ == "__main__":
    print("SAC Matrix for AES:")
    sac_matrix_aes = calculate_sac(encrypt_aes)
    print(sac_matrix_aes)
    save_matrix_to_file(sac_matrix_aes, 'sac_matrix_aes.txt')
    aes_bin_probabilities = calculate_bin_probabilities(sac_matrix_aes)
    print("AES Bin Probabilities:", aes_bin_probabilities)

    print("\nSAC Matrix for DES:")
    sac_matrix_des = calculate_sac(encrypt_des)
    print(sac_matrix_des)
    save_matrix_to_file(sac_matrix_des, 'sac_matrix_des.txt')
    des_bin_probabilities = calculate_bin_probabilities(sac_matrix_des)
    print("DES Bin Probabilities:", des_bin_probabilities)