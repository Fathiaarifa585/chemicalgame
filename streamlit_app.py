import streamlit as st

st.title("Halo Selamat Datang Di Game Kami!")
st.title("Mau Ngapain Dulu Nih?")

import time
import numpy as np
import pandas as pd
import streamlit as st

_LOREM_IPSUM = """
Di materi ini kamu akan mempelajari onorganik. ada latoihan dan materinya juga. kamu mau pilih yang mana dulu?
"""

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        st.write(word)
        time.sleep(0.3)
        
if st.button("Stream data"):
    st.write_stream(stream_data)
        
import streamlit as st
left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
     middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")

if st.button("Stream data"):
    st.write_stream(stream_data)
