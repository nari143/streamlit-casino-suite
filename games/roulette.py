import streamlit as st#type:ignore
import random

ROULETTE_NUMBERS = list(range(37))  # 0-36
RED_NUMBERS = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
BLACK_NUMBERS = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}

BET_TYPES = [
    'Single Number', 'Red', 'Black', 'Even', 'Odd',
    '1 to 18', '19 to 36', '1st 12', '2nd 12', '3rd 12',
    '1st Column', '2nd Column', '3rd Column'
]

PROBABILITIES = {
    'Single Number': 1/37,
    'Red': 18/37,
    'Black': 18/37,
    'Even': 18/37,
    'Odd': 18/37,
    '1 to 18': 18/37,
    '19 to 36': 18/37,
    '1st 12': 12/37,
    '2nd 12': 12/37,
    '3rd 12': 12/37,
    '1st Column': 12/37,
    '2nd Column': 12/37,
    '3rd Column': 12/37
}

# Helper to check if a number matches a bet type
def matches_bet(number, bet_type, bet_number=None):
    if bet_type == 'Single Number':
        return number == bet_number
    if bet_type == 'Red':
        return number in RED_NUMBERS
    if bet_type == 'Black':
        return number in BLACK_NUMBERS
    if bet_type == 'Even':
        return number != 0 and number % 2 == 0
    if bet_type == 'Odd':
        return number % 2 == 1
    if bet_type == '1 to 18':
        return 1 <= number <= 18
    if bet_type == '19 to 36':
        return 19 <= number <= 36
    if bet_type == '1st 12':
        return 1 <= number <= 12
    if bet_type == '2nd 12':
        return 13 <= number <= 24
    if bet_type == '3rd 12':
        return 25 <= number <= 36
    if bet_type == '1st Column':
        return number != 0 and number % 3 == 1
    if bet_type == '2nd Column':
        return number != 0 and number % 3 == 2
    if bet_type == '3rd Column':
        return number != 0 and number % 3 == 0
    return False

def roulette_table_html():
    # Zero cell separate on the left, then 12 rows of 3 numbers
    table_html = "<div style='display:flex;align-items:flex-start;'>"
    # Zero column
    table_html += "<div><table style='border-collapse:collapse;'><tr>"
    table_html += "<td style='background:#4caf50;color:white;text-align:center;font-weight:bold;width:40px;height:120px;vertical-align:middle;font-size:1.5em;'>0</td>"
    table_html += "</tr></table></div>"
    # Main grid
    table_html += "<div><table style='border-collapse:collapse;'>"
    for row in range(12):
        table_html += "<tr>"
        for col in range(3):
            num = row*3 + col + 1
            color = '#e53935' if num in RED_NUMBERS else '#333'
            table_html += f"<td style='background:{color};color:white;text-align:center;width:40px;height:40px;font-size:1.2em;'>{num}</td>"
        table_html += "</tr>"
    table_html += "</table></div>"
    table_html += "</div>"
    return table_html

def roulette_game():
    st.subheader("Roulette 🎡")
    col1, col2 = st.columns([2,3])
    with col1:
        bet_type = st.selectbox("Bet Type", BET_TYPES)
        bet_number = None
        if bet_type == 'Single Number':
            bet_number = st.number_input("Choose a number (0-36)", min_value=0, max_value=36, value=0, key='roulette_number_input')
        bet = st.number_input("Place your bet:", min_value=0.01, max_value=float(st.session_state['coins']), value=10.0, key='roulette_bet_input')
        if st.button("Spin Wheel", key='roulette_spin'):
            st.session_state['coins'] -= bet
            result = random.choice(ROULETTE_NUMBERS)
            st.write(f"The ball landed on: **{result}**")
            win = matches_bet(result, bet_type, bet_number)
            prob = PROBABILITIES[bet_type] if bet_type != 'Single Number' else 1/37
            payout_multiplier = round(1/prob)
            if win:
                payout = bet * payout_multiplier
                st.write(f"You win! 🎉 Payout: {payout} coins (odds: {payout_multiplier}x)")
                st.session_state['coins'] += payout
            else:
                st.write("You lost! 😢")
    with col2:
        st.markdown("Roulette Table Preview:")
        st.markdown(roulette_table_html(), unsafe_allow_html=True) 