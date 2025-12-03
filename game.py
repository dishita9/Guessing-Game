import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize the secret number in session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

if "message" not in st.session_state:
    st.session_state.message = ""

st.write("I'm thinking of a number between 1 and 100. Try to guess!")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    secret = st.session_state.secret_number

    if guess < secret:
        st.session_state.message = "🔼 Too low! Try again."
    elif guess > secret:
        st.session_state.message = "🔽 Too high! Try again."
    else:
        st.session_state.message = "🎉 Correct! Click *Restart* to play again."

st.write(st.session_state.message)

if st.button("Restart"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.message = "Game restarted! Guess a new number."

