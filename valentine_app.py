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
    st.markdown("<h3 style='text-align: center;'>Jaf Iessa, will you be my Valentine FOREVER?</h3>", unsafe_allow_html=True)

    # Growth Logic
    yes_font = 16 + (st.session_state.no_count * 12)
    yes_padding = 15 + (st.session_state.no_count * 20) # Equal start padding
    
    # Custom CSS for parity and then dominance
    st.markdown(f"""
        <style>
        .stButton > button {{
            height: auto !important;
            white-space: nowrap !important;
        }}
        /* YES Button: Market Cap Expansion */
        div.stButton > button[kind="primary"] {{
            font-size: {yes_font}px !important;
            padding: {yes_padding}px 0px !important;
            width: 100% !important;
        }}
        /* NO Button */
        div.stButton > button[kind="secondary"] {{
            padding: 15px 0px !important; /* Matches YES start padding */
            font-size: 16px !important;
            width: 100% !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    # 12-Column Grid [cite: 2025-12-10]
    # Starts 6:6 (Balanced), ends 11:1 (Monopoly)
    yes_ratio = min(11, 6 + (st.session_state.no_count * 1))
    no_ratio = 12 - yes_ratio
    
    col_main = st.columns([1, 10, 1])[1] 

    with col_main:
        sub_col_yes, sub_col_no = st.columns([yes_ratio, no_ratio])
        
        with sub_col_yes:
            if st.button("YES", type="primary", use_container_width=True):
                st.session_state.accepted = True
                st.rerun()
        
        with sub_col_no:
            # Baited labels to encourage the first click
            no_labels = ["No (DO NOT CLICK ⛔️)"]
            current_label = no_labels[min(st.session_state.no_count, len(no_labels)-1)]
            
            if st.session_state.no_count < 5:
                if st.button(current_label, type="secondary", use_container_width=True):
                    st.session_state.no_count += 1
                    st.rerun()
            else:
                st.empty() 

    if st.session_state.no_count > 0:
        msgs = [
            "This 'No' is an unhedged risk I can't accept.",
            "I've already priced in your 'Yes'. Don't cause a crash.",
            "The ROI on my affection is 10,000%. Do the math.",
            "If you click No again, I'm calling the SEC frfr.",
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
            <p style='font-size: 1.5em; font-weight: bold;'>You will now be my Valentine FOR LIFE! ❤️</p>
            <p style='font-size: 0.9em'>
                <i>Note: Approval of this contract removes the need for future annual renegotiations.</i>
            </p>
            <hr>
            <p><b>Contract Term:</b> Perpetual & Irrevocable (FY2026 - Forever Bru).</p>
            <p><b>Dividend Policy:</b> Unlimited affection DAILY.</p>
            <p>Reservation for Feb 14th is now legally binding. See you then, Sayang! 😘</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Stable Minion Asset
    st.image("https://media.tenor.com/kutFNFXxSIsAAAAM/minion-minion-loves.gif", use_container_width=True)
