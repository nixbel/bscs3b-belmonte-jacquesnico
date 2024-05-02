import streamlit as st
import random
from math import gcd

# Helper function to calculate modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        # q is quotient
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


# Helper function to generate a large prime number
def generate_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits)
        if prime_candidate % 2 == 0:
            prime_candidate += 1
        if is_prime(prime_candidate):
            return prime_candidate


# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Function to generate RSA key pair
def generate_rsa_key_pair(bits=1024):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Common choice for RSA
    d = modinv(e, phi)

    return (e, n), (d, n)  # Public key, private key


# Function to encrypt a message with RSA
def encrypt_with_rsa(public_key, message):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted


# Function to decrypt an encrypted message with RSA
def decrypt_with_rsa(private_key, encrypted_message):
    d, n = private_key
    decrypted = "".join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted


# Streamlit App
st.title("RSA Encryption/Decryption with Streamlit")

# Generate RSA key pair
public_key, private_key = generate_rsa_key_pair()

# User input for the message to encrypt
message = st.text_area("Enter a message for RSA encryption:")

# Button to trigger encryption and decryption
if st.button("Encrypt & Decrypt"):
    # Encrypt the message
    encrypted_message = encrypt_with_rsa(public_key, message)
    encrypted_message_str = ' '.join(map(str, encrypted_message))  # Display encrypted message
    
    # Decrypt the message
    decrypted_message = decrypt_with_rsa(private_key, encrypted_message)
    
    # Display encrypted and decrypted messages
    st.write("Encrypted Message:", encrypted_message_str)
    st.write("Decrypted Message:", decrypted_message)
