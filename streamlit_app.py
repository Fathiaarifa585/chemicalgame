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
    for char in _LOREM_IPSUM:
        full_text+=char
        placeholder.markdown(f"<p style='font-size:20px'>{full_text}</p>",unsafe_allow_html=True)
        time.sleep(0.05)
        
if st.button("Stream data"):
    stream_data()
        
import streamlit as st
left, right = st.columns(2)
if left.button("Organik", icon="🧫", use_container_width=True):
    left.markdown("sekarang kamu mau belajar materi dulu atau langsung main game aja?")
if right.button("Anorganik", icon="🧪", use_container_width=True):
     right.markdown("You clicked the Anorganik.")

col1,col2=st.columns(2)
with col1:
    if st.button("materi Organik"):
        st.write("🔬 *Uji Alkohol dalam Kimia Organik*

Alkohol adalah senyawa organik yang memiliki gugus –OH (hidroksil) yang terikat pada atom karbon jenuh. Untuk mengidentifikasi jenis alkohol (primer, sekunder, atau tersier), dapat dilakukan beberapa *uji kualitatif sederhana, antara lain **reaksi dengan logam natrium (Na)* dan *uji Lucas*.

---

### ⚗ *1. Reaksi Alkohol dengan Logam Natrium (Na)*

*Prinsip:*
Alkohol dapat bereaksi dengan logam natrium membentuk *alkoksida* dan *gas hidrogen (H₂). Reaksi ini ditandai dengan **munculnya gelembung gas (buih)*.
Pengamatan:*

* Timbul *buih atau gelembung gas* menunjukkan adanya gas H₂
* Semakin reaktif alkohol → reaksi lebih cepat
 🧪 *2. Uji Lucas (Lucas Test)*

*Prinsip:*
Uji ini digunakan untuk *mengidentifikasi jenis alkohol* berdasarkan kecepatan terbentuknya *endapan atau kekeruhan* saat alkohol bereaksi dengan *reagen Lucas* (campuran ZnCl₂ dan HCl pekat). Reagen ini menyebabkan terbentuknya alkil halida yang tidak larut dalam air → larutan menjadi *keruh*.
")
with col2:
    if st.button("materi Anorganik"):
        st.write("mulai materi Anorganik")

col1,col2=st.columns(2)
with col1:
    if st.button("game Organik"):
        st.write("mulai game Organik")
with col2:
    if st.button("game Anorganik"):
        st.write("mulai game Anorganik")



