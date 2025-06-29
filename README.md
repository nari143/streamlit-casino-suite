# Casino Logic Suite

An interactive web application featuring multiple casino-style games, built with Streamlit, probability-based logic, and SQLite database for persistent user management.

## Features

- Play classic casino games: Blackjack, Dice, Roulette, Coin Flip, Slots, High-Low, Mines, and IPL Betting.
- User authentication with registration and login.
- Persistent coin balance and statistics for each user.
- Borrow coins if your balance runs out.
- Modern dark-themed UI with real-time feedback.

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **Python**: Core language for all game and backend logic.
- **SQLite**: Lightweight database for user management and persistent storage.
- **Probability & Game Logic**: Ensures fair, mathematically sound outcomes.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nari143/streamlit-casino-suite.git
   cd gamble
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** Streamlit >=1.10.0 is recommended for best compatibility.

3. **(Optional) Delete `users.db`** if you want to reset all user data.

## Running the Application

1. **Start the app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser:**  
   Go to the local URL shown in the terminal (usually http://localhost:8501).

3. **Register or log in:**  
   - New users: Register with a username and password.
   - Existing users: Log in to continue with your saved coins and stats.

4. **Play games:**  
   - Choose a game from the sidebar.
   - Place bets, play, and see your coin balance update in real time.
   - If you run out of coins, use the "Borrow 1000 Coins" button to keep playing.

5. **Logout:**  
   Use the sidebar button to log out and save your progress.

## File Structure

- `app.py` – Main Streamlit app, handles navigation and session.
- `games/` – Contains logic for each casino game.
- `users.py` – User authentication, session, and database management.
- `users.db` – SQLite database file (auto-created on first run).
- `requirements.txt` – Python dependencies.

## Customization

- Add or modify games in the `games/` directory.
- Adjust starting coins or game rules in the respective Python files.

## License

This project is for educational and entertainment purposes. 
