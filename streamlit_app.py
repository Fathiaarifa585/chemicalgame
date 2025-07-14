import streamlit as st

st.title("Halo Selamat Datang Di Game Kami!")
st.title("Mau Ngapain Dulu Nih?")

import time
import numpy as np
import pandas as pd
import streamlit as st

Di materi ini kamu akan mempelajari tentang materi yang ada di kimia anorganik, meliputi analisis kualitatif senyawa anorganik dan juga uji nyala


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)
