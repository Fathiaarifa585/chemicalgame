import streamlit as st

st.title("Halo Selamat Datang Di Game Kami!")
st.title("Mau Ngapain Dulu Nih?")

import time
import numpy as np
import pandas as pd
import streamlit as st

_KIMIA_ORGANIK = """
HALO!!!Di materi ini kamu akan mempelajari materi terkait kimia anorganik, meliputi Uji nyala dan Uji Kualitatif senyawa anorganik
"""

if st.button("KIMIA ORGANIK"):
    st.write_stream(KIMIA_ORGANIK)
