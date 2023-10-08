import streamlit as st
import random

# Function to determine if the background color is dark
def is_dark_color(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    return brightness < 128

text_color_markdown = "#33CC33"  # Bright Green
equation_style = f"color: {text_color_markdown}; font-size: 3em;"

st.title('Learn Plus and Minus!')

# Initialize the session state
if 'number_1' not in st.session_state:
    st.session_state.number_1 = random.randint(1, 10)
    st.session_state.number_2 = random.randint(1, 10)  # Initialize number_2 here
    st.session_state.operation = "Plus"  # Default to "Plus"
    st.session_state.correct = 0
    st.session_state.attempts = 0
    st.session_state.show_next_button = False

# Option to choose between "Plus" and "Minus"
st.session_state.operation = st.radio("Choose an operation:", ["Plus", "Minus"])

# Display the math statement in a larger font size directly below the radio button
if st.session_state.operation == "Minus":
    st.markdown(f"<div style='{equation_style}'>{st.session_state.number_1} - {st.session_state.number_2} = ?</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div style='{equation_style}'>{st.session_state.number_1} + {st.session_state.number_2} = ?</div>", unsafe_allow_html=True)

MAX_BLOCKS = 10

# Display number_1 blocks
st.write(f"{st.session_state.number_1} blocks:")
cols1 = st.columns(MAX_BLOCKS)
for i in range(st.session_state.number_1):
    cols1[i].image('blue-square-png-13.png', width=50, use_column_width=False)

if st.session_state.operation == "Minus":
    st.write(f"Minus {st.session_state.number_2} blocks:")
    cols2 = st.columns(MAX_BLOCKS)
    for i in range(st.session_state.number_2):
        cols2[i].image('red-square-png-14.png', width=50, use_column_width=False)
else:  # For the "Plus" operation
    st.write(f"Plus {st.session_state.number_2} blocks:")
    cols3 = st.columns(MAX_BLOCKS)
    for i in range(st.session_state.number_2):
        cols3[i].image('blue-square-png-13.png', width=50, use_column_width=False)

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
        st.experimental_rerun()  # Force the app to re-run

st.write(f"You have answered correctly {st.session_state.correct} out of {st.session_state.attempts} attempts.")