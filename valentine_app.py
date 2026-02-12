import streamlit as st

st.set_page_config(page_title="Strategic Proposal FY2026", page_icon="📈")

# 1. State Management
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# 2. The Logic
if not st.session_state.accepted:
    st.title("Final Term Sheet: Strategic Partnership")
    st.write("### Will you be my Valentine?")

    # Squeeze Logic: "Yes" grows, "No" disappears
    # We use a 12-column grid. "Yes" takes more columns as count increases.
    yes_cols = min(11, 2 + (st.session_state.no_count * 2)) 
    no_cols = 12 - yes_cols

    col1, col2 = st.columns([yes_cols, no_cols])

    with col1:
        # Custom CSS to make the button actually bigger vertically too
        yes_padding = 10 + (st.session_state.no_count * 20)
        st.markdown(f"""
            <style>
            div.stButton > button:first-child {{
                padding: {yes_padding}px 0px;
                font-size: {16 + st.session_state.no_count * 5}px !important;
            }}
            </style>""", unsafe_allow_html=True)
            
        if st.button("YES", type="primary", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        # If no_cols is very small, we just stop showing the button
        if no_cols > 1:
            if st.button("No", type="secondary", use_container_width=True):
                st.session_state.no_count += 1
                st.rerun()
        else:
            st.write("") # No button has been "delisted"

    # The Pleading Messages: "Leveraged Negotiation" Mode
    if st.session_state.no_count > 0:
        pleading_messages = [
            "This 'No' is an unhedged risk I can't accept.",
            "I've already priced in your 'Yes'. Don't cause a market crash.",
            "The ROI on my affection is literally 10,000%. Do the math.",
            "You're creating a liquidity trap. Have mercy.",
            "Wait, if you click No again, I'm calling the SEC.",
            "Please? 🥺",
            "PLEASEEEE? 🥺😩",
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
