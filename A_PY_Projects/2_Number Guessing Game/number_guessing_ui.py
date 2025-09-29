import streamlit as st
import requests

st.set_page_config(page_title="Number Guessing Game", page_icon="🎲")
st.title("Number Guessing Game")
api_url = "http://localhost:8000"

if st.button("Start New Game"):
    resp = requests.post(f"{api_url}/start")
    st.session_state['active'] = True
    st.session_state['attempts'] = 0
    st.success(resp.json()["message"])

if st.session_state.get('active', False):
    guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)
    if st.button("Submit Guess"):
        resp = requests.post(f"{api_url}/guess", json={"guess": guess})
        result = resp.json()["result"]
        attempts = resp.json()["attempts"]
        st.info(result)
        st.session_state['attempts'] = attempts
        if "Congratulations" in result:
            st.session_state['active'] = False
            st.balloons()
    st.write(f"Attempts: {st.session_state.get('attempts', 0)}")