FROM python:3.9-slim

# Instalasi dependensi dan gcloud CLI
RUN apt-get update && apt-get install -y libpq-dev gcc curl gnupg && \
    curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz && \
    mkdir -p /usr/local/gcloud && \
    tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz && \
    /usr/local/gcloud/google-cloud-sdk/install.sh && \
    rm /tmp/google-cloud-sdk.tar.gz && \
    apt-get clean

# Tambahkan gcloud ke PATH
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

# Set direktori kerja
WORKDIR /app

# Buat direktori untuk model
RUN mkdir -p /app/models

# Download model
RUN curl -o /app/models/fix_model.pkl $FIX_MODEL_URL \
    && curl -o /app/models/fix_model_cpu.pkl $FIX_MODEL_CPU_URL \
    && curl -o /app/models/fix_tokenizer.pkl $FIX_TOKENIZER_URL

# Copy file aplikasi
COPY . .

# Instal dependensi Python
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8501

# Jalankan aplikasi Streamlit
CMD ["streamlit", "run", "app.py"]