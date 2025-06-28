import streamlit as st#type:ignore
import sqlite3
import hashlib
import os

def get_db():
    conn = sqlite3.connect('users.db')
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        coins INTEGER
    )''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'username' not in st.session_state:
        st.session_state['username'] = None
    if 'coins' not in st.session_state:
        st.session_state['coins'] = 1000
    init_db()

def save_user_data():
    if st.session_state['logged_in'] and st.session_state['username']:
        conn = get_db()
        c = conn.cursor()
        c.execute('UPDATE users SET coins=? WHERE username=?', (st.session_state['coins'], st.session_state['username']))
        conn.commit()
        conn.close()

def login_page():
    # Custom CSS for bright input text and labels
    st.markdown(
        """
        <style>
        label, .stTextInput > div > div > input, .stPassword > div > div > input {
            color: #fff !important;
            background-color: #242526 !important;
        }
        .stTextInput > div > div > input, .stPassword > div > div > input {
            border: 1px solid #fff !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("🎰 Virtual Casino Login")
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            conn = get_db()
            c = conn.cursor()
            c.execute('SELECT password, coins FROM users WHERE username=?', (username,))
            row = c.fetchone()
            conn.close()
            if row and row[0] == hash_password(password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.session_state['coins'] = row[1]
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")
    
    with tab2:
        st.subheader("Register")
        new_username = st.text_input("Username", key="reg_username")
        new_password = st.text_input("Password", type="password", key="reg_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm")
        
        if st.button("Register"):
            if not new_username or not new_password:
                st.error("Username and password are required")
            elif new_password != confirm_password:
                st.error("Passwords do not match")
            else:
                conn = get_db()
                c = conn.cursor()
                c.execute('SELECT username FROM users WHERE username=?', (new_username,))
                if c.fetchone():
                    st.error("Username already exists")
                else:
                    c.execute('INSERT INTO users (username, password, coins) VALUES (?, ?, ?)',
                              (new_username, hash_password(new_password), 1000))
                    conn.commit()
                    st.success("Registration successful! Please login.")
                conn.close() 