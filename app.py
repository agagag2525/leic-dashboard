import streamlit as st
import pandas as pd
import logging

logging.getLogger('streamlit.runtime.scriptrunner.script_run_context').setLevel(logging.ERROR)

sheet_id = "1IsugMSq1iZuKw3fwkKsCc93MOqUsXG6HY5rvLZrQuqI"
sheet_name = "Peserta"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

st.set_page_config(page_title="LEIC 2K25 Dashboard", layout="wide")

base_img_url = "https://raw.githubusercontent.com/agagag2525/leic-dashboard/main/assets/"
logo_paths = {
    "WM": "Logo_WM_Standar_PNG.png",
    "TI": "TI.png",
    "HMPS": "HMPS.PNG",
    "IC": "IC.png",
    "KB": "Primary_Horizontal%20Logo.png"
}
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col1:
    st.image(base_img_url + logo_paths["WM"], width=100)
with col2:
    st.image(base_img_url + logo_paths["TI"], width=100)
with col3:
    st.image(base_img_url + logo_paths["HMPS"], width=100)
with col4:
    st.image(base_img_url + logo_paths["IC"], width=100)
with col5:
    st.image(base_img_url + logo_paths["KB"], width=100)

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
       
