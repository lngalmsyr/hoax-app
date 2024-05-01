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
        Project ini bertujuan untuk ... (jelaskan tujuan project Anda).
    """)

st.write("""
        **Kekurangan dan Pengembangan Lebih Lanjut**

        Project ini masih dalam tahap pengembangan dan memiliki beberapa kekurangan, di antaranya:
        * ... (sebutkan beberapa kekurangan project Anda)
        * ... 

        Kami sangat terbuka untuk masukan dan kontribusi dari siapa pun yang ingin mengembangkan project ini lebih lanjut. 
        Kode sumber project ini tersedia di GitHub: 
        [Link ke Repository GitHub](https://github.com/your-username/your-repository)  
""")

st.write("""
    **Terima kasih atas kunjungan Anda!**
""")