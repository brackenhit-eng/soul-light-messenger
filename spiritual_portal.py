import streamlit as st
import webbrowser
import time

st.set_page_config(page_title="🕊️ Spiritual Portal", page_icon="🕊️", layout="centered")

st.title("🕊️ Walk With God’s Hand — Portal")

# Welcome and Blessing
st.markdown("""
Welcome to your sacred space online. Choose a tool below to receive light, prayer, and guidance. Each app is a doorway for healing, reflection, and divine connection.🕊️✨

**🙏 Opening Prayer**

Heavenly Father, let this space be filled with peace, wisdom, and light.  
Guide each soul who visits here with clarity, courage, and comfort.  
May Your hand be upon them as they explore, heal, and remember who they truly are in You.  
Amen.
""")

st.markdown("---")

# Mini Guided Meditation
with st.expander("🧘‍♀️ Start a Mini Guided Meditation"):
    st.markdown("""
    **Close your eyes and take a deep breath.**

    As you inhale, feel light filling your body.

    As you exhale, release all burdens to God.

    > "Be still, and know that I am God." — Psalm 46:10

    Let your heart open.  
    Let peace flow in.

    **You are held. You are loved. You are not alone.**
    """)
    if st.button("✨ Play Soft Meditation"):
        st.audio("https://upload.wikimedia.org/wikipedia/commons/8/89/Relaxing_Nature_Sounds_-_Birds_and_Water.ogg")

st.markdown("---")

# Chakra Section (Renamed for Biblical Clarity)
st.markdown("""
## 🌟 Your Sacred Centers (Inspired by Scripture)

Each center reflects an aspect of your walk with God:

1. **Foundation (Root)** — Your trust in God's protection and stability.  
   🛐 *Prayer:* "Lord, ground me in Your promises. Let me feel safe and secure in You."

2. **Connection (Sacral)** — Your ability to form holy bonds and express creativity.  
   🛐 *Prayer:* "God, bless my relationships and awaken the holy creativity within me."

3. **Strength (Solar Plexus)** — Your courage, self-worth, and confidence in Christ.  
   🛐 *Prayer:* "Jesus, be my strength. Let my confidence rise from knowing I am Yours."

4. **Heart of Love (Heart)** — Your ability to love as Christ loves.  
   🛐 *Prayer:* "Fill my heart with Your divine love so I may reflect it to others."

5. **Voice of Truth (Throat)** — Speaking with clarity, grace, and honesty.  
   🛐 *Prayer:* "Holy Spirit, guide my words. Let truth flow from my lips with love."

6. **Eyes of Faith (Third Eye)** — Seeing with spiritual vision and divine wisdom.  
   🛐 *Prayer:* "Open the eyes of my heart, Lord, that I may see through Your wisdom."

7. **Crown of Light (Crown)** — Your spiritual connection with the Father and awareness of divine purpose.  
   🛐 *Prayer:* "God, align me with Your will. Let Your light guide my every step."

> "Do you not know that you are God’s temple and that God’s Spirit dwells in you?" — 1 Corinthians 3:16

Take a moment to reflect on which area needs attention and ask God to align it with His will.
""")

st.markdown("---")

# App Links
apps = [
    {
        "title": "📬 Soul Light Messenger",
        "description": "Send or receive soul messages and prayers when you or others are going through hard times.",
        "url": "https://soul-light1.streamlit.app/"
    },
    {
        "title": "🌈 Walk With God’s Hand",
        "description": "A guided chakra journey through scripture and prayer, aligned with divine light.",
        "url": "https://walk-with-gods-hand7.streamlit.app/"
    },
    {
        "title": "📖 Guided Soul Messages",
        "description": "Explore what emotions someone might be feeling and offer a soul message and prayer to uplift them.",
        "url": "https://soul-light-messenger-cx9gpaxu4xwx4wwwmvmnka.streamlit.app/"
    },
    {
        "title": "🕯️ Prayer Request Box",
        "description": "Send a prayer or healing request directly to Jannie's meditation circle.",
        "url": "https://walk-with-gods-hand7.streamlit.app/"  # Replace with prayer app link if separate
    }
]

# Display App Buttons
for app in apps:
    st.subheader(app["title"])
    st.markdown(app["description"])
    st.markdown(f"[Open App ➜]({app['url']})", unsafe_allow_html=True)
    st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; font-size: 0.9em;'>
    Made with 🤍 by Jannie · <a href="https://spiritualp1.streamlit.app" target="_blank">Return to Main</a>
</div>
""", unsafe_allow_html=True)
