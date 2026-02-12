import streamlit as st

# Set page config for a professional terminal look
st.set_page_config(page_title="Strategic Proposal FY2026", page_icon="📈")

# Initialize session state for the "No" counter
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# Layout
st.title("Final Term Sheet: Strategic Partnership")
st.subheader("To: My Favourite Asset")

if not st.session_state.accepted:
    st.write("### Will you be my Valentine?")
    
    # Growth logic: The "No-Trap" mechanism
    yes_size = 1.0 + (st.session_state.no_count * 0.6) # Aggressive expansion
    no_size = max(0.1, 1.0 - (st.session_state.no_count * 0.2)) # Liquidity squeeze
    
    col1, col2 = st.columns([yes_size, no_size])

    with col1:
        if st.button("YES", type="primary", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        if st.button("No", type="secondary", use_container_width=True):
            st.session_state.no_count += 1
            st.rerun()

    # The Pleading Messages: "Leveraged Negotiation" Mode
    if st.session_state.no_count > 0:
        pleading_messages = [
            "Please? 🥺",
            "This 'No' is an unhedged risk I can't accept.",
            "I've already priced in your 'Yes'. Don't cause a market crash.",
            "The ROI on my affection is literally 10,000%. Do the math.",
            "You're creating a liquidity trap. Have mercy.",
            "Wait, if you click No again, I'm calling the SEC.",
            "Please? I'll treat you like a blue-chip stock.",
            "Fine. I'll buy you nuggets. Now click Yes.",
        ]
        msg_index = min(st.session_state.no_count - 1, len(pleading_messages) - 1)
        st.error(pleading_messages[msg_index])

else:
    # Success State: The "Closing Bell"
    st.balloons()
    st.success("## TRANSACTION CONFIRMED! ✅")
    st.write("You have successfully merged with Ikhwan. See you on Feb 14th! 😘❤️")
    # Fixed GIF: Direct link to the Minion Heart 
    st.image("https://media.tenor.com/kutFNFXxSIsAAAAM/minion-minion-loves.gif")
