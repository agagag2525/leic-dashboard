import streamlit as st
import pandas as pd
import logging

logging.getLogger('streamlit.runtime.scriptrunner.script_run_context').setLevel(logging.ERROR)

sheet_id = "1IsugMSq1iZuKw3fwkKsCc93MOqUsXG6HY5rvLZrQuqI"
sheet_name = "Peserta"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

st.set_page_config(page_title="LEIC 2K25 Dashboard", layout="wide")

base_img_url = "https://raw.githubusercontent.com/agagag2525/leic-dashboard/main/assets/"

logos = [
    "Logo_WM_Standar_PNG.png",                  # WM
    "TI.png",                                    # TI
    "HMPS.PNG",                                  # HMPS TI
    "IC.png",                                    # Industrial Challenge
    "Primary_Horizontal%20Logo.png",            # Kampus Berdampak
]

st.markdown("""
<style>
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
</style>
""", unsafe_allow_html=True)

logo_html = "<div class='logo-container'>"
for logo in logos:
    logo_html += f"<img src='{base_img_url}{logo}' alt='logo'>"
logo_html += "</div>"
st.markdown(logo_html, unsafe_allow_html=True)

st.title("🚛 Logistics Execution Industrial Challenge 2K25")
st.subheader("📊 Real-Time Dashboard")

try:
    df = pd.read_csv(url, dtype=str).fillna("")
    df = df.dropna(axis=1, how='all')

    st.success("✅ Data berhasil dimuat!")

    st.markdown("### 💰 Uang Per Tim")
    if "Rank" in df.columns and "Uang" in df.columns:
        display_df = df[["Rank", "Uang"]].copy()
        display_df.index = display_df.index + 1
        st.dataframe(display_df)
    else:
        st.warning("Kolom 'Rank' dan/atau 'Uang' tidak ditemukan.")
except Exception as e:
    st.error(f"❌ Gagal memuat data: {e}")
       
