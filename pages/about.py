import streamlit as st
from st_pages import add_page_title
from streamlit_extras.colored_header import colored_header

add_page_title(layout="wide")

colored_header(
    label="MESIN DETEKSI BERITA PALSU DENGAN METODE FINETUNING INDOBERT", 
    description="Tugas Akhir Lanang Almasyuri (120450109)",
    color_name="violet-70"
)
st.write("""
        Project ini merupakan tugas akhir dari **Lanang Almasyuri**, mahasiswa program studi Sains Data di Institut Teknologi Sumatera. 
        Project ini bertujuan untuk  membangun sebuah model machine learning yang dapat mendeteksi berita palsu (hoax) dalam bahasa Indonesia menggunakan metode fine-tuning pada model IndoBERT.
    """)

st.write("""
        **Kekurangan dan Pengembangan Lebih Lanjut**

        Project ini masih dalam tahap pengembangan dan memiliki beberapa kekurangan, di antaranya:
        * Data yang digunakan masih terbatas pada data yang diambil dari website turnbackhoax.id
        * hasil prediksi masih belum optimal, hanya dapat deteksi berita palsu ini hanya berdasarkan pada judul berita yang ada di dataset. Hasil deteksi ini tidak sepenuhnya akurat dan hanya digunakan sebagai referensi
        * Usahakan Masukkan Kata Kunci berita, usahakan kata kunci berita yang dimasukkan lebih spesifik agar mendapatkan hasil yang lebih akurat.
        
        Kami sangat terbuka untuk masukan dan kontribusi dari siapa pun yang ingin mengembangkan project ini lebih lanjut. 
        Kode sumber project ini tersedia di GitHub: 
        [Link ke Repository GitHub](https://github.com/lngalmsyr/hoax-app.git)  
""")

st.write("""
    **Terima kasih atas kunjungan Anda!**
""")