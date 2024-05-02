FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc curl gnupg && apt-get clean

# Install gcloud CLI
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz \
    && mkdir -p /usr/local/gcloud \
    && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
    && /usr/local/gcloud/google-cloud-sdk/install.sh \
    && rm /tmp/google-cloud-sdk.tar.gz

# Add gcloud to PATH
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Download models and data from Cloud Storage
ENV FIX_MODEL_URL https://storage.googleapis.com/hoax-sto/fix_model.pkl
ENV FIX_MODEL_CPU_URL https://storage.googleapis.com/hoax-sto/fix_model_cpu.pkl
ENV FIX_TOKENIZER_URL https://storage.googleapis.com/hoax-sto/fix_tokenizer.pkl

RUN curl -o fix_model.pkl $FIX_MODEL_URL \
    && curl -o fix_model_cpu.pkl $FIX_MODEL_CPU_URL \
    && curl -o fix_tokenizer.pkl $FIX_TOKENIZER_URL

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]
