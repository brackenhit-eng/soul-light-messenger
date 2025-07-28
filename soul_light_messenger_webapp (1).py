
import streamlit as st
import random
import datetime

# Title and description
st.set_page_config(page_title="Soul Light Messenger", page_icon="🕊️")
st.title("🌌 Soul Light Messenger")
st.markdown("A gentle tool to deliver soul messages and prayers to those going through hard times.")

# Sample soul messages and prayers
messages = [
    {
        "trigger": "hopeless",
        "message": (
            "Beloved soul, I know you feel like the light is gone — like there’s no way forward. But please know this:\n"
            "Even the deepest night ends, and the smallest spark can relight a life. You are not your pain. You are not forgotten.\n"
            "Right now, simply breathe. You are still here, and that is a miracle. Light is returning — gently, slowly, faithfully.\n"
            "Let it in, one breath at a time."
        ),
        "prayer": (
            "God of grace, wrap this soul in light. Let peace touch their heart and remind them they are not alone.\n"
            "Send angels to their side, silence the lies of despair, and speak love into the silence.\n"
            "May hope rise again — even if softly, even if slowly. Amen."
        )
    },
    {
        "trigger": "grief",
        "message": (
            "I know the loss feels unbearable. There are no perfect words — only this truth: love does not die.\n"
            "The one you lost is closer than you think. In the stillness, in the tears, in the quiet — they are near.\n"
            "You are allowed to feel broken. But you are not alone in the breaking. You are not alone in the healing."
        ),
        "prayer": (
            "Divine Spirit, cradle this grieving soul. Let your gentleness soothe the ache no words can reach.\n"
            "Bring memories that heal. Hold their heart in sacred rest. And remind them: love always finds a way to return.\n"
            "Amen."
        )
    },
    {
        "trigger": "failure",
        "message": (
            "You think you’ve failed, but listen: failure is not the end. It’s a redirection, not a rejection.\n"
            "Every soul that rose again has felt this — the shame, the weight, the ‘not enough.’ But you are not your lowest moment.\n"
            "You are worthy. You are becoming. And your story is not over yet."
        ),
        "prayer": (
            "God of mercy, lift this soul from the weight of self-blame. Show them the truth — that they are loved, even now.\n"
            "May they rise, not in perfection, but in grace. Let them see their worth reflected in Your eyes.\n"
            "Amen."
        )
    }
]

# Input field
feeling = st.text_input("🖤 What is this person feeling or going through?", "")

# Search for matching message
if feeling:
    match = next((m for m in messages if m["trigger"] in feeling.lower()), None)
    if match:
        st.markdown("### 🌙 Soul Message")
        st.text(match["message"])
        st.markdown("### 🙏 Prayer")
        st.text(match["prayer"])
        st.markdown(f"*Delivered at:* {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.warning("🌫️ No message matched that word yet — but this soul is still deeply seen and loved.")
        st.info("🕊️ May peace surround them even when words fall short.")
