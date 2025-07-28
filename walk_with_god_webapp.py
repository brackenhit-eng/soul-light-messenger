
import streamlit as st

st.set_page_config(page_title="Walk With God's Hand", page_icon="🕊️")

st.title("🕊️ Walk With God's Hand")
st.subheader("A Guided Healing Journey Through Your Sacred Centers")

st.write("Choose how you're feeling today, and receive a message, prayer, and truth to restore balance — rooted in scripture.")

feelings = {
    "Anxious or unsafe": "Foundation of Trust (Root)",
    "Guilty or emotionally stuck": "Wellspring of Life (Sacral)",
    "Powerless or insecure": "Seat of Courage (Solar Plexus)",
    "Numb or unloved": "Chamber of Love (Heart)",
    "Can't speak or express": "Voice of Truth (Throat)",
    "Confused or foggy": "Eyes of Discernment (Third Eye)",
    "Disconnected from God": "Covenant of Light (Crown)"
}

choice = st.selectbox("🙏 How are you feeling today?", [""] + list(feelings.keys()))

if choice:
    center = feelings[choice]

    st.markdown(f"### 🌈 {center}")

    if center == "Foundation of Trust (Root)":
        st.write("**You are held. Even now, even in fear — God is still your refuge.**")
        st.markdown("> 📖 *Psalm 46:1 — 'God is our refuge and strength, a very present help in trouble.'*")
        st.write("🙏 *Heavenly Father, restore my trust. Let Your peace guard me and root me in safety. Amen.*")
        st.info("💡 Visualize red light flowing down your spine. Say: 'God is my Rock.'")

    elif center == "Wellspring of Life (Sacral)":
        st.write("**Your emotions are sacred. God designed your flow.**")
        st.markdown("> 📖 *Proverbs 4:23 — 'Guard your heart... it is the wellspring of life.'*")
        st.write("🙏 *Lord, help me feel again. Unblock my creativity and let joy flow freely.*")
        st.info("💡 Move your hips gently, dance, or paint. Say: 'I am flowing with grace.'")

    elif center == "Seat of Courage (Solar Plexus)":
        st.write("**Your courage is not your own — it is gifted by God.**")
        st.markdown("> 📖 *Joshua 1:9 — 'Be strong and courageous... for the Lord your God is with you.'*")
        st.write("🙏 *God, ignite my inner fire. Let me stand in Your strength.*")
        st.info("💡 Place your hand on your belly. Say: 'I rise in holy strength.'")

    elif center == "Chamber of Love (Heart)":
        st.write("**You are worthy of love. God is love.**")
        st.markdown("> 📖 *1 John 4:16 — 'God is love. Whoever lives in love lives in God.'*")
        st.write("🙏 *Father, soften my heart. Let me receive and give love again.*")
        st.info("💡 Breathe deeply into your chest. Say: 'Love lives here.'")

    elif center == "Voice of Truth (Throat)":
        st.write("**Your voice matters. You are called to speak life.**")
        st.markdown("> 📖 *John 8:32 — 'Then you will know the truth, and the truth will set you free.'*")
        st.write("🙏 *Lord, release my voice. Let me speak with grace and boldness.*")
        st.info("💡 Hum, chant, or speak aloud. Say: 'My voice carries truth.'")

    elif center == "Eyes of Discernment (Third Eye)":
        st.write("**You are not lost. Your inner sight is awakening.**")
        st.markdown("> 📖 *Ephesians 1:18 — 'That the eyes of your heart may be enlightened...'*")
        st.write("🙏 *God, open my eyes to see with wisdom and trust.*")
        st.info("💡 Sit in silence. Say: 'God shows me the way.'")

    elif center == "Covenant of Light (Crown)":
        st.write("**You are not alone. You are connected to Heaven.**")
        st.markdown("> 📖 *John 15:5 — 'Remain in Me, and I in you.'*")
        st.write("🙏 *Lord, reconnect me. Remind me that You are near.*")
        st.info("💡 Visualize white light above your head. Say: 'I walk with God.'")
