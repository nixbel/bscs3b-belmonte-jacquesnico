import streamlit as st

st.set_page_config(
    page_title = "Block Cipher", page_icon="🔐",layout = "wide")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_primitive_root(g, q):
    residues = set()
    for i in range(1, q):
        residue = pow(g, i, q)
        if residue in residues:
            return False
        residues.add(residue)
    return len(residues) == q - 1

def find_primitive_roots(q):
    primitive_roots = []
    for g in range(1, q):
        if is_primitive_root(g, q):
            primitive_roots.append(g)
    return primitive_roots

def display_output(q, g):
    if not is_prime(q):
        st.write(f"{q} is not a prime number!!")
    else:
        st.write("1^1 mod", q, "= 1|")
        for i in range(2, q):
            output = f"{i}^1 mod {q} = {pow(i, 1, q)}|"
            for j in range(2, q):
                residue = pow(i, j, q)
                if residue == 1:
                    output += f"{i}^{j} mod {q} = {residue}|"
                    break
                output += f"{i}^{j} mod {q} = {residue}|"
            if is_primitive_root(i, q):
                output += f" ==> {i} is primitive root of {q}"
                output = output.replace("| ==> ", " ==> ")
            st.write(output)

        primitive_roots = find_primitive_roots(q)
        if g not in primitive_roots:
            st.write(f"{g} is NOT primitive root of {q} - List of Primitive roots: {primitive_roots}")
        else:
            st.write(f"{g} is primitive root: {g in primitive_roots} {primitive_roots}")
st.title("Primitive Root.")
q_input = st.text_input("Enter a prime number (q):")
g_input = st.text_input("Enter a generator (g):")
submit_button = st.button("Submit")

if submit_button:
    display_output(int(q_input), int(g_input))
