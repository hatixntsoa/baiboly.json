# Use a lightweight Python image as the base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Copy project files to the container
COPY . /app

# Install dependencies
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Activate the virtual environment in PATH
ENV PATH="/opt/venv/bin:$PATH"

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]