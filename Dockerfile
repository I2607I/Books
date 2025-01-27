# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl build-essential libpq-dev && \
    apt-get clean && \
    apt install python3-dev -y && \
    apt-get install build-essential -y && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app


# Expose port (if your app runs on a specific port)
#EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "python -m books"]