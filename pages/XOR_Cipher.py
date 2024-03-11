import streamlit as st

st.set_page_config(
    page_title = "Block Cipher", page_icon="🔐",layout = "wide")

def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, printing bits involved."""

    ciphertext = bytearray()
    for i in range(len(plaintext)):
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]
        xor_result = plaintext_byte ^ key_byte
        ciphertext.append(xor_result)
        st.write(f"Plaintext byte: {bin(plaintext_byte)[2:]:>08} = {chr(plaintext_byte)}")
        st.write(f"Key byte:       {bin(key_byte)[2:]:>08} = {chr(key_byte)}")
        st.write(f"XOR result:     {bin(xor_result)[2:]:>08} = {chr(xor_result)}")
        st.write("-" * 20)
    
    return ciphertext

def xor_decrypt(ciphertext, key):
    """Decrypts ciphertext using XOR cipher with the given key."""
    decrypt_text = ''
    for i in range(len(ciphertext)):
        ciphertext_byte = ciphertext[i]
        key_byte = key[i % len(key)]
        xor_result = ciphertext_byte ^ key_byte
        decrypt_text += chr(xor_result)
        
        st.write(f"Plaintext byte: {bin(ciphertext_byte)[2:]:>08} = {chr(ciphertext_byte)}")
        st.write(f"Key byte:       {bin(key_byte)[2:]:>08} = {chr(key_byte)}")
        st.write(f"XOR result:     {bin(xor_result)[2:]:>08} = {chr(xor_result)}")
        st.write("-" * 20)
    
    return decrypt_text

# Input fields for plaintext and key
st.title("XOR Cipher.")
plaintext_input = st.text_input("Enter plaintext:")
key_input = st.text_input("Enter key:")

# Submit button
if st.button("Submit"):
    if len(plaintext_input) >= 1 and len(key_input) >= 1:
        plaintext = bytes(plaintext_input.encode())
        key = bytes(key_input.encode())

        if plaintext != key:
            ciphertext = xor_encrypt(plaintext, key)
            st.write(f"Ciphertext: {''.join([chr(byte_value) for byte_value in ciphertext])}")
            decrypted_text = xor_decrypt(ciphertext, key)
            st.write(f"Decrypted: {decrypted_text}")
        else: 
            st.write("Plaintext should not be equal to the key")
    else:
        st.write("Plaintext length should be equal or greater than the length of key")
