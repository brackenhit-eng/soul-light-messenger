import streamlit as st

st.set_page_config(page_title="Walk With God's Hand: Portal", page_icon="🕊️", layout="centered")

st.title("🕊️ Welcome to Your Spiritual Tools Portal")
st.markdown("**All your sacred tools in one place. Choose a path of light.**")

apps = {
    "🧘 Soul Light Messenger": "https://soul-light.streamlit.app",
    "🙏 Walk With God's Hand": "https://walk-with-gods-hand.streamlit.app",
    "📿 Prayer Request Tool": "https://walk-with-gods-hand.streamlit.app/prayer",  # Optional if split
    "🌈 Chakra Cleanse (Biblical Names)": "https://walk-with-gods-hand.streamlit.app/chakras",  # Optional
}

for name, link in apps.items():
    st.markdown(f"[{name}]({link})", unsafe_allow_html=True)

st.markdown("---")
st.info("💖 You are walking with purpose. Each link is a sacred invitation.")
