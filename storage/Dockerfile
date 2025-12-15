# Use official MinIO server image
FROM minio/minio:RELEASE.2025-09-07T16-13-09Z

# Create persistent storage directory
RUN mkdir -p /data

# Download and install MinIO client
ADD https://dl.min.io/client/mc/release/linux-amd64/mc /usr/local/bin/mc
RUN chmod +x /usr/local/bin/mc

# Expose default MinIO ports
EXPOSE 9000 9001

# Start MinIO server
ENTRYPOINT ["minio", "server", "/data"]