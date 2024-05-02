import streamlit as st
from cryptography.fernet import Fernet

# Functions to generate a key, encrypt, and decrypt
def generate_fernet_key():
    return Fernet.generate_key()

def encrypt_with_fernet(key, message):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_with_fernet(key, encrypted_message):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

# Streamlit app layout
st.title("Fernet Encryption and Decryption")

# Generate a Fernet key
if st.button("Generate Fernet Key"):
    fernet_key = generate_fernet_key()
    st.session_state['fernet_key'] = fernet_key
    st.success("Fernet key generated!")
    st.write("Fernet Key:", fernet_key.decode())

# Encrypt message
if 'fernet_key' in st.session_state:
    message = st.text_input("Enter a message to encrypt:")
    if message and st.button("Encrypt"):
        encrypted_message = encrypt_with_fernet(st.session_state['fernet_key'], message)
        st.session_state['encrypted_message'] = encrypted_message
        st.success("Message encrypted!")
        st.write("Encrypted Message:", encrypted_message)

# Decrypt message
if 'encrypted_message' in st.session_state:
    if st.button("Decrypt"):
        decrypted_message = decrypt_with_fernet(st.session_state['fernet_key'], st.session_state['encrypted_message'])
        st.success("Message decrypted!")
        st.write("Decrypted Message:", decrypted_message)
