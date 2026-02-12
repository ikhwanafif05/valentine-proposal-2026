import streamlit as st

st.set_page_config(page_title="MVSA: Perpetual Contract", page_icon="📈")

# 1. State Management
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# 2. Logic & Layout
if not st.session_state.accepted:
    st.markdown("<h1 style='text-align: center;'>Master Valentine Services Agreement (MVSA)</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Jaf Iessa Will you be my Valentine FOREVER?</h3>", unsafe_allow_html=True)

    # Growth Logic
    yes_font = 16 + (st.session_state.no_count * 12)
    yes_padding = 10 + (st.session_state.no_count * 20)
    
    # Custom CSS for the "Hostile Takeover"
    st.markdown(f"""
        <style>
        .stColumn {{ display: flex; align-items: center; justify-content: center; }}
        /* YES Button: Becomes the Market Leader */
        div.stButton > button[kind="primary"] {{
            font-size: {yes_font}px !important;
            padding: {yes_padding}px 0px !important;
            width: 100% !important;
            transition: all 0.3s ease;
        }}
        /* NO Button: Headed for Delisting */
        div.stButton > button[kind="secondary"] {{
            opacity: {max(0.1, 1 - (st.session_state.no_count * 0.25))};
            font-size: 14px !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    # 12-Column Grid Squeeze
    # After 5 clicks, yes_ratio = 11, no_ratio = 1. Effectively 100% ownership.
    yes_ratio = min(11, 2 + (st.session_state.no_count * 2))
    no_ratio = 12 - yes_ratio
    
    col_main = st.columns([1, 10, 1])[1] # Center the action

    with col_main:
        sub_col_yes, sub_col_no = st.columns([yes_ratio, no_ratio])
        
        with sub_col_yes:
            if st.button("YES", type="primary", use_container_width=True):
                st.session_state.accepted = True
                st.rerun()
        
        with sub_col_no:
            # The "Hard-Stop"
            # Once she hits 5 'No's, the button is delisted from the UI.
            if st.session_state.no_count < 5:
                if st.button("No", type="secondary", use_container_width=True):
                    st.session_state.no_count += 1
                    st.rerun()
            else:
                st.empty() # Total Liquidity Squeeze

    # The Pleading Messages [cite: 2025-11-25]
    if st.session_state.no_count > 0:
        msgs = [
            "This 'No' is an unhedged risk I can't accept. [cite: 2025-11-25]",
            "I've already priced in your 'Yes'. Don't cause a crash. [cite: 2025-11-25]",
            "The ROI on my affection is 10,000%. Do the math. [cite: 2025-12-10]",
            "Wait, if you click No again, I'm calling the SEC. [cite: 2025-12-10]",
            "PLEASEEEE? 🥺😩",
        ]
        st.error(msgs[min(st.session_state.no_count-1, len(msgs)-1)])

else:
    # Success State: MVSA Execution
    st.balloons()
    st.success("## MVSA STATUS: FULLY EXECUTED & NOTARISED! ✅")
    st.markdown("""
        <div style='text-align: center;'>
            <h2>Acquisition Complete.</h2>
            <p>You have been designated as the <b>Core Strategic Asset</b> of my life. [cite: 2025-11-25]</p>
            <p style='font-size: 0.9em; color: #888;'>
                <i>Note: Approval of this contract removes the need for future annual renegotiations. [cite: 2025-11-25]</i>
            </p>
            <hr>
            <p><b>Contract Term:</b> Perpetual & Irrevocable (FY2026 - Forever Bru) [cite: 2025-11-25]</p>
            <p>See you on Feb 14th! 😘❤️</p>
        </div>
    """, unsafe_allow_html=True)
    st.image("https://media.tenor.com/kutFNFXxSIsAAAAM/minion-minion-loves.gif", use_container_width=True)
