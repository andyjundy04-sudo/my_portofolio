# 01
# Mengimpor library Streamlit untuk membuat aplikasi web interaktif
import streamlit as st

# Mengimpor Pandas untuk manipulasi dan analisis data
import pandas as pd

# Mengimpor NumPy untuk komputasi numerik
import numpy as np

# Mengimpor Plotly Express untuk visualisasi data interaktif
import plotly.express as px

# Mengimpor datetime untuk menangani data tanggal dan waktu
from datetime import datetime

#02
# Mengatur konfigurasi halaman Streamlit
st.set_page_config(
    # Judul halaman yang ditampilkan di tab browser
    page_title="Portfolio Data Analyst",

    # Icon halaman yang ditampilkan di tab browser
    page_icon="📊",

    # Mengatur layout halaman menjadi lebar (wide)
    layout="wide",  #bisa "center"

    # Mengatur sidebar agar terbuka secara default
    initial_sidebar_state="expanded"
)

#03.1
# Dekorator untuk meng-cache data dan tidak memuatnya ulang setiap kali
@st.cache_data
# Fungsi untuk menghasilkan data dashboard dan menyimpannya di cache
def generate_dashboard_data():
    # Membuat range tanggal dari 1 Januari 2024 selama 30 hari
    dates = pd.date_range('2024-01-01', periods=30)

    # Mengembalikan DataFrame dengan kolom Date, Sales, Visitors, dan Conversion
    return pd.DataFrame({
        # Kolom tanggal
        'Date': dates,

        # Kolom penjualan dengan nilai random antara 1000-5000
        'Sales': np.random.randint(1000, 5000, 30),

        # Kolom pengunjung dengan nilai random antara 500-3000
        'Visitors': np.random.randint(500, 3000, 30),

        # Kolom konversi dengan nilai random antara 0.01-0.1
        'Conversion': np.random.uniform(0.01, 0.1, 30)
    })

# Test: Lihat hasil data yang dihasilkan
# dashboard_data = generate_dashboard_data()
# dashboard_data.head()
# 03.2
# Dekorator untuk meng-cache data skills
@st.cache_data
# Fungsi untuk mengembalikan data skills/keahlian
def get_skills_data():
    # Mengembalikan DataFrame berisi daftar skill dan tingkat keahlian
    return pd.DataFrame({
        # Kolom nama skill
        'Skill': ['Python', 'SQL', 'Tableau', 'PowerBI', 'Excel', 'Statistics'],

        # Kolom profisiensi dengan nilai 0-100
        'Proficiency': [95, 90, 85, 80, 95, 85]
    })

#03.3
# Dekorator untuk meng-cache data proyek
@st.cache_data
# Fungsi untuk mengembalikan data proyek dengan kemampuan filter
def get_projects_data():
    # Membuat list berisi data-data proyek
    projects = [
        # Proyek pertama: E-commerce Sales Analysis
        {
            # Judul proyek dengan emoji
            'title': '📊 Proyek 1: E-commerce Sales Analysis',
            # Kategori proyek
            'category': 'EDA',
            # Tahun proyek dibuat
            'year': 2023,
            # Deskripsi detail tentang proyek
            'description': '''**Deskripsi:**
Melakukan analisis mendalam terhadap data penjualan e-commerce untuk mengidentifikasi
trend dan peluang pertumbuhan.

**Tools:** Python, Pandas, Matplotlib, Streamlit

**Key Insights:**
- Total sales meningkat 45% YoY
- Kategori Electronics adalah top performer
- Waktu terbaik untuk promo adalah Q4''',
            # Flag apakah proyek memiliki gambar atau tidak
            'has_image': False
        },
        # Proyek kedua: Customer Segmentation Dashboard
        {
            # Judul proyek dengan emoji
            'title': '📈 Proyek 2: Customer Segmentation Dashboard',
            # Kategori proyek
            'category': 'Dashboard',
            # Tahun proyek dibuat
            'year': 2023,
            # Deskripsi detail tentang proyek
            'description': '''**Deskripsi:**
Interactive dashboard untuk segmentasi pelanggan berdasarkan RFM analysis.

**Tools:** SQL, Tableau, Python

**Key Metrics:**
- 5 customer segments identified
- Average CLV per segment
- Churn risk prediction''',
            # Flag apakah proyek memiliki gambar atau tidak
            'has_image': False
        },
        # Proyek ketiga: Churn Prediction Model
        {
            # Judul proyek dengan emoji
            'title': '🤖 Proyek 3: Churn Prediction Model',
            # Kategori proyek
            'category': 'Prediction',
            # Tahun proyek dibuat
            'year': 2024,
            # Deskripsi detail tentang proyek
            'description': '''**Deskripsi:**
Machine learning model untuk memprediksi customer churn dengan akurasi 85%.

**Tools:** Python, Scikit-learn, XGBoost

**Performance:**
- Accuracy: 85%
- Precision: 0.82
- Recall: 0.88''',
            # Flag apakah proyek memiliki gambar atau tidak
            'has_image': False
        }
    ]

    # Mengkonversi list projects menjadi DataFrame dan mengembalikannya
    return pd.DataFrame(projects)

#04.1
# Fungsi untuk menampilkan garis pemisah
def render_divider():
    # Menampilkan garis horizontal sebagai pemisah
    st.markdown("---")

#04.2
# Fungsi untuk menampilkan navigasi di sidebar
def render_sidebar_nav():
    # Menampilkan judul navigasi di sidebar
    st.sidebar.markdown("# 📍 Navigasi")

    # Membuat tombol radio untuk memilih halaman
    page = st.sidebar.radio(
        # Label untuk radio button
        "Pilih halaman:",
        # Opsi halaman yang tersedia
        ["🏠 Beranda", "👤 Tentang Saya", "📁 Proyek", "📊 Dashboard", "📧 Contact"]
    )

    # Menampilkan pemisah di sidebar
    st.sidebar.markdown("---")

    # Menampilkan tautan media sosial di sidebar
    st.sidebar.markdown(
        """
        ### 🔗 Media Sosial
        - [LinkedIn](https://linkedin.com)
        - [GitHub](https://github.com)
        - [Email](mailto:email@example.com)
        """
    )

    # Menampilkan pemisah lagi di sidebar
    st.sidebar.markdown("---")

    # Menampilkan caption/teks kecil di sidebar
    st.sidebar.caption("© 2024 Portfolio Saya")

    # Mengembalikan halaman yang dipilih user
    return page

#04.3
# Fungsi untuk menampilkan foto profil
from pathlib import Path
def render_profile_image():
    img_path = Path("assets/Jundy Andymurti.jpg")

    if img_path.exists():
        st.image(img_path, caption="Foto Profil", use_container_width=True)
    else:
        st.warning("⚠️ Foto profil tidak ditemukan")
        st.info("💡 Pastikan file ada di folder assets/")

#05.1
# Fungsi untuk menampilkan halaman beranda
def page_beranda():
    # Membuat 2 kolom dengan rasio 2:1
    col1, col2 = st.columns([2, 1])

    # Menggunakan kolom pertama
    with col1:
        # Menampilkan judul besar dengan emoji
        st.title("🌟 Selamat Datang!")

        # Menampilkan teks markdown dengan pengenalan diri
        st.markdown(
            """
            Halo, nama saya **Muhammad Rizki**. Saya adalah seorang **Data Analyst**
            yang passionate tentang mengubah data menjadi insights yang actionable.

            Dalam portfolio ini, saya menampilkan beberapa proyek data yang telah saya kerjakan,
            dari exploratory data analysis hingga business intelligence dashboard.
            """
        )

        # Menampilkan ruang kosong untuk spacing
        st.write(" ")

        # Membuat 2 kolom untuk tombol
        col_btn1, col_btn2 = st.columns(2)

        # Menggunakan kolom pertama untuk tombol download CV
        with col_btn1:
            # Membuat tombol download CV
            if st.button("📥 Download CV"):
                # Menampilkan pesan sukses ketika tombol ditekan
                st.success("CV berhasil diunduh!")

        # Menggunakan kolom kedua untuk tombol hubungi
        with col_btn2:
            # Membuat tombol hubungi saya
            if st.button("💬 Hubungi Saya"):
                # Menampilkan pesan info ketika tombol ditekan
                st.info("Silakan scroll ke halaman Contact!")

    # Menggunakan kolom kedua untuk foto profil
    with col2:
        # Memanggil fungsi untuk menampilkan foto profil
        render_profile_image()

    # Menampilkan garis pemisah
    render_divider()

    # Menampilkan statistik singkat
    st.subheader("📈 Statistik Singkat")

    # Membuat 4 kolom untuk menampilkan metrik
    col1, col2, col3, col4 = st.columns(4)

    # Menampilkan metrik proyek selesai
    col1.metric("Proyek Selesai", 12, "+3")

    # Menampilkan metrik total dataset
    col2.metric("Total Dataset", 50, "-5")

    # Menampilkan metrik jumlah klien
    col3.metric("Clients", 8, "+2")

    # Menampilkan metrik tahun pengalaman
    col4.metric("Tahun Pengalaman", 3, "+1")

#06.1
# Fungsi untuk menampilkan halaman tentang saya
def page_tentang_saya():
    # Menampilkan judul halaman dengan emoji
    st.title("👤 Tentang Saya")

    # Menampilkan subheader untuk latar belakang
    st.subheader("Latar Belakang")

    # Menampilkan teks tentang latar belakang dan keahlian
    st.write(
        """
        Saya adalah data analyst dengan pengalaman 3+ tahun di industri e-commerce dan fintech.
        Saya berspesialisasi dalam:
        - **Data Exploration & Cleaning**: Menggunakan Pandas & NumPy
        - **Data Visualization**: Tableau, PowerBI, Streamlit
        - **Statistical Analysis**: A/B Testing, Hypothesis Testing
        - **Business Intelligence**: Dashboard development, KPI tracking
        """
    )

    # Menampilkan subheader untuk technical skills
    st.subheader("🛠️ Technical Skills")

    # Memanggil fungsi untuk mendapatkan data skills dan menyimpannya dalam variable
    skills_data = get_skills_data()

    # Membuat bar chart menggunakan Plotly Express
    fig = px.bar(
        # Data yang digunakan untuk chart
        skills_data,
        # Kolom yang ditampilkan di x-axis
        x='Skill',
        # Kolom yang ditampilkan di y-axis
        y='Proficiency',
        # Judul chart
        title='Tingkat Keahlian',
        # Kolom yang digunakan untuk warna
        color='Proficiency',
        # Skala warna yang digunakan
        color_continuous_scale='Viridis',
        # Menampilkan nilai di atas bar
        text='Proficiency'
    )

    # Menampilkan chart di Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Menampilkan subheader untuk sertifikasi
    st.subheader("📚 Sertifikasi")

    # Membuat 3 kolom untuk menampilkan sertifikasi
    cert_col1, cert_col2, cert_col3 = st.columns(3)

    # Menampilkan sertifikasi Google Analytics di kolom pertama
    cert_col1.markdown(
        """
        **Google Analytics Certification**
        ✅ Certified, 2022
        """
    )

    # Menampilkan sertifikasi SQL di kolom kedua
    cert_col2.markdown(
        """
        **SQL for Data Analysis**
        ✅ Certified, 2021
        """
    )

    # Menampilkan sertifikasi Tableau di kolom ketiga
    cert_col3.markdown(
        """
        **Data Visualization with Tableau**
        ✅ Certified, 2023
        """
    )

#07.1
# asumsi: fungsi-fungsi ini tersedia di tempat lain dalam project
# from your_module import render_divider, get_projects_data

def page_proyek():
    # Menampilkan judul halaman dengan emoji
    st.title("📁 Proyek Saya")

    # Menampilkan subheader untuk filter proyek
    st.subheader("🔍 Filter Proyek")

    # Membuat 2 kolom untuk filter
    col1, col2 = st.columns(2)

    # Menggunakan kolom pertama untuk filter kategori
    with col1:
        selected_category = st.multiselect(
            "Kategori:",
            ['EDA', 'Dashboard', 'Prediction', 'Visualization'],
            default=['EDA', 'Dashboard', 'Prediction']
        )

    # Menggunakan kolom kedua untuk filter tahun
    with col2:
        selected_year = st.slider(
            "Tahun:",
            2021,
            2024,
            (2021, 2024)
        )

    # Menampilkan garis pemisah (pastikan render_divider() didefinisikan)
    render_divider()

    # Memanggil fungsi untuk mendapatkan data proyek (harus mengembalikan pandas.DataFrame)
    projects_df = get_projects_data()

    # Pastikan selected_year adalah tuple (jika user mengkonfigurasi slider sebagai single value)
    if isinstance(selected_year, int):
        year_min, year_max = selected_year, selected_year
    else:
        year_min, year_max = selected_year

    # Melakukan filter pada data proyek berdasarkan kategori dan tahun yang dipilih
    filtered_projects = projects_df[
        (projects_df['category'].isin(selected_category)) &
        (projects_df['year'] >= year_min) &
        (projects_df['year'] <= year_max)
    ]

    # Mengecek apakah ada proyek yang sesuai dengan filter
    if filtered_projects.empty:
        st.info("📭 Tidak ada proyek yang sesuai dengan filter Anda")
        return

    # Loop untuk menampilkan setiap proyek yang telah difilter
    # Gunakan enumerate untuk membuat key tombol unik (agar tidak bentrok jika index DataFrame bukan 0..n-1)
    for i, (_, project) in enumerate(filtered_projects.iterrows()):
        # Membuat expander untuk setiap proyek (dapat diklik untuk membuka/menutup)
        with st.expander(f"{project.get('title', 'Untitled')} ({project.get('year', '')})", expanded=(i == 0)):
            # Membuat 2 kolom jika proyek memiliki gambar, jika tidak membuat 1 kolom (container)
            if project.get('has_image', False):
                col_left, col_right = st.columns([2, 1])
            else:
                col_left = st.container()
                col_right = None

            # Menggunakan kolom pertama untuk deskripsi
            with col_left:
                st.markdown(project.get('description', ''))

                # Jika ada URL proyek, gunakan itu; kalau tidak, hanya tampilkan tombol info
                proj_url = project.get('url', None)
                if proj_url:
                    # Tombol untuk membuka link di tab baru: gunakan markdown link (Streamlit akan membuka di tab baru)
                    if st.button("🔗 View Project", key=f"project_{i}"):
                        st.write(f"[Membuka project]({proj_url})")
                else:
                    if st.button("🔗 View Project", key=f"project_{i}"):
                        st.info(f"Link ke project {project.get('title', '')} akan dibuka!")

            # Mengecek apakah kolom kedua ada dan proyek memiliki gambar
            if col_right is not None and project.get('has_image', False):
                with col_right:
                    img_path = project.get('image_path', 'assets/project1_ss.png')
                    # Resolve path relative ke working directory jika bukan absolute
                    img_path = Path(img_path)
                    if not img_path.is_absolute():
                        img_path = Path.cwd() / img_path
                    if img_path.exists():
                        st.image(str(img_path), caption="Project Screenshot")
                    else:
                        st.info("📷 Screenshot tidak tersedia")

#08.1
# Fungsi untuk menampilkan halaman dashboard
def page_dashboard():
    # Menampilkan judul halaman dengan emoji
    st.title("📊 Interactive Dashboard")

    # Memanggil fungsi untuk mendapatkan data dashboard yang sudah di-cache
    dashboard_data = generate_dashboard_data()

    # Menampilkan subheader untuk KPI metrics
    st.subheader("📌 KPI Metrics")

    # Membuat 4 kolom untuk menampilkan KPI
    col1, col2, col3, col4 = st.columns(4)

    # Menghitung total penjualan dengan menjumlahkan kolom Sales
    total_sales = dashboard_data['Sales'].sum()

    # Menghitung total pengunjung dengan menjumlahkan kolom Visitors
    total_visitors = dashboard_data['Visitors'].sum()

    # Menghitung rata-rata konversi dengan merata-rata kolom Conversion
    avg_conversion = dashboard_data['Conversion'].mean()

    # Menghitung rata-rata nilai order dengan merata-rata kolom Sales
    avg_order_value = dashboard_data['Sales'].mean()

    # Menampilkan metric total penjualan di kolom pertama
    col1.metric("Total Sales", f"Rp {total_sales:,.0f}", "+15%")

    # Menampilkan metric total pengunjung di kolom kedua
    col2.metric("Total Visitors", f"{total_visitors:,}", "+12%")

    # Menampilkan metric rata-rata konversi di kolom ketiga
    col3.metric("Avg Conversion", f"{avg_conversion:.2%}", "+8%")

    # Menampilkan metric rata-rata nilai order di kolom keempat
    col4.metric("Avg Order Value", f"Rp {avg_order_value:,.0f}", "-3%")

    # Menampilkan garis pemisah
    render_divider()

    # Menampilkan subheader untuk sales trend
    st.subheader("📈 Sales Trend")

    # Membuat line chart untuk menampilkan tren penjualan harian
    fig1 = px.line(
        # Data yang digunakan untuk chart
        dashboard_data,
        # Kolom yang ditampilkan di x-axis
        x='Date',
        # Kolom yang ditampilkan di y-axis
        y='Sales',
        # Judul chart
        title='Daily Sales',
        # Menampilkan marker pada setiap data point
        markers=True
    )

    # Menampilkan chart di Streamlit
    st.plotly_chart(fig1, use_container_width=True)

    # Membuat 2 kolom untuk menampilkan 2 chart sekaligus
    col1, col2 = st.columns(2)

    # Menggunakan kolom pertama untuk chart pengunjung harian
    with col1:
        # Membuat bar chart untuk menampilkan pengunjung harian
        fig2 = px.bar(
            # Mengelompokkan data berdasarkan tanggal dan menjumlahkan nilai numerik
            dashboard_data.groupby('Date').sum(numeric_only=True).reset_index(),
            # Kolom yang ditampilkan di x-axis
            x='Date',
            # Kolom yang ditampilkan di y-axis
            y='Visitors',
            # Judul chart
            title='Daily Visitors'
        )

        # Menampilkan chart di Streamlit
        st.plotly_chart(fig2, use_container_width=True)

    # Menggunakan kolom kedua untuk scatter plot
    with col2:
        # Membuat scatter plot untuk menampilkan hubungan antara pengunjung dan penjualan
        fig3 = px.scatter(
            # Data yang digunakan untuk chart
            dashboard_data,
            # Kolom yang ditampilkan di x-axis
            x='Visitors',
            # Kolom yang ditampilkan di y-axis
            y='Sales',
            # Kolom yang digunakan untuk ukuran bubble
            size='Conversion',
            # Judul chart
            title='Visitors vs Sales',
            # Kolom yang digunakan untuk warna
            color='Conversion',
            # Skala warna yang digunakan
            color_continuous_scale='Viridis'
        )

        # Menampilkan chart di Streamlit
        st.plotly_chart(fig3, use_container_width=True)

#09.1
import re
from typing import Optional

import streamlit as st

# Optional: provide a simple divider if render_divider isn't defined elsewhere
try:
    render_divider  # type: ignore
except NameError:
    def render_divider() -> None:
        st.markdown("---")


def _is_valid_email(email: str) -> bool:
    """Very small email validity check (sufficient for simple form validation)."""
    if not email:
        return False
    # basic pattern: something@something.something
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


# Fungsi untuk menampilkan halaman contact
def page_contact() -> None:
    # Menampilkan judul halaman dengan emoji
    st.title("📧 Get in Touch")

    # Menampilkan teks penjelasan
    st.write(
        "Jika Anda tertarik untuk berkolaborasi atau memiliki pertanyaan, "
        "silakan hubungi saya melalui form di bawah!"
    )

    # Menampilkan garis pemisah
    render_divider()

    # Membuat form untuk contact
    with st.form("contact_form"):
        # Membuat input text untuk nama lengkap
        nama = st.text_input("Nama Lengkap")

        # Membuat input text untuk email
        email = st.text_input("Email")

        # Membuat selectbox untuk subjek
        subject = st.selectbox(
            "Subjek:",
            ['Project Inquiry', 'Collaboration', 'General Question', 'Others']
        )

        # Membuat text area untuk pesan dengan tinggi 150 pixel
        message = st.text_area("Pesan:", height=150)

        # Membuat tombol submit untuk mengirim form
        submitted = st.form_submit_button("📤 Send Message")

        # Mengecek apakah form telah disubmit
        if submitted:
            # Validasi sederhana
            if not nama or not email or not message:
                st.error("❌ Mohon isi semua field!")
            elif not _is_valid_email(email):
                st.error("❌ Format email tidak valid. Contoh: nama@domain.com")
            else:
                # Menampilkan pesan sukses dengan nama user
                st.success(
                    f"✅ Terima kasih, {nama}! Pesan Anda telah dikirim. "
                    "Saya akan menghubungi Anda dalam 24 jam."
                )
                # (Opsional) tampilkan ringkasan
                st.markdown("**Rincian pesan:**")
                st.write(f"- Email: {email}")
                st.write(f"- Subjek: {subject}")
                st.write(f"- Pesan: {message}")

    # Menampilkan garis pemisah
    render_divider()

    # Menampilkan subheader untuk kontak lainnya
    st.subheader("🔗 Kontak Lainnya")

    # Membuat 3 kolom untuk menampilkan kontak lainnya
    col1, col2, col3 = st.columns(3)

    # Menampilkan kontak email di kolom pertama
    col1.markdown(
        """
        **Email**
        📧 [email@example.com](mailto:email@example.com)
        """
    )

    # Menampilkan kontak LinkedIn di kolom kedua
    col2.markdown(
        """
        **LinkedIn**
        💼 [linkedin.com/in/username](https://linkedin.com)
        """
    )

    # Menampilkan kontak GitHub di kolom ketiga
    col3.markdown(
        """
        **GitHub**
        🐙 [github.com/username](https://github.com)
        """
    )

#010.1
import streamlit as st
from typing import Callable, Dict

# Attempt to import page functions; if they are defined in other modules,
# adjust the import paths accordingly.
try:
    from pages import page_beranda, page_tentang_saya, page_proyek, page_dashboard, page_contact  # type: ignore
except Exception:
    # If the pages are defined in the same module, the above import will fail;
    # fall back to attributes in the current module (caller should define them).
    page_beranda = globals().get("page_beranda")
    page_tentang_saya = globals().get("page_tentang_saya")
    page_proyek = globals().get("page_proyek")
    page_dashboard = globals().get("page_dashboard")
    page_contact = globals().get("page_contact")


def _missing_page(name: str) -> Callable[[], None]:
    """Return a function that shows an error for missing pages."""
    def _show_missing():
        st.error(f"Halaman '{name}' belum diimplementasikan atau tidak dapat diimpor.")
    return _show_missing


def main() -> None:
    # Optional: configure the Streamlit page (adjust as needed)
    st.set_page_config(page_title="Portfolio", layout="wide")

    # Build mapping from sidebar labels to page callables.
    pages: Dict[str, Callable[[], None]] = {
        "🏠 Beranda": page_beranda or _missing_page("🏠 Beranda"),
        "👤 Tentang Saya": page_tentang_saya or _missing_page("👤 Tentang Saya"),
        "📁 Proyek": page_proyek or _missing_page("📁 Proyek"),
        "📊 Dashboard": page_dashboard or _missing_page("📊 Dashboard"),
        "📧 Contact": page_contact or _missing_page("📧 Contact"),
    }

    # Render the sidebar navigation. This function should return one of the keys above.
    # If render_sidebar_nav is defined elsewhere, call it; otherwise show a simple selectbox.
    renderer = globals().get("render_sidebar_nav")
    if callable(renderer):
        try:
            selected_page = renderer()
        except Exception as e:
            st.error(f"Terjadi error saat merender sidebar: {e}")
            selected_page = None
    else:
        # Fallback: simple selectbox in sidebar
        selected_page = st.sidebar.selectbox("Navigate to", list(pages.keys()))

    # If the renderer returned None or an unexpected value, default to the first page.
    if not selected_page or selected_page not in pages:
        selected_page = list(pages.keys())[0]

    # Call the page function
    page_func = pages[selected_page]
    try:
        page_func()
    except Exception as e:
        st.exception(e)


if __name__ == "__main__":
    main()

