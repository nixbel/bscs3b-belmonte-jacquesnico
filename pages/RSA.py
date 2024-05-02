import streamlit as st
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def generate_rsa_key_pair():
    # Generate RSA public/private key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt_with_rsa(public_key, message):
    # Encrypt a message with RSA public key
    return public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def decrypt_with_rsa(private_key, encrypted_message):
    # Decrypt a message with RSA private key
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    ).decode()


# Streamlit App
st.title("RSA Encryption/Decryption with Streamlit")

# Generate RSA key pair
private_key, public_key = generate_rsa_key_pair()

# User input for the message to encrypt
message = st.text_area("Enter a message for RSA encryption:")

# Button to trigger encryption and decryption
if st.button("Encrypt & Decrypt"):
    # Encrypt the message
    encrypted_message = encrypt_with_rsa(public_key, message)
    encrypted_message_str = encrypted_message.hex()  # Display as hex for easier visualization
    
    # Decrypt the message
    decrypted_message = decrypt_with_rsa(private_key, encrypted_message)
    
    # Display encrypted and decrypted messages
    st.write("Encrypted Message (Hex):", encrypted_message_str)
    st.write("Decrypted Message:", decrypted_message)
