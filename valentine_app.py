import streamlit as st

st.set_page_config(page_title="Strategic Proposal FY2026", page_icon="📈")

# 1. State Management
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# 2. Logic & Layout
if not st.session_state.accepted:
    # Centering the header
    st.markdown("<h1 style='text-align: center;'>Master Valentine Services Agreement (MVSA)</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Will you be my Valentine forever and ever? 😁</h3>", unsafe_allow_html=True)

    # Dynamic Sizing based on "No" count
    # 'YES' gets bigger, 'No' stays small then disappears
    yes_font = 16 + (st.session_state.no_count * 10)
    yes_padding = 10 + (st.session_state.no_count * 15)
    
    # Custom CSS for the "Hostile Takeover"
    st.markdown(f"""
        <style>
        /* Center the button container */
        .stColumn {{
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        /* Target the YES button */
        div.stButton > button[kind="primary"] {{
            font-size: {yes_font}px !important;
            padding: {yes_padding}px {yes_padding*2}px !important;
            width: 100%;
        }}
        /* Target the NO button */
        div.stButton > button[kind="secondary"] {{
            font-size: 14px !important;
            opacity: {max(0.1, 1 - (st.session_state.no_count * 0.2))};
        }}
        </style>
    """, unsafe_allow_html=True)

    # Column split (Starts 50/50, then YES takes over)
    yes_ratio = 1 + (st.session_state.no_count * 2)
    no_ratio = 1
    
    col1, col2, col3 = st.columns([1, yes_ratio + no_ratio, 1]) # Added spacers for centering

    with col2:
        sub_col1, sub_col2 = st.columns([yes_ratio, no_ratio])
        with sub_col1:
            if st.button("YES", type="primary", use_container_width=True):
                st.session_state.accepted = True
                st.rerun()
        with sub_col2:
            # Squeeze out the No option after 5 tries
            if st.session_state.no_count < 5:
                if st.button("No", type="secondary", use_container_width=True):
                    st.session_state.no_count += 1
                    st.rerun()
            else:
                st.empty()

    # The "ROI" Pleading Messages
    if st.session_state.no_count > 0:
        msgs = [
            "This 'No' is an unhedged risk I can't accept.",
            "I've already priced in your 'Yes'. Don't cause a crash.",
            "The ROI on my affection is 10,000%. Do the math.",
            "You're creating a liquidity trap. Have mercy.",
            "Please Sayang? 🥺"
            "SAYANG PLEASEEEE? 🥺😩",
        ]
        st.error(msgs[min(st.session_state.no_count-1, len(msgs)-1)])

else:
    # Success State: The "Closing Bell"
    st.balloons()
    st.success("## MVSA STATUS: FULLY EXECUTED & NOTARISED! ✅")
    
    st.markdown("""
        <div style='text-align: center;'>
            <h2>Acquisition Complete.</h2>
            <p>You have been designated as the <b>Core Strategic Asset</b> of my life.</p>
            <p style='font-size: 0.9em; color: #666;'>
                <i>Note: Approval of this contract removes the need for future annual renegotiations.</i>
            </p>
            <hr>
            <p><b>Contract Term:</b> Perpetual & Irrevocable (FY2026 - ∞)</p>
            <p><b>Next Steps:</b> Dividend payments (endless affection) are now active.</p>
            <p>Reservation for Feb 14th is now legally binding. See you then! 😘❤️</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Stable Minion Asset
    st.image("https://media.tenor.com/kutFNFXxSIsAAAAM/minion-minion-loves.gif", use_container_width=True)
