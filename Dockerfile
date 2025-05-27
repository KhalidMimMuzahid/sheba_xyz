# --- Base image ---
    FROM python:3.11-slim

    # --- Set working directory ---
    WORKDIR /app
    
    # --- Install system deps for Postgres client and wait script ---
    RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

    
    # --- Copy requirements and install ---
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # --- Copy app code ---
    COPY . .
    
    # --- Make entrypoint script executable ---
    RUN chmod +x ./start.sh
    
    # --- Expose FastAPI port ---
    EXPOSE 8000
    
    # --- Entrypoint ---
    CMD ["./start.sh"]
    