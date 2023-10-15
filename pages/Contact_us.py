import streamlit as st
from send_email import send_email

st.header("Leave a message")

with st.form(key="email_forms"):
    user_email =st.text_input("Enter your Email:")
    options = st.selectbox("what would you to discuss about?",("study","course", "general enquiry"))
    raw_message = st.text_area("Your message")
    Message = f"""\
Subject: Love from {user_email} + {options}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(Message)
        st.info("your email was sent successfully")
