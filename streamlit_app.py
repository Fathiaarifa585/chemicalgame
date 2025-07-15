import streamlit as st

st.title("Halo Selamat Datang Di Game Kami!")
st.title("Mau Ngapain Dulu Nih?")

import time
import streamlit as st

_LOREM_IPSUM = """
Di materi ini kamu akan mempelajari onorganik. ada latoihan dan materinya juga. kamu mau pilih yang mana dulu?
"""

def stream_data():
    placeholder=st.empty()
    full_text=""
    for char in_LOREM_IPSUM:
        full_text+=char
        placeholder.markdown(f"<p style='font-size:20px'>{full_text}</p>",unsafe_allow_html=True)
        time.sleep(0.05)
        
if st.button("Stream data"):
    stream_data()
        
import streamlit as st
left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
     middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")

