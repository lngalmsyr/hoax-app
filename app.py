import streamlit as st
from st_pages import Page, show_pages


show_pages(
    [
        Page("pages/detection.py", "Deteksi Berita Palsu", "🏠"),
        Page("pages/list.py", "Tampilkan Berita Hoax Sekarang", ":books:"),
        Page("pages/about.py", "Halaman Tentang", "🧐")
    ])