FROM python:3.11-slim

WORKDIR /app

# Install MySQL client libraries, build tools, and netcat
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files and entrypoint
COPY . .

# Ensure script is executable
RUN chmod +x /app/entrypoint.sh

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

# Start app using entrypoint
CMD ["/app/entrypoint.sh"]




