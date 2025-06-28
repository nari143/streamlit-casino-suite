import streamlit as st#type:ignore
from games.blackjack import blackjack_game
from games.dice import dice_game
from games.roulette import roulette_game
from games.coinflip import coinflip_game
from games.slots import slots_game
from games.hilo import hilo_game
from games.ipl import ipl_game
from games.mines import mines_game
from users import init_session_state, login_page, save_user_data

st.set_page_config(page_title="Virtual Casino", layout="centered")

# Set dark theme using Streamlit theme config
st.markdown(
    """
    <style>
    .stApp {
        background-color: #18191A;
        color: #E4E6EB;
    }
    .css-1v0mbdj, .css-1d391kg, .css-1cpxqw2, .css-1offfwp, .css-1lcbmhc, .css-1p05t8e {
        background-color: #242526 !important;
        color: #E4E6EB !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
init_session_state()

# Show login page if not logged in
if not st.session_state['logged_in']:
    login_page()
else:
    st.title("🎰 Virtual Casino")
    st.write(f"Welcome back, **{st.session_state['username']}**!")
    st.write(f"**Your Coins:** {st.session_state['coins']}")

    # Borrow coins option if coins are zero or negative
    if st.session_state['coins'] <= 0:
        st.warning("You have run out of coins! You can borrow more to keep playing, but your balance will be negative until you win it back.")
        if st.button("Borrow 1000 Coins"):
            st.session_state['coins'] += 1000.00
            save_user_data()
            st.experimental_rerun() if hasattr(st, 'experimental_rerun') else st.rerun()

    # Add logout button in sidebar
    if st.sidebar.button("Logout"):
        save_user_data()  # Save user's coins before logging out
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.rerun()

    game = st.sidebar.radio("Choose a game:", ["Blackjack", "Dice", "Roulette", "Coin Flip", "Slots", "High-Low", "Mines"])

    # Save user data after each game action
    if game == "Blackjack":
        st.header("Blackjack 🃏")
        if st.session_state['coins'] <= 0:
            st.warning("You are out of coins! Please borrow more to continue playing.")
        else:
            blackjack_game()
        save_user_data()
    elif game == "Dice":
        st.header("Dice Game 🎲")
        if st.session_state['coins'] <= 0:
            st.warning("You are out of coins! Please borrow more to continue playing.")
        else:
            dice_game()
        save_user_data()
    elif game == "Roulette":
        st.header("Roulette 🎡")
        if st.session_state['coins'] <= 0:
            st.warning("You are out of coins! Please borrow more to continue playing.")
        else:
            roulette_game()
        save_user_data()
    elif game == "Coin Flip":
        st.header("Coin Flip 🪙")
        if st.session_state['coins'] <= 0:
            st.warning("You are out of coins! Please borrow more to continue playing.")
        else:
            coinflip_game()
        save_user_data()
    elif game == "Slots":
        st.header("Slots 🎰")
        if st.session_state['coins'] <= 0:
            st.warning("You are out of coins! Please borrow more to continue playing.")
        else:
            slots_game()
        save_user_data()
    elif game == "High-Low":
        st.header("High-Low 🃏")
        if st.session_state['coins'] <= 0:
            st.warning("You are out of coins! Please borrow more to continue playing.")
        else:
            hilo_game()
        save_user_data()
    elif game == "IPL Betting":
        st.header("IPL Match Betting 🏏")
        if st.session_state['coins'] <= 0:
            st.warning("You are out of coins! Please borrow more to continue playing.")
        else:
            ipl_game()
        save_user_data()
    elif game == "Mines":
        st.header("Mines 💣💎")
        if st.session_state['coins'] <= 0:
            st.warning("You are out of coins! Please borrow more to continue playing.")
        else:
            mines_game()
        save_user_data() 