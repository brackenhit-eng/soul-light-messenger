import streamlit as st
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

st.set_page_config(page_title="Walk With God's Hand", page_icon="🕊️")

st.title("🕊️ Walk With God's Hand")
st.subheader("Send a Prayer or Healing Request")

st.markdown("If you or someone you love needs prayer, healing, or simply to be held in sacred space — send a message below. Jannie will hold your request in meditation with care and light.")

# Prayer Request Form
with st.form("prayer_form"):
    name = st.text_input("Name (optional)")
    message = st.text_area("What are you going through? (or how can we support you?)")
    request_type = st.selectbox("How would you like to be lifted?", [
        "Prayer", "Healing Light in Meditation", "Encouragement", "Just to Be Seen"
    ])
    healing_circle = st.checkbox("Please add me to your daily healing circle 🙏")
    submitted = st.form_submit_button("Send My Request")

    if submitted:
        try:
            # Setup Google Sheets connection using secrets
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds_dict = st.secrets["gcp_service_account"]
            creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), scope)
            client = gspread.authorize(creds)

            # Open or create the sheet
            sheet_name = "WWGH Prayer Requests"
            try:
                sheet = client.open(sheet_name).sheet1
            except gspread.SpreadsheetNotFound:
                sheet = client.create(sheet_name).sheet1
                sheet.append_row(["Timestamp", "Name", "Message", "Request Type", "Healing Circle"])

            # Add the submission
            sheet.append_row([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name,
                message,
                request_type,
                "Yes" if healing_circle else "No"
            ])
            st.success("Your message has been received. You are held in light. 🕊️")

        except Exception as e:
            st.error("Oops! Something went wrong sending your request. Please try again later.")
            st.exception(e)

st.markdown("---")
st.markdown("**🔐 Your message is private and goes only to Jannie. You will never be judged — only held in prayer.**")