import streamlit as st
import random
import base64

text_color_markdown = "#33CC33"  # Bright Green
equation_style = f"color: {text_color_markdown}; font-size: 3em;"

st.title('Learn Plus and Minus!')

# Initialize the session state
if 'number_1' not in st.session_state:
    st.session_state.number_1 = random.randint(1, 10)
    st.session_state.number_2 = random.randint(1, 10)
    st.session_state.operation = "Plus"
    st.session_state.correct = 0
    st.session_state.attempts = 0
    st.session_state.show_next_button = False

# Option to choose between "Plus" and "Minus"
st.session_state.operation = st.radio("Choose an operation:", ["Plus", "Minus"])

# Adjust number_2 for minus operation
if st.session_state.operation == "Minus" and st.session_state.number_2 >= st.session_state.number_1:
    st.session_state.number_2 = random.randint(1, st.session_state.number_1)

# Display the math statement in a larger font size directly below the radio button
if st.session_state.operation == "Minus":
    st.markdown(f"<div style='{equation_style}'>{st.session_state.number_1} - {st.session_state.number_2} = ?</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div style='{equation_style}'>{st.session_state.number_1} + {st.session_state.number_2} = ?</div>", unsafe_allow_html=True)

def display_blocks(count, image_path, text):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    blocks_html = ''.join([f"<img src='data:image/png;base64,{b64_string}' style='width:50px; margin-right:5px;' />" for _ in range(count)])
    st.markdown(f"{text}<br>{blocks_html}", unsafe_allow_html=True)

# Display number_1 blocks
display_blocks(st.session_state.number_1, 'blue-square-png-13.png', f"{st.session_state.number_1} blocks:")

if st.session_state.operation == "Minus":
    display_blocks(st.session_state.number_2, 'red-square-png-14.png', f"Minus {st.session_state.number_2} blocks:")
else:
    display_blocks(st.session_state.number_2, 'blue-square-png-13.png', f"Plus {st.session_state.number_2} blocks:")

# Get user answer
answer = st.number_input('What is the answer?', value=0, step=1, min_value=0)

# Check if the answer is correct only when the button is pressed
if st.button("Check Answer"):
    if st.session_state.operation == "Plus":
        correct_answer = st.session_state.number_1 + st.session_state.number_2
    else:
        correct_answer = st.session_state.number_1 - st.session_state.number_2

    st.session_state.attempts += 1
    if answer == correct_answer:
        st.markdown("<h2 style='font-weight: bold;'>Correct!</h2>", unsafe_allow_html=True)
        st.session_state.correct += 1
        st.session_state.show_next_button = True
    else:
        st.markdown("<h2 style='font-weight: bold;'>Wrong! Try again!</h2>", unsafe_allow_html=True)

if st.session_state.show_next_button:
    if st.button("Next"):
        st.session_state.number_1 = random.randint(1, 10)
        if st.session_state.operation == "Minus" and st.session_state.number_1 > 1:
            st.session_state.number_2 = random.randint(1, st.session_state.number_1 - 1)
        else:
            st.session_state.number_2 = random.randint(1, 10)
        st.session_state.show_next_button = False
        st.experimental_rerun()

st.write(f"You have answered correctly {st.session_state.correct} out of {st.session_state.attempts} attempts.")
