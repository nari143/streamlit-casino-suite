import streamlit as st#type:ignore
import random

def hilo_game():
    st.subheader("High-Low 🃏")
    if 'hilo_card' not in st.session_state:
        st.session_state['hilo_card'] = random.randint(2, 14)
    bet = st.number_input("Place your bet:", min_value=0.01, max_value=st.session_state['coins'], value=10.0, key='hilo_bet_input')
    st.write(f"Current card: {st.session_state['hilo_card']}")
    guess = st.radio("Will the next card be higher or lower?", ["Higher", "Lower"], key='hilo_guess_input')
    if st.button("Draw Card", key='hilo_draw'):
        st.session_state['coins'] -= bet
        next_card = random.randint(2, 14)
        st.write(f"Next card: {next_card}")
        if (guess == "Higher" and next_card > st.session_state['hilo_card']) or (guess == "Lower" and next_card < st.session_state['hilo_card']):
            st.write("You win! 🎉")
            st.session_state['coins'] += bet * 2
        elif next_card == st.session_state['hilo_card']:
            st.write("It's a tie! You get your bet back.")
            st.session_state['coins'] += bet
        else:
            st.write("You lost! 😢")
        st.session_state['hilo_card'] = next_card 