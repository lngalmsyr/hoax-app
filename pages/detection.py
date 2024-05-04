import streamlit as st
from st_pages import add_page_title
from streamlit_extras.colored_header import colored_header
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
import numpy as np

#load data
import pandas as pd

df = pd.read_csv('./assets/df.csv')

# Load Tokenizer and Model (assuming you've saved them correctly)
tokenizer = AutoTokenizer.from_pretrained("lngalmsyr/hoax-appClass")
model = AutoModelForSequenceClassification.from_pretrained("lngalmsyr/hoax-appClass")
trainer = Trainer(model=model)

add_page_title(layout="wide")
colored_header(
    description="Welcome to Our Projects, Tugas Akhir Lanang Almasyuri (120450109)!",
    label="MESIN DETEKSI BERITA PALSU DENGAN METODE FINETUNING INDOBERT",
    color_name="violet-70",
)

# Prediction Function (modified to handle potential indexing issues)
def predict(text):
    # Tokenize the text
    tokenized = tokenizer(text, padding='max_length', max_length=256)

    # Make prediction and get the label index directly
    label = trainer.predict([tokenized]).predictions.argmax(1)[0]

    # Return prediction as text
    if label == 0:
        return f'Predicted: Negatif [{label}], berita ini merupakan fakta'
    elif label == 1:
        return f'Predicted: Positif [{label}], berita ini merupakan hoax/palsu'

# Form Input dan Deteksi
text = st.text_input('Silahkan Masukkan Kata Kunci')
col1, col2 = st.columns([1, 1])
with col1:
    st.text("Klik Tombol Detect Untuk Melakukan Deteksi Berita Palsu")
    #buat disclaimer berwarna merah
    if st.button('Detect'):
        if text:
            prediction_result = predict(text)
            st.write(prediction_result)
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