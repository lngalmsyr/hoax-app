FROM python:3.9-slim

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install torch 
RUN pip install transformers[torch]

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

RUN pip install -r requirements.txt

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"] 