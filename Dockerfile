FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc google-cloud-storage

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Download model from Cloud Storage
RUN gsutil cp gs://hoax-sto/fix_model.pkl ./fix_model.pkl
RUN gsutil cp gs://hoax-sto/fix_model_cpu.pkl ./fix_model_cpu.pkl
RUN gsutil cp gs://hoax-sto/fix_tokenizer.pkl ./fix_tokenizer.pkl
RUN gsutil cp gs://hoax-sto/df.csv ./df.csv

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]