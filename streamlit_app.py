import streamlit as st
def tampilkan_menu_utama():
  st.title("Game Uji Kualitatif Senyawa Organik dan Anorganik")
  menu=st.selectbox("Pilih menu:",["Organik","Anorganik"])
  return menu
