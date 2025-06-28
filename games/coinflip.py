import streamlit as st#type:ignore
import random

def coinflip_game():
    st.subheader("Coin Flip 🪙")
    bet = st.number_input("Place your bet:", min_value=0.01, max_value=float(st.session_state['coins']), value=10.0, key='coinflip_bet_input')
    choice = st.selectbox("Bet on:", ["Heads", "Tails"], key='coinflip_choice_input')
    if st.button("Flip Coin", key='coinflip_flip'):
        st.session_state['coins'] -= bet
        result = random.choice(["Heads", "Tails"])
        st.write(f"The coin landed on: {result}")
        if result == choice:
            st.write("You win! 🎉")
            st.session_state['coins'] += bet * 2
        else:
            st.write("You lost! 😢") 