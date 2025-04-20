# Use official Python image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Expose the app's port
EXPOSE 3000

# Run the Flask app
CMD ["python", "app.py"]
