FROM python:3.11-slim

WORKDIR /app

# Install MySQL client libraries and build tools
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

# Run entrypoint script (or flask directly)
CMD ["flask", "run", "--host=0.0.0.0"]
