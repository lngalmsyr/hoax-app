FROM python:3.9-slim

# Install Python dependencies
RUN pip install -r requirements.txt

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"] 