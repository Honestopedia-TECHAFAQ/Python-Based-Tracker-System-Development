import streamlit as st
import hashlib

users_db = {
    "testuser": {
        "password": hashlib.sha256("testpassword".encode()).hexdigest(),
        "name": "Test User"
    }
}

project_details = {
    "budget": 5000,
    "expenses": 2500,
    "remaining": 2500
}

def verify_password(stored_password, input_password):
    return stored_password == hashlib.sha256(input_password.encode()).hexdigest()

def login_page():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.session_state.logged_in = False
    st.title("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Login", key="login_button"):
        if username in users_db and verify_password(users_db[username]["password"], password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def project_page():
    if not st.session_state.get("logged_in", False):
        login_page()
        return
    
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Budget Overview", "Profile", "Logout"])
    
    if selection == "Budget Overview":
        budget_overview_page()
    elif selection == "Profile":
        profile_page()
    elif selection == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = None
        st.success("Logged out successfully")
        st.experimental_rerun()

def budget_overview_page():
    st.title("Budget Overview")
    st.image("https://www.example.com/budget_image.jpg", caption="Budget Tracker")
    st.subheader("Budget Summary")
    st.write(f"Total Budget: ${project_details['budget']}")
    st.write(f"Total Expenses: ${project_details['expenses']}")
    st.write(f"Remaining Budget: ${project_details['remaining']}")
    st.write("\n")
    st.subheader("Expenses Chart (Placeholder for UI enhancement)")
    st.write("Here will be an expenses chart.")

def profile_page():
    st.title(f"Profile of {st.session_state.username}")
    st.image("https://www.example.com/user_profile_image.jpg", caption="Profile Image")
    st.write("Profile information here...")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    project_page()
else:
    login_page()
