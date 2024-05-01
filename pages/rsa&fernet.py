import streamlit as st
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


# Fernet Functions
def generate_fernet_key():
    return Fernet.generate_key()


def encrypt_with_fernet(key, message):
    f = Fernet(key)
    return f.encrypt(message.encode())


def decrypt_with_fernet(key, encrypted_message):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()


# RSA Functions
def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt_with_rsa(public_key, message):
    return public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def decrypt_with_rsa(private_key, encrypted_message):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    ).decode()


def main():
    st.title("Streamlit Encryption Demonstration")

    # Fernet Section
    st.header("Fernet Encryption/Decryption")
    fernet_key = generate_fernet_key()

    fernet_message = st.text_input("Enter a message to encrypt with Fernet")
    if fernet_message:
        fernet_encrypted = encrypt_with_fernet(fernet_key, fernet_message)
        fernet_decrypted = decrypt_with_fernet(fernet_key, fernet_encrypted)

        st.write("Fernet Encrypted Message:", fernet_encrypted)
        st.write("Fernet Decrypted Message:", fernet_decrypted)

    # RSA Section
    st.header("RSA Encryption/Decryption")
    private_key, public_key = generate_rsa_key_pair()

    rsa_message = st.text_input("Enter a message to encrypt with RSA")
    if rsa_message:
        rsa_encrypted = encrypt_with_rsa(public_key, rsa_message)
        rsa_decrypted = decrypt_with_rsa(private_key, rsa_encrypted)

        st.write("RSA Encrypted Message:", rsa_encrypted)
        st.write("RSA Decrypted Message:", rsa_decrypted)


if __name__ == "__main__":
    main()
