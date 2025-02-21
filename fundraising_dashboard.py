import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time

# Simulasi Data Real-Time
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
donations = np.random.randint(100, 1000, size=30)
donors = np.random.randint(10, 100, size=30)
df = pd.DataFrame({'Date': dates, 'Donations': donations, 'Donors': donors})

# Layout
st.set_page_config(page_title="Fundraising Dashboard", layout="wide")
st.markdown("""
    <style>
        .main {background-color: #f5f5f5;}
        .stMetric {font-size: 24px !important;}
    </style>
""", unsafe_allow_html=True)

st.title("📊 Fundraising Dashboard")
st.markdown("---")

# Sidebar Filters
st.sidebar.header("🎯 Filter Data")
date_range = st.sidebar.slider("🗓 Pilih Rentang Tanggal", min_value=dates.min().date(), 
                              max_value=dates.max().date(), 
                              value=(dates.min().date(), dates.max().date()))

# Real-Time Data Update
placeholder = st.empty()
while True:
    df['Donations'] = np.random.randint(100, 1000, size=30)
    df['Donors'] = np.random.randint(10, 100, size=30)
    filtered_df = df[(df['Date'] >= pd.Timestamp(date_range[0])) & (df['Date'] <= pd.Timestamp(date_range[1]))]
    
    with placeholder.container():
        st.markdown("### 📌 KPI Utama")
        col1, col2, col3 = st.columns(3)
        col1.metric("💰 Total Donasi", f"Rp {filtered_df['Donations'].sum():,.0f}")
        col2.metric("👥 Jumlah Donatur", f"{filtered_df['Donors'].sum()} orang")
        col3.metric("📊 Rata-rata Donasi", f"Rp {filtered_df['Donations'].mean():,.0f}")
        
        st.markdown("---")
        
        st.subheader("📈 Tren Donasi")
        fig_donations = px.line(filtered_df, x='Date', y='Donations', title='📊 Tren Donasi per Hari', 
                                template='seaborn', markers=True)
        st.plotly_chart(fig_donations, use_container_width=True)

        st.markdown("---")
        
        st.subheader("🔍 Funnel Konversi")
        funnel_data = pd.DataFrame({
            "Tahap": ["Pengunjung Halaman", "Klik Donasi", "Transaksi Berhasil"],
            "Jumlah": [10000, 2500, 800]
        })
        fig_funnel = px.funnel(funnel_data, x='Jumlah', y='Tahap', title='🚀 Funnel Konversi Donasi', 
                                template='seaborn')
        st.plotly_chart(fig_funnel, use_container_width=True)
        
        st.markdown("---")
        
        st.subheader("🗺 Sebaran Donatur")
        map_data = pd.DataFrame({
            'lat': np.random.uniform(-6.2, -6.3, 50),
            'lon': np.random.uniform(106.7, 106.9, 50)
        })
        st.map(map_data)
        
        st.markdown("---")
        
        st.success("✅ Data diperbarui setiap 5 detik secara otomatis!")
    
    time.sleep(5)
