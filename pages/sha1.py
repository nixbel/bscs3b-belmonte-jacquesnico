import streamlit as st
import hashlib

st.set_page_config(
    page_title = "Block Cipher", page_icon="🔐",layout = "wide")

# Function to hash the text and display individual character hashes
def hash_text(text):
    hashed_chars = {}
    space = False
    output = []

    for char in text:
        if char == " ":
            if not space:
                space = True
                space_hashvalue = "5c1ce938ec4b836703c845a1d8db57348758f283"
                output.append(f"{space_hashvalue.upper()} <space>")
            continue
        if char not in hashed_chars:
            hash_text_obj = hashlib.sha1()
            hash_text_obj.update(char.encode())
            hash_value = hash_text_obj.hexdigest()
            hashed_chars[char] = hash_value
            output.append(f"{hash_value.upper()} {char}")
            
    hash_text_obj = hashlib.sha1()
    hash_text_obj.update(text.encode())
    hash_value = hash_text_obj.hexdigest()
    output.append(f"{hash_value.upper()} {text}")
    
    return output

# Streamlit app
def main():
    st.title("Text Hasher with SHA-1")
    
    # Create a text box for user input
    user_text = st.text_input("Enter your text:")
    
    if user_text:
        # Get the hashed results
        results = hash_text(user_text)
        
        # Display the results
        st.write("Hash results:")
        for res in results:
            st.write(res)

# Run the app
if __name__ == "__main__":
    main()
