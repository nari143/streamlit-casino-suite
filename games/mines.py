import streamlit as st#type:ignore
import random
import math

def get_cashout_multiplier(mines, diamonds_found, grid_size=5):
    # Progressive, risk-based multiplier
    total_cells = grid_size * grid_size
    if diamonds_found == 0:
        return 0
    base = 1 + (mines / (total_cells - mines))  # base increase per diamond
    multiplier = 1.0
    for i in range(diamonds_found):
        multiplier *= base
    # House edge: reduce slightly
    return round(multiplier * (1.0 - 0.01 * mines), 2)

def mines_game():
    st.subheader("Mines 💣💎")
    grid_size = 5
    total_cells = grid_size * grid_size

    if 'mines_active' not in st.session_state or st.session_state.get('mines_reset', False):
        st.session_state['mines_active'] = False
        st.session_state['mines_reset'] = False

    if not st.session_state['mines_active']:
        bet = st.number_input("Place your bet:", min_value=0.01, max_value=float(st.session_state['coins']), value=10.0, key='mines_bet_input')
        num_mines = st.slider("Number of Mines (Bombs):", min_value=1, max_value=total_cells-1, value=3, key='mines_num_mines')
        if st.button("Start Game", key='mines_start'):
            cells = [(i, j) for i in range(grid_size) for j in range(grid_size)]
            mines = set(random.sample(cells, num_mines))
            st.session_state['mines_mines'] = mines
            st.session_state['mines_revealed'] = set()
            st.session_state['mines_diamonds'] = set(cells) - mines
            st.session_state['mines_bet'] = bet
            st.session_state['mines_num_mines_game'] = num_mines
            st.session_state['mines_active'] = True
            st.session_state['coins'] -= bet
            st.session_state['mines_lost'] = False
            st.session_state['mines_cashout'] = 0
            st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()
        return

    bet = st.session_state['mines_bet']
    num_mines = st.session_state['mines_num_mines_game']
    mines = st.session_state['mines_mines']
    revealed = st.session_state['mines_revealed']
    diamonds = st.session_state['mines_diamonds']
    lost = st.session_state['mines_lost']
    diamonds_found = len([cell for cell in revealed if cell in diamonds])
    cashout_multiplier = get_cashout_multiplier(num_mines, diamonds_found, grid_size)
    cashout_value = math.floor(bet * cashout_multiplier)

    st.write(f"Bet: **{bet}** | Mines: **{num_mines}** | Diamonds found: **{diamonds_found}** | Potential Cashout: **{cashout_value} coins**")

    for i in range(grid_size):
        cols = st.columns(grid_size)
        for j in range(grid_size):
            cell = (i, j)
            if cell in revealed:
                if cell in mines:
                    cols[j].markdown('<span style="font-size:2em;">💣</span>', unsafe_allow_html=True)
                else:
                    cols[j].markdown('<span style="font-size:2em;">💎</span>', unsafe_allow_html=True)
            elif not lost and st.session_state['mines_active']:
                if cols[j].button(" ", key=f"mines_{i}_{j}"):
                    if cell in mines:
                        st.session_state['mines_revealed'].add(cell)
                        st.session_state['mines_lost'] = True
                        st.error("Boom! You hit a bomb and lost your bet.")
                        st.session_state['mines_active'] = False
                        st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()
                    else:
                        st.session_state['mines_revealed'].add(cell)
                        st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()
            else:
                cols[j].markdown('<span style="font-size:2em;">⬜</span>', unsafe_allow_html=True)

    if not lost and st.session_state['mines_active'] and diamonds_found > 0:
        if st.button(f"💰 Cash Out {cashout_value} coins", key='mines_cashout'):
            st.session_state['coins'] += cashout_value
            st.success(f"You cashed out {cashout_value} coins!")
            st.session_state['mines_active'] = False
            st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()

    if not st.session_state['mines_active']:
        if st.button("New Game", key='mines_new_game'):
            st.session_state['mines_reset'] = True
            st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun() 