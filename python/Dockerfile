FROM python:3.12-alpine AS runner
WORKDIR /app

# Install Python
RUN apk add --no-cache python3 py3-pip bash && \
    ln -sf python3 /usr/bin/python

# Set environment variable for real-time logs
ENV PYTHONUNBUFFERED=1

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose your port
EXPOSE 8000

# Start the Python app
CMD ["python3", "app.py"]
