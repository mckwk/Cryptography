def read_sbox_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return data

def extract_boolean_functions(sbox_data):
    # Extract non-zero bytes (every other byte starting from index 0)
    non_zero_bytes = sbox_data[0::2]
    
    # 8-bit binary representation
    boolean_functions = [[] for _ in range(8)]
    
    for byte in non_zero_bytes:
        binary_repr = format(byte, '08b')  # Get binary string representation
        for i in range(8):
            boolean_functions[i].append(int(binary_repr[i]))
    
    return boolean_functions

if __name__ == "__main__":
    sbox_filename = "D:\Repos\Cryptography\S-box\sbox.SBX"  
    sbox_data = read_sbox_file(sbox_filename)
    boolean_functions = extract_boolean_functions(sbox_data)
