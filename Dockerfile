# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12

WORKDIR /app
EXPOSE 8080


# Set working directory in container
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .
EXPOSE 5000

# Run command when container launches
CMD ["python", "app.py"]
