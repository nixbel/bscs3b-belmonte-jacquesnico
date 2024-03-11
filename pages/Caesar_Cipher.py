import streamlit as st

st.set_page_config(
    page_title = "Block Cipher", page_icon="🔐",layout = "wide")

def caesar_cipher(char, shift):
    if char.isalpha():
        if char.islower():
            return chr((ord(char) + shift - 32 + 94) % 94 + 32)
        else:
            return chr((ord(char) + shift - 32 + 94) % 94 + 32)
    else:
        return chr((ord(char) + shift - 32 + 94) % 94 + 32)

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    result = ''
    details = []
    for i, char in enumerate(text):
        shift = shift_keys[i % len(shift_keys)]
        if ifdecrypt:
            shift = -shift
        result_char = caesar_cipher(char, shift)
        details.append((char, shift, result_char))
        result += result_char
    return result, details

def display_encryption_decryption_details(details):
    for i, (char, shift, result_char) in enumerate(details):
        st.write(f"{i} {char} {shift} {result_char}")

def main():
    st.title("Caesar Cipher.")

    text = st.text_input("Enter text to encrypt/decrypt:")
    shift_keys_input = st.text_input("Enter shift keys (comma-separated):")

    if st.button("Submit"):
        shift_keys = list(map(int, shift_keys_input.split(',')))

        st.write("--- Encryption ---")
        encrypted_text, details_encrypt = encrypt_decrypt(text, shift_keys, False)
        display_encryption_decryption_details(details_encrypt)
        st.write("-" * 10)

        st.write("--- Decryption ---")
        decrypted_text, details_decrypt = encrypt_decrypt(encrypted_text, shift_keys, True)
        display_encryption_decryption_details(details_decrypt)
        st.write("-" * 10)

        st.write("Text:", text)
        st.write("Shift keys:", " ".join(map(str, shift_keys)))
        st.write("Cipher:", encrypted_text)
        st.write("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
