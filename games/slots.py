import streamlit as st#type:ignore
import random

def slots_game():
    st.subheader("Slots 🎰")
    bet = st.number_input("Place your bet:", min_value=0.01, max_value=float(st.session_state['coins']), value=10.0, key='slots_bet_input')
    if st.button("Spin", key='slots_spin'):
        st.session_state['coins'] -= bet
        symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]
        result = [random.choice(symbols) for _ in range(3)]
        st.write(f"Result: {' | '.join(result)}")
        if result[0] == result[1] == result[2]:
            st.write("Jackpot! You win 10x your bet! 🎉")
            st.session_state['coins'] += bet * 10
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            st.write("Two matched! You win 2x your bet!")
            st.session_state['coins'] += bet * 2
        else:
            st.write("No match. You lost! 😢") 