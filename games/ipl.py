import streamlit as st#type:ignore
import random

def ipl_game():
    st.subheader("IPL Match Betting 🏏")
    teams = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore", "Kolkata Knight Riders"]
    team1, team2 = random.sample(teams, 2)
    st.write(f"Today's Match: **{team1}** vs **{team2}**")
    bet_team = st.radio("Which team do you want to bet on?", [team1, team2], key='ipl_bet_team')
    bet = st.number_input("Place your bet:", min_value=0.01, max_value=float(st.session_state['coins']), value=10.0, key='ipl_bet_input')
    if st.button("Place Bet & Simulate Match", key='ipl_bet_btn'):
        st.session_state['coins'] -= bet
        winner = random.choice([team1, team2])
        st.write(f"The match is over! Winner: **{winner}**")
        if bet_team == winner:
            st.success(f"Congratulations! You won {bet*2} coins!")
            st.session_state['coins'] += bet * 2
        else:
            st.error("You lost the bet! Better luck next time.") 