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

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

if st.button("Stream data"):
    st.write_stream(stream_data)
