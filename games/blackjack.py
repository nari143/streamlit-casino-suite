import streamlit as st#type:ignore
import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def card_symbol(card):
    # Map card values to symbols (A, 2-10, J, Q, K)
    if card == 11:
        return 'A'
    elif card == 10:
        # Randomly pick a face card or 10 for variety
        return random.choice(['10', 'J', 'Q', 'K'])
    else:
        return str(card)

def render_hand(hand):
    # Render hand as a row of cards
    return ' '.join(f':black_joker: **{card_symbol(card)}**' for card in hand)

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def reset_blackjack():
    st.session_state['bj_player'] = [deal_card(), deal_card()]
    st.session_state['bj_dealer'] = [deal_card(), deal_card()]
    st.session_state['bj_bet'] = 0
    st.session_state['bj_active'] = True
    st.session_state['bj_result'] = ''
    st.session_state['bj_show_dealer'] = False

def blackjack_game():
    st.subheader("Blackjack 🃏")
    if 'bj_player' not in st.session_state:
        reset_blackjack()
    if 'bj_result' not in st.session_state:
        st.session_state['bj_result'] = ''
    if 'bj_show_dealer' not in st.session_state:
        st.session_state['bj_show_dealer'] = False

    if st.session_state['bj_active']:
        bet = st.number_input("Place your bet:", min_value=0.01, max_value=float(st.session_state['coins']), value=10.0, key='bj_bet_input')
        if st.button("Deal", key='bj_deal'):
            st.session_state['bj_bet'] = bet
            st.session_state['coins'] -= bet
            st.session_state['bj_active'] = False
            st.session_state['bj_result'] = ''
            st.session_state['bj_show_dealer'] = False
            st.rerun()
    else:
        player = st.session_state['bj_player']
        dealer = st.session_state['bj_dealer']
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)
        st.write(f"Your hand: {render_hand(player)} (Score: {player_score})")
        if st.session_state['bj_show_dealer']:
            st.write(f"Dealer's hand: {render_hand(dealer)} (Score: {dealer_score})")
        else:
            st.write(f"Dealer's hand: :black_joker: **{card_symbol(dealer[0])}** :black_joker: **?**")

        if st.session_state['bj_result']:
            st.write(st.session_state['bj_result'])
            if st.button("New Game", key='bj_new_game'):
                reset_blackjack()
                st.rerun()
        else:
            if st.button("Hit", key='bj_hit'):
                player.append(deal_card())
                player_score = calculate_score(player)
                if player_score > 21:
                    st.session_state['bj_result'] = "You busted! 💥"
                    st.session_state['bj_show_dealer'] = True
                st.rerun()
            if st.button("Stand", key='bj_stand'):
                while calculate_score(dealer) < 17:
                    dealer.append(deal_card())
                dealer_score = calculate_score(dealer)
                st.session_state['bj_show_dealer'] = True
                player_score = calculate_score(player)
                if dealer_score > 21 or player_score > dealer_score:
                    st.session_state['bj_result'] = "You win! 🎉"
                    st.session_state['coins'] += st.session_state['bj_bet'] * 2
                elif player_score == dealer_score:
                    st.session_state['bj_result'] = "Push! It's a tie."
                    st.session_state['coins'] += st.session_state['bj_bet']
                else:
                    st.session_state['bj_result'] = "Dealer wins! 😢"
                st.rerun() 