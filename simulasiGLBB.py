import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="Simulasi GLBB", layout="centered")

logo = Image.open("logosmando2d.png")
st.image(logo, width=150)
st.title("🚀 Simulasi Gerak Lurus Berubah Beraturan (GLBB)")
st.markdown("### Andy Kurniawan, S.Si. - SMA Negeri 1 Dolopo, Kab. Madiun")

st.write("Masukkan parameter gerak di bawah ini:")

# Input
v0 = st.number_input("Kecepatan awal (m/s)", value=0.0, step=1.0)
a = st.number_input("Percepatan (m/s²)", value=0.0, step=1.0)
t = st.number_input("Waktu total (s)", min_value=1.0, value=10.0, step=1.0)

if st.button("🔍 Jalankan Simulasi"):
    waktu = np.linspace(0, t, 100)
    posisi = v0 * waktu + 0.5 * a * waktu**2
    kecepatan = v0 + a * waktu

    # Grafik 1: Posisi vs Waktu
    fig1, ax1 = plt.subplots()
    ax1.plot(waktu, posisi, 'b-', linewidth=2)
    ax1.set_title("Grafik Posisi vs Waktu")
    ax1.set_xlabel("Waktu (s)")
    ax1.set_ylabel("Posisi (m)")
    ax1.grid(True)
    st.pyplot(fig1)

    # Grafik 2: Kecepatan vs Waktu
    fig2, ax2 = plt.subplots()
    ax2.plot(waktu, kecepatan, 'g-', linewidth=2)
    ax2.set_title("Grafik Kecepatan vs Waktu")
    ax2.set_xlabel("Waktu (s)")
    ax2.set_ylabel("Kecepatan (m/s)")
    ax2.grid(True)
    st.pyplot(fig2)