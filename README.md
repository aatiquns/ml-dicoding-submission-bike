# Bike Sharing Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dan memvisualisasikan data penyewaan sepeda berdasarkan waktu dan kondisi cuaca. Dengan menggunakan dashboard interaktif, pengguna dapat memahami tren penyewaan sepeda, mengevaluasi performa operasional, dan menemukan korelasi antara variabel cuaca dan jumlah penyewaan.

## Fitur Dashboard
1. **Filter Data:**
   - Filter berdasarkan musim, bulan, hari kerja, dan periode tanggal.
2. **Visualisasi Operasional KPI:**
   - Rata-rata dan total penyewaan per jam dan per hari.
3. **Penyewaan Berdasarkan Musim:**
   - Visualisasi perbandingan jumlah penyewaan berdasarkan musim (_hour_ dan _day_).
4. **Tren Penyewaan Harian:**
   - Grafik tren harian untuk data _hour_ dan _day_.
5. **Distribusi Penyewaan Berdasarkan Jam:**
   - Grafik batang rata-rata penyewaan untuk setiap jam.
6. **Korelasi antara Data _Hour_ dan _Day_:**
   - Heatmap korelasi antara variabel _hour_ dan _day_.

## Cara Menjalankan Proyek
1. **Clone repository:**
   ```bash
   git clone https://github.com/aatiquns/ml-dicoding-submission-bike.git
   cd ml-dicoding-submission-bike
3. **Instal Dependensi:**
   ```bash
    pip install -r requirements.txt
4. **Jalankan Aplikasi Streamlit:**
   ```bash
    streamlit run dashboard/dashboard.py

### **2. requirements.txt**
Berikut adalah daftar pustaka yang dibutuhkan untuk menjalankan proyek dan melakukan deploy di Streamlit Community Cloud:
    ```bash
    streamlit pandas numpy matplotlib seaborn scikit-learn

### **3. url.txt**
File ini berisi URL ke repository GitHub dan aplikasi Streamlit:
    [github](https://github.com/aatiquns/ml-dicoding-submission-bike)
    [streamlit](https://atiq-ml-dicoding-submission.streamlit.app)