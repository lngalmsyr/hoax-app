
import torch
import streamlit as st
from st_pages import add_page_title
from streamlit_extras.colored_header import colored_header
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load data
import pandas as pd

df = pd.read_csv('./assets/dfdf.csv')

model_pkl_file = "./assets/fix_model_cpu.pkl"  # load model from pickle file
with open(model_pkl_file, 'rb') as file:
    model = pickle.load(file)

# save the iris classification model as a pickle file
tokenizer_pkl_file = "./assets/fix_tokenizer.pkl"
with open(tokenizer_pkl_file, 'rb') as file:
    loaded_tokenizer = pickle.load(file)

add_page_title(layout="wide")
colored_header(
    description="Welcome to Our Projects, Tugas Akhir Lanang Almasyuri (120450109)!",
    label="MESIN DETEKSI BERITA PALSU DENGAN METODE FINETUNING INDOBERT",
    color_name="violet-70",
)

# Fungsi Prediksi (updated based on predict2)
def predict(text):
    """Melakukan prediksi sentimen pada teks menggunakan model yang dimuat."""
    encoded_input = loaded_tokenizer(text, return_tensors='pt', padding='max_length', max_length=256)

    # Pastikan model dan input berada pada device yang sama (misalnya GPU)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model.to(device)  # Pindahkan model ke device yang dipilih
    encoded_input = {k: v.to(device) for k, v in encoded_input.items()}  # Pindahkan input ke device yang sama

    # Prediksi dengan model (forward pass)
    with torch.no_grad():
        output = model(**encoded_input)

    # Mendapatkan logits dan label
    logits = output.logits
    label = torch.argmax(logits, dim=1).item()

    return label

# Form Input dan Deteksi
text = st.text_input('Silahkan Masukkan Kata Kunci')
col1, col2 = st.columns([1, 1])
with col1:
    st.text("Klik Tombol Detect Untuk Melakukan Deteksi Berita Palsu")
    #buat disclaimer berwarna merah
    if st.button('Detect'):
        if text:
            label = predict(text)
            if label == 0:
                st.write(f'Predicted: Negatif [{label}], berita ini merupakan fakta')
            elif label == 1:
                st.write(f'Predicted: Positif [{label}], berita ini merupakan hoax/palsu')
            else:
                st.write('Masukkan Kata Kunci Berita Untuk Mengecek Keberitaan')

    #buat text seperti warning didalam kotak kuning
    
    st.warning("""
               Disclaimer: Hasil deteksi berita palsu ini hanya berdasarkan pada judul berita yang ada di dataset. Hasil deteksi ini tidak sepenuhnya akurat dan hanya digunakan sebagai referensi
               
               Masukkan Kata Kunci berita, usahakan kata kunci berita yang dimasukkan lebih spesifik agar mendapatkan hasil yang lebih akurat.
               """)

with col2:
    if text:  # Only execute if 'text' is not empty
        st.text("Berikut adalah artikel yang mungkin terkait:")
        vectorizer = TfidfVectorizer()
        # Ambil list judul berita dari df 
        judul_berita = df['judul'].tolist()  # More efficient way to get the list of titles

        # Fit and transform the titles
        judul_vectors = vectorizer.fit_transform(judul_berita)

        # Transform the input text
        text_vectors = vectorizer.transform([text])

        # Calculate cosine similarity
        similarity_scores = cosine_similarity(text_vectors, judul_vectors)

        # Get the indices of the most similar articles
        sorted_indices = similarity_scores.argsort()[0][::-1]

        # Get the top N recommended articles (you can adjust N as needed)
        N = 5  # Number of recommendations
        recommended_articles = df.iloc[sorted_indices[:N]]

        # Display the recommendations
        for index, row in recommended_articles.iterrows():
            st.write(row['judul'])
            st.write(row['url'])
            if row['label'] == 'positive':
                st.write('Ini adalah Berita Palsu')
            else:
                st.write('Ini adalah Berita Benar')
            st.write("---")  # Separator between articles
    else:
        st.write("Masukkan teks untuk mendapatkan rekomendasi artikel.")  # Prompt for input