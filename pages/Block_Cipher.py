import streamlit as st

st.set_page_config(
    page_title = "Block Cipher", page_icon="🔐",layout = "wide")

def pad(data, block_size):    
    padding_length = block_size - len(data) % block_size  
    padding = bytes([padding_length] * padding_length)  
    return data + padding                       

def unpad(data):
    padding_length = data[-1]     
    return data[:-padding_length]                         # Return the data without the padding

def xor_encrypt_block(plaintext_block, key):
    encrypted_block = b''
    for i in range(len(plaintext_block)):
        encrypted_block += bytes([plaintext_block[i] ^ key[i % len(key)]])
    return encrypted_block                 

def xor_decrypt_block(ciphertext_block, key):
    return xor_encrypt_block(ciphertext_block, key)  # XOR decryption is same as encryption

def xor_encrypt(plaintext, key, block_size):
    encrypted_data = b''
    padded_plaintext = pad(plaintext, block_size)
    st.write("Encrypted blocks")
    for x, i in enumerate(range(0, len(padded_plaintext), block_size)):
        plaintext_block = padded_plaintext[i:i+block_size]
        st.write(f"Plain  block[{x}]: {plaintext_block.hex()} : {plaintext_block}")
        encrypted_block = xor_encrypt_block(plaintext_block, key)
        encrypted_data += encrypted_block
        st.write(f"Cipher block[{x}]: {encrypted_block.hex()} : {encrypted_block}")
    return encrypted_data                          

def xor_decrypt(ciphertext, key, block_size):
    decrypted_data = b''
    st.write("Decrypted blocks")
    for x, i in enumerate(range(0, len(ciphertext), block_size)):
        ciphertext_block = ciphertext[i:i+block_size]
        decrypted_block = xor_decrypt_block(ciphertext_block, key)
        decrypted_data += decrypted_block
        st.write(f"block[{x}]: {decrypted_block.hex()}: {decrypted_block}")
    unpadded_decrypted_data = unpad(decrypted_data)
    return unpadded_decrypted_data                 

if __name__ == "__main__":
    
    st.title("Block Cipher - XOR ")
    plaintext = st.text_input("Enter plaintext: ").encode()
    key_input = st.text_input("Enter key: ")
    key = key_input.encode() if key_input else b''  # Encoding only if key is non-empty
    block_size_input = st.text_input("Enter block size: ")
    block_size = int(block_size_input) if block_size_input.isdigit() else None
    if block_size not in [8, 16, 32, 64, 128]:
        st.write("Block size must be one of 8, 16, 32, 64, or 128 bytes")
    else:
        key = pad(key, block_size)
        encrypted_data = xor_encrypt(plaintext, key, block_size)
        decrypted_data = xor_decrypt(encrypted_data, key, block_size)
        st.write("\nOriginal plaintext:", plaintext)
        st.write("Key byte      :" , key)
        st.write("Key hex       :", key.hex())
        st.write("Encrypted data:", encrypted_data.hex())
        st.write("Decrypted data:", decrypted_data.hex())
        st.write("Decrypted data:", decrypted_data)
