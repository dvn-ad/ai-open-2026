FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

# Avoid interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies needed for OpenCV, PaddleOCR, and other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    git \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

# Upgrade pip
RUN python3 -m pip install --no-cache-dir --upgrade pip

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install PyTorch with CUDA 12.1 support to leverage GPU
RUN python3 -m pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cu121

# Install remaining dependencies with an increased timeout
RUN python3 -m pip install --no-cache-dir --default-timeout=1000 -r requirements.txt


# Copy the rest of the application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Default command runs the FastAPI server
CMD ["uvicorn", "src.validation.api:app", "--host", "0.0.0.0", "--port", "8000"]
