
import streamlit as st

st.set_page_config(page_title="Walk With God's Hand", page_icon="🕊️")

st.title("🕊️ Walk With God's Hand")
st.subheader("A Guided Healing Journey Through Your Sacred Centers")

# Opening Blessing
st.markdown("### 🙌 Opening Blessing")
st.markdown("> *You are not alone. As you begin, may the hand of God gently rest upon your heart. Breathe… you are safe here.*")

# Scripture of the Day
import random
scriptures = [
    "Psalm 46:1 — 'God is our refuge and strength, a very present help in trouble.'",
    "Isaiah 41:10 — 'Do not fear, for I am with you... I will uphold you.'",
    "John 15:5 — 'Remain in Me, and I in you.'",
    "Joshua 1:9 — 'Be strong and courageous... for the Lord your God is with you.'",
    "Ephesians 1:18 — 'That the eyes of your heart may be enlightened...'",
    "Proverbs 4:23 — 'Guard your heart... for it is the wellspring of life.'",
    "1 John 4:16 — 'God is love. Whoever lives in love lives in God.'"
]
daily_verse = random.choice(scriptures)
st.markdown("### 📖 Scripture of the Day")
st.success(f"“{daily_verse}”")

st.markdown("---")

# Full Body Alignment Flow
st.markdown("## 🌈 Full Body Alignment with God")
st.write("Take a moment to align your entire being with God's hand. Let each center be bathed in light, love, and truth.")

alignment_steps = [
    {
        "title": "🟥 Foundation of Trust (Root)",
        "message": "You are held. Even now — God is still your refuge.",
        "scripture": "Psalm 46:1",
        "prayer": "Heavenly Father, restore my trust. Let Your peace root me in safety.",
        "affirmation": "God is my Rock."
    },
    {
        "title": "🟧 Wellspring of Life (Sacral)",
        "message": "Your emotions are sacred. God designed your flow.",
        "scripture": "Proverbs 4:23",
        "prayer": "Lord, unblock my creativity and let joy flow freely.",
        "affirmation": "I am flowing with grace."
    },
    {
        "title": "🟨 Seat of Courage (Solar Plexus)",
        "message": "Your courage is a divine gift.",
        "scripture": "Joshua 1:9",
        "prayer": "God, ignite my fire. Let me stand in Your strength.",
        "affirmation": "I rise in holy strength."
    },
    {
        "title": "🟩 Chamber of Love (Heart)",
        "message": "You are worthy of love. God is love.",
        "scripture": "1 John 4:16",
        "prayer": "Father, soften my heart. Let me receive and give love.",
        "affirmation": "Love lives here."
    },
    {
        "title": "🟦 Voice of Truth (Throat)",
        "message": "Your voice matters. You are called to speak life.",
        "scripture": "John 8:32",
        "prayer": "Lord, release my voice. Let me speak with boldness.",
        "affirmation": "My voice carries truth."
    },
    {
        "title": "🟪 Eyes of Discernment (Third Eye)",
        "message": "You are not lost. Your inner sight is awakening.",
        "scripture": "Ephesians 1:18",
        "prayer": "God, open my eyes to see with wisdom and trust.",
        "affirmation": "God shows me the way."
    },
    {
        "title": "⬜ Covenant of Light (Crown)",
        "message": "You are connected to Heaven.",
        "scripture": "John 15:5",
        "prayer": "Lord, reconnect me. Let Your presence dwell in me.",
        "affirmation": "I walk with God."
    }
]

if "alignment_index" not in st.session_state:
    st.session_state.alignment_index = 0

current = alignment_steps[st.session_state.alignment_index]
st.markdown(f"### {current['title']}")
st.write(f"**{current['message']}**")
st.markdown(f"> 📖 *{current['scripture']}*")
st.write(f"🙏 *{current['prayer']}*")
st.info(f"💡 Affirmation: **{current['affirmation']}**")

col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Back", disabled=st.session_state.alignment_index == 0):
        st.session_state.alignment_index -= 1
with col2:
    if st.button("Next ➡️", disabled=st.session_state.alignment_index == len(alignment_steps) - 1):
        st.session_state.alignment_index += 1
