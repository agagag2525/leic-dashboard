import streamlit as st
import pandas as pd
import logging

# Hapus warning log Streamlit
logging.getLogger('streamlit.runtime.scriptrunner.script_run_context').setLevel(logging.ERROR)

# Spreadsheet source
sheet_id = "1IsugMSq1iZuKw3fwkKsCc93MOqUsXG6HY5rvLZrQuqI"
sheet_name = "Peserta"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Page setup
st.set_page_config(page_title="LEIC 2K25 Dashboard", layout="wide")

# Logo image sources (GitHub)
base_img_url = "https://raw.githubusercontent.com/agagag2525/leic-dashboard/main/assets/"
logos = [
    "Logo_WM_Standar_PNG.png",
    "TI.png",
    "HMPS.PNG",
    "IC.png",
    "Primary_Horizontal%20Logo.png",
]

# --- CSS Styling ---
st.markdown("""
<style>
body {
    background-color: #cceeff;
    font-family: 'Fredoka', sans-serif;
}
.logo-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 24px;
    margin-bottom: 32px;
}
.logo-container img {
    max-height: 80px;
    height: auto;
    max-width: 100%;
    object-fit: contain;
}
@media (max-width: 768px) {
    .logo-container img {
        max-height: 60px;
    }
}
.block-container {
    padding-top: 0rem;
}
h1, h2, h3 {
    color: #2b6777;
    font-family: 'Fredoka', sans-serif;
}
.dataframe-style {
    background-color: white;
    border-radius: 10px;
    padding: 1rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
</style>
<link href="https://fonts.googleapis.com/css2?family=Fredoka&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# --- Logo Display ---
logo_html = "<div class='logo-container'>"
for logo in logos:
    logo_html += f"<img src='{base_img_url}{logo}' alt='logo'>"
logo_html += "</div>"
st.markdown(logo_html, unsafe_allow_html=True)

# --- Judul Dashboard ---
st.title("🚛 Logistics Execution Industrial Challenge 2K25")
st.subheader("📊 Real-Time Dashboard")

# --- Data Loading ---
try:
    df = pd.read_csv(url, dtype=str).fillna("")
    df = df.dropna(axis=1, how='all')
    st.success("✅ Data berhasil dimuat!")

    st.markdown("### 💰 Uang Per Tim")
    if "Rank" in df.columns and "Uang" in df.columns:
        display_df = df[["Rank", "Uang"]].copy()
        display_df.index = display_df.index + 1
        st.markdown('<div class="dataframe-style">', unsafe_allow_html=True)
        st.dataframe(display_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Kolom 'Rank' dan/atau 'Uang' tidak ditemukan.")
except Exception as e:
    st.error(f"❌ Gagal memuat data: {e}")
