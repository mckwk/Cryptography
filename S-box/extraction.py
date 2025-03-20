import numpy as np

def read_sbox_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return data

def extract_boolean_functions(sbox_data):
    # Ensure the file contains 512 bytes
    assert len(sbox_data) == 512, "Invalid file size. Expected 512 bytes."
    
    # Extract non-zero bytes (every other byte starting from index 0)
    non_zero_bytes = sbox_data[0::2]
    assert len(non_zero_bytes) == 256, "Incorrect number of non-zero bytes."
    
    # Convert each byte into an 8-bit binary representation
    boolean_functions = [[] for _ in range(8)]
    
    for byte in non_zero_bytes:
        binary_repr = format(byte, '08b')  # Get binary string representation
        for i in range(8):
            boolean_functions[i].append(int(binary_repr[i]))
    
    return boolean_functions

def verify_balance(boolean_functions):
    for i, func in enumerate(boolean_functions):
        ones = sum(func)
        zeros = len(func) - ones
        print(f"Function F{i+1}: 1s = {ones}, 0s = {zeros}, Balanced: {ones == zeros}")

if __name__ == "__main__":
    sbox_filename = "D:\Repos\Cryptography\S-box\sbox.SBX"  
    sbox_data = read_sbox_file(sbox_filename)
    boolean_functions = extract_boolean_functions(sbox_data)
    verify_balance(boolean_functions)
