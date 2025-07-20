import streamlit as st
import pandas as pd
import logging

logging.getLogger('streamlit.runtime.scriptrunner.script_run_context').setLevel(logging.ERROR)

sheet_id = "1IsugMSq1iZuKw3fwkKsCc93MOqUsXG6HY5rvLZrQuqI"
sheet_name = "Peserta"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

st.set_page_config(page_title="LEIC 2K25 Dashboard", layout="wide")

logo_urls = [
    "https://drive.google.com/uc?export=view&id=1LuA3DfdXXRXDiqFJpCiVjyJsMX0UXOsI",  # WM
    "https://drive.google.com/uc?export=view&id=1XNy3M4hWvEfC7kHbCyWeoq5-IgHcwgbz",  # TI
    "https://drive.google.com/uc?export=view&id=13Yms8QdLPh63OR0PUYxoTyA0H9YaHxjL",  # HMPS
    "https://drive.google.com/uc?export=view&id=1dBrtaa64m8HcJ927N6J9W5to9eU00Ayj",  # IC
]
right_logo_url = "https://drive.google.com/uc?export=view&id=1HijbSANYKVzavYqNkW7b64hokDmWm7kD"  # Kampus Berdampak

left_col, right_col = st.columns([4, 1])
with left_col:
    logo_cols = st.columns(len(logo_urls))
    for col, url in zip(logo_cols, logo_urls):
        with col:
            st.image(url, width=90)

with right_col:
    st.image(right_logo_url, width=90, use_column_width=False)

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
       
