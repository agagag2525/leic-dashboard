import streamlit as st
import pandas as pd
import logging

logging.getLogger('streamlit.runtime.scriptrunner.script_run_context').setLevel(logging.ERROR)

sheet_id = "1IsugMSq1iZuKw3fwkKsCc93MOqUsXG6HY5rvLZrQuqI"
sheet_name = "Peserta"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

st.set_page_config(page_title="LEIC 2K25 Dashboard", layout="wide")

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1.5])

with col1:
    st.image("https://drive.google.com/uc?export=view&id=1LuA3DfdXXRXDiqFJpCiVjyJsMX0UXOsI", width=80)  # Logo WM
with col2:
    st.image("https://drive.google.com/uc?export=view&id=1XNy3M4hWvEfC7kHbCyWeoq5-IgHcwgbz", width=80)  # Logo TI
with col3:
    st.image("https://drive.google.com/uc?export=view&id=13Yms8QdLPh63OR0PUYxoTyA0H9YaHxjL", width=80)  # Logo HMPS
with col4:
    st.image("https://drive.google.com/uc?export=view&id=1dBrtaa64m8HcJ927N6J9W5to9eU00Ayj", width=80)  # Logo IC
with col5:
    st.image("https://drive.google.com/uc?export=view&id=1HijbSANYKVzavYqNkW7b64hokDmWm7kD", width=120)  # Logo Kampus Berdampak

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
       
