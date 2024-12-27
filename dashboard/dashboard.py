import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Judul Aplikasi
st.title('Bike Sharing Dashboard')
st.write("""
Dashboard ini menampilkan visualisasi operasional penyewaan sepeda berdasarkan data cuaca dan waktu.
""")

# 2. Load Data
@st.cache_data  # Menggunakan cache untuk mempercepat load data
def load_data():
    data = pd.read_csv('dashboard/main_data.csv')
    data['dteday'] = pd.to_datetime(data['dteday'])  # Pastikan kolom dteday dalam format datetime
    return data

data = load_data()

# 3. Filter Data
st.sidebar.header('Filter Data')
season_filter = st.sidebar.multiselect('Season (Hour)', data['season_hour'].unique(), default=data['season_hour'].unique())
month_filter = st.sidebar.slider('Month (Hour)', 1, 12, (1, 12))
workingday_filter = st.sidebar.selectbox('Working Day (Hour)', [0, 1], index=1)

# Filter Periode Tanggal
date_filter = st.sidebar.date_input('Filter Periode Tanggal', [data['dteday'].min().date(), data['dteday'].max().date()])

filtered_data = data[(data['season_hour'].isin(season_filter)) &
                    (data['mnth_hour'] >= month_filter[0]) & (data['mnth_hour'] <= month_filter[1]) &
                    (data['workingday_hour'] == workingday_filter) &
                    (data['dteday'] >= pd.to_datetime(date_filter[0])) & (data['dteday'] <= pd.to_datetime(date_filter[1]))]

# 4. Visualisasi Operasional KPI
st.subheader('Key Performance Indicators')

# Rata-rata Penyewaan Per Jam
avg_rentals_hour = filtered_data['cnt_hour'].mean()
st.metric(label='Rata-rata Penyewaan Per Jam', value=f"{avg_rentals_hour:.0f}")

# Total Penyewaan Per Jam
total_rentals_hour = filtered_data['cnt_hour'].sum()
st.metric(label='Total Penyewaan Per Jam', value=f"{total_rentals_hour:.0f}")

# Rata-rata Penyewaan Per Hari
avg_rentals_day = filtered_data['cnt_day'].mean()
st.metric(label='Rata-rata Penyewaan Per Hari', value=f"{avg_rentals_day:.0f}")

# Total Penyewaan Per Hari
total_rentals_day = filtered_data['cnt_day'].sum()
st.metric(label='Total Penyewaan Per Hari', value=f"{total_rentals_day:.0f}")

# Penyewaan Musiman
st.subheader('Penyewaan Berdasarkan Musim (Hour)')
season_data_hour = filtered_data.groupby('season_hour')['cnt_hour'].sum()
st.bar_chart(season_data_hour)

st.subheader('Penyewaan Berdasarkan Musim (Day)')
season_data_day = filtered_data.groupby('season_day')['cnt_day'].sum()
st.bar_chart(season_data_day)

# Tren Penyewaan Harian
st.subheader('Tren Penyewaan Harian (Hour)')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data['dteday'], filtered_data['cnt_hour'], label='Total Rentals (cnt_hour)')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewaan')
ax.legend()
st.pyplot(fig)

st.subheader('Tren Penyewaan Harian (Day)')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data['dteday'], filtered_data['cnt_day'], label='Total Rentals (cnt_day)', color='green')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewaan')
ax.legend()
st.pyplot(fig)

# Distribusi Jam Sibuk
st.subheader('Distribusi Penyewaan Berdasarkan Jam')
fig, ax = plt.subplots(figsize=(10, 5))
filtered_data.groupby('hr')['cnt_hour'].mean().plot(kind='bar', ax=ax)
ax.set_xlabel('Jam')
ax.set_ylabel('Rata-rata Penyewaan')
st.pyplot(fig)

# 5. Korelasi antara Data Hour dan Day
st.subheader('Korelasi antara Data Hour dan Day')

# Memilih kolom yang relevan
hour_cols = ['temp_hour', 'atemp_hour', 'hum_hour', 'windspeed_hour', 'cnt_hour']
day_cols = ['temp_day', 'atemp_day', 'hum_day', 'windspeed_day', 'cnt_day']

# Gabungkan data yang sesuai
corr_data = filtered_data[hour_cols + day_cols]

# Hitung korelasi
corr_matrix = corr_data.corr()

# Visualisasi korelasi menggunakan heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
st.pyplot(fig)
