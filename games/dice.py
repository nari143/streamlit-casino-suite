import streamlit as st#type:ignore
import random

def dice_game():
    st.subheader("Dice Game 🎲")
    # Slider for win chance (1-100)
    win_chance = st.slider("Win Chance (%)", min_value=1, max_value=100, value=50, step=1)
    multiplier = round(100 / win_chance, 4)
    roll_over = 100 - win_chance
    bet = st.number_input("Bet Amount", min_value=0.01, max_value=float(st.session_state['coins']), value=10.0, key='dice_bet_input')
    profit_on_win = round(multiplier * bet - bet, 2)

    st.markdown(f"**Multiplier:** {multiplier}x")
    st.markdown(f"**Roll Over:** {roll_over:.2f}")
    st.markdown(f"**Win Chance:** {win_chance:.4f}%")
    st.markdown(f"**Profit on Win:** {profit_on_win}")

    if st.button("Bet", key='dice_bet'):
        st.session_state['coins'] -= bet
        roll = random.uniform(0, 100)
        st.write(f"You rolled: **{roll:.2f}**")
        if roll < win_chance:
            st.success(f"You win! 🎉 Profit: {profit_on_win}")
            st.session_state['coins'] += bet + profit_on_win
        else:
            st.error("You lost! 😢") 